# -*- coding:utf-8 -*-
import urllib3
from PyQt5.QtCore import pyqtSignal, QThread
from threading import Thread,Lock
from settings import *
import requests
from lxml import etree
import re
import time
import random
import copy
from db_class import db_class

urllib3.disable_warnings()


class SearchClass(QThread):
    # 创建信号结果list传给主窗口
    Sig_result = pyqtSignal(list)
    Sig_result_count = pyqtSignal(str)
    Sig_search_end = pyqtSignal()
    Sig_verify = pyqtSignal()

    def __init__(self, id=None,keys_list=None, engine_list=None, level=None, thread=None, timeout=None):
        super(SearchClass, self).__init__()

        self.flag = 1
        self.id = id
        self.keys_list = keys_list
        self.engine_list = engine_list
        self.level = int(level)
        self.timeout = int(timeout)
        self.thread_count = int(thread)
        self.result_list = []
        self.old_set = set()
        self.getList()
        self.db = db_class()
        self.db.open()
        self.db.start()
        self.wordCount = 0
        self.wordDict = {}
        self.lock = Lock()
        self.spiderFunc = {
            'pcbaidu': self.PCbaidu,
            'pcsogou': self.PCsogou,
            'mbaidu': self.Mbaidu,
            'msogou': self.Msogou,
            'mshenma': self.Msm
        }

    def getList(self):
        with open('filter.txt', 'r', encoding='utf-8') as f:
            self.filter = [li for li in f.read().split('\n') if li.strip()]
        with open('contain.txt', 'r', encoding='utf-8') as f:
            self.contain = [li for li in f.read().split('\n') if li.strip()]

    def run(self):
        try:
            for key in self.keys_list:
                for engine in self.engine_list:
                    if self.flag:
                        self.thread_pool(self.spiderFunc[engine], [key], 0)
        except Exception as e:
            print(e)
        finally:
            self.Sig_search_end.emit()
            self.db.switch = False

    def get_data(self, func, key, count):
        try:
            result = func(key)
            if self.filter:
                result = [li for li in result if all(F.upper() not in li.upper() for F in self.filter if F.strip())]
            if self.contain:
                result = [li for li in result if any(C.upper() in li.upper() for C in self.contain if C.strip())]
            result = copy.deepcopy(result)
            self.result_list += result
            self.db.q.put([[self.id, key, self.id, key, self.id, key] for key in result])
            self.lock.acquire()
            self.wordCount += len(result)
            for i in result:
                self.wordDict[i] = self.wordDict.get(i, 0) + 1
            result = copy.deepcopy(sorted(self.wordDict.items(), key=lambda kv: (kv[1], kv[0]), reverse=True))
            self.Sig_result.emit(result)
            self.Sig_result_count.emit(str(self.wordCount))
            self.lock.release()
            time.sleep(0.5)
            return None
        except Exception as e:
            if count < 3:
                count += 1
                return self.get_data(func, key, count)

    def thread_pool(self, func, keylist, count):
        try:
            if self.level > count:
                result_list = list(set(keylist) - self.old_set)
                self.old_set |= set(keylist)
                for n in range(0, len(result_list), self.thread_count):
                    if self.flag:
                        tasks = [Thread(target=self.get_data, args=(func, key, 0)) for key in
                                 result_list[n:n + self.thread_count]]
                        for t in tasks:
                            time.sleep(0.3)
                            t.start()
                        for t in tasks: t.join()
                count += 1
                return self.thread_pool(func, self.result_list, count)
            return None
        except Exception as e:
            print(e)

    def PCbaidu(self, key):
        '''
        pc百度搜索
        :param key:关键词
        :return: 结果集合
        '''
        try:
            sess = requests.session()
            url = 'https://www.baidu.com/s?ie=utf-8&mod=1&isbd=1&wd={}'.format(key)
            response = sess.get(url, headers=PCheaders, timeout=self.timeout, allow_redirects=False)
            status_code1 = response.status_code
            html = etree.HTML(response.text)
            rs = html.xpath('//div[@id="rs"]//a/text()')
            url = 'https://www.baidu.com/sugrec?prod=pc&wd={}'.format(key)
            response = sess.get(url, headers=PCheaders, timeout=self.timeout, allow_redirects=False)
            status_code2 = response.status_code
            try:
                sugrec = [li['q'] for li in response.json()['g']]
            except Exception as e:
                sugrec = []
            if status_code1 + status_code2 > 400:
                time.sleep(random.uniform(1, 3))
                self.Sig_verify.emit()
                time.sleep(10)
                return self.PCbaidu(key)
            return rs + sugrec
        except Exception as e:
            raise e

    def Mbaidu(self, key):
        '''
        m百度搜索
        :param key:关键词
        :return: 结果集合
        '''
        try:
            sess = requests.session()
            sugrec = []
            t = str(time.time()).replace('.', '')[:-1]
            url = 'http://m.baidu.com/s?word={}'.format(key)
            response = sess.get(url, headers=Mheaders, timeout=self.timeout, allow_redirects=False)
            status_code1 = response.status_code
            html = etree.HTML(response.text)
            rs = html.xpath('//div[contains(text(), "其他人还在搜")]/../../..//span/text()')[:-1]
            qid = re.search('lid=(.*?)"', response.text)[1] if re.search('lid=(.*?)"', response.text) else ''
            url = 'http://m.baidu.com/rec?platform=wise&rset=rcmd&word={}&qid={}&t={}'.format(key, qid, t)
            response = sess.get(url, headers=Mheaders, timeout=self.timeout, allow_redirects=False)
            status_code2 = response.status_code
            try:
                for li in response.json()['rs']['rcmd']['list']:
                    sugrec += li['down'] + li['up']
            except Exception as e:
                pass
            if status_code1 + status_code2 > 400:
                time.sleep(random.uniform(1, 3))
                self.Sig_verify.emit()
                time.sleep(10)
                return self.Mbaidu(key)
            return rs + sugrec
        except Exception as e:
            raise e

    def PCsogou(self, key):
        '''
        pc搜狗搜索
        :param key:关键词
        :return: 结果集合
        '''
        try:
            url = 'https://www.sogou.com/web?query={}'.format(key)
            sess = requests.session()
            response = sess.get(url, headers=PCheaders, timeout=self.timeout, allow_redirects=False)
            status_code1 = response.status_code
            html = etree.HTML(response.text)
            rs = html.xpath('//caption[contains(text(), "相关搜索")]/..//a/text()')
            url = 'https://www.sogou.com/suggnew/ajajjson?key={}&type=web'.format(key)
            response = sess.get(url, headers=headers, timeout=self.timeout, allow_redirects=False)
            status_code2 = response.status_code
            try:
                sugrec = eval('[' + re.search(',\[(.*?)\]', response.text)[1] + ']')
            except Exception as e:
                sugrec = []
            if status_code1 + status_code2 > 400:
                time.sleep(random.uniform(1, 3))
                self.Sig_verify.emit()
                time.sleep(10)
                return self.PCsogou(key)
            return rs + sugrec
        except Exception as e:
            raise e

    def Msogou(self, key):
        '''
        m搜狗搜索
        :param key:关键词
        :return: 结果集合
        '''
        try:
            url = 'https://m.sogou.com/web/searchList.jsp?keyword={}'.format(key)
            sess = requests.session()
            response = sess.get(url, headers=Mheaders, timeout=self.timeout, allow_redirects=False)
            status_code1 = response.status_code
            try:
                div = re.search('相关搜索</span></h3>(.*?)</div>', response.text, re.S | re.I)[1]
                rs = re.findall('<a.*?>(.*?)</a>', div, re.DOTALL)
            except Exception as e:
                rs = []
            url = 'https://m.sogou.com/web/sugg/{}?vr=1&s=1&source=wapsearch'.format(key)
            response = sess.get(url, headers=Mheaders, timeout=self.timeout, allow_redirects=False)
            status_code2 = response.status_code
            try:
                sugrec = [li['q'] for li in response.json()['s']]
            except Exception as e:
                sugrec = []
            if status_code1 + status_code2 > 400:
                time.sleep(random.uniform(1, 3))
                self.Sig_verify.emit()
                time.sleep(10)
                return self.Msogou(key)
            return rs + sugrec
        except Exception as e:
            raise e

    def Msm(self, key):
        '''
        m神马搜索
        :param key:关键词
        :return: 结果集合
        '''
        try:
            url = 'https://m.sm.cn/s?q={}&from=smor&safe=1&snum=6'.format(key)
            sess = requests.session()
            response = sess.get(url, headers=Mheaders, timeout=self.timeout, allow_redirects=False)
            status_code1 = response.status_code
            html = etree.HTML(response.text)
            rs = html.xpath('//h2[contains(text(), "相关搜索")]/..//span/text()')
            url = 'https://sugs.m.sm.cn/web?t=w&uc_param_str=dnnwnt&scheme=https&fr=android&q={}&&callback=jsonp2'.format(
                key)
            response = sess.get(url, headers=Mheaders, timeout=self.timeout, allow_redirects=False)
            status_code2 = response.status_code
            try:
                down = re.search('jsonp2\((.*)\);', response.text, re.S | re.I)[1]
                sugrec = [li['w'] for li in eval(down)['r']]
            except Exception as e:
                sugrec = []
            if status_code1 + status_code2 > 400:
                time.sleep(random.uniform(1, 3))
                self.Sig_verify.emit()
                time.sleep(10)
                return self.Msm(key)
            return rs + sugrec
        except Exception as e:
            raise e
