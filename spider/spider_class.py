from settings import *
import requests
from lxml import etree
import re
import time
import random
from requests import exceptions

def verify(func):
    def inner(key, timeout, Sig_verify):
        rs, sugrec, code = func(key, timeout, Sig_verify)
        if code > 400:
            time.sleep(random.uniform(1, 3))
            Sig_verify.emit()
            time.sleep(10)
            return func(key, timeout, Sig_verify)
        result = rs + sugrec
        return result
    return inner


@verify
def PCbaidu(key, timeout, Sig_verify):
    '''
    pc百度搜索
    :param key:关键词
    :return: 结果集合
    '''
    try:
        sess = requests.session()
        url = 'https://www.baidu.com/s?ie=utf-8&mod=1&isbd=1&wd={}'.format(key)
        response = sess.get(url, headers=PCheaders, timeout=timeout,allow_redirects=False)
        status_code1 = response.status_code
        html = etree.HTML(response.text)
        rs = html.xpath('//div[@id="rs"]//a/text()')
        url = 'https://www.baidu.com/sugrec?prod=pc&wd={}'.format(key)
        response = sess.get(url, headers=PCheaders, timeout=timeout,allow_redirects=False)
        status_code2 = response.status_code
        try:
            sugrec = [li['q'] for li in response.json()['g']]
        except Exception as e:
            sugrec = []
        return rs, sugrec, status_code1 + status_code2
    except Exception as e:
        raise e


@verify
def Mbaidu(key, timeout, Sig_verify):
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
        response = sess.get(url, headers=Mheaders, timeout=timeout,allow_redirects=False)
        status_code1 = response.status_code
        html = etree.HTML(response.text)
        rs = html.xpath('//div[contains(text(), "其他人还在搜")]/../../..//span/text()')[:-1]
        qid = re.search('lid=(.*?)"', response.text)[1] if re.search('lid=(.*?)"', response.text) else ''
        url = 'http://m.baidu.com/rec?platform=wise&rset=rcmd&word={}&qid={}&t={}'.format(key, qid, t)
        response = sess.get(url, headers=Mheaders, timeout=timeout,allow_redirects=False)
        status_code2 = response.status_code
        try:
            for li in response.json()['rs']['rcmd']['list']:
                sugrec += li['down'] + li['up']
        except Exception as e:
            pass
        return rs, sugrec, status_code1 + status_code2
    except Exception as e:
        raise e


@verify
def PCsogou(key, timeout, Sig_verify):
    '''
    pc搜狗搜索
    :param key:关键词
    :return: 结果集合
    '''
    try:
        url = 'https://www.sogou.com/web?query={}'.format(key)
        sess = requests.session()
        response = sess.get(url, headers=PCheaders, timeout=timeout,allow_redirects=False)
        status_code1 = response.status_code
        html = etree.HTML(response.text)
        rs = html.xpath('//caption[contains(text(), "相关搜索")]/..//a/text()')
        url = 'https://www.sogou.com/suggnew/ajajjson?key={}&type=web'.format(key)
        response = sess.get(url, headers=headers, timeout=timeout,allow_redirects=False)
        status_code2 = response.status_code
        try:
            sugrec = eval('[' + re.search(',\[(.*?)\]', response.text)[1] + ']')
        except Exception as e:
            sugrec = []
        return rs, sugrec, status_code1 + status_code2
    except Exception as e:
        raise e


@verify
def Msogou(key, timeout, Sig_verify):
    '''
    m搜狗搜索
    :param key:关键词
    :return: 结果集合
    '''
    try:
        url = 'https://m.sogou.com/web/searchList.jsp?keyword={}'.format(key)
        sess = requests.session()
        response = sess.get(url, headers=Mheaders, timeout=timeout,allow_redirects=False)
        status_code1 = response.status_code
        try:
            div = re.search('相关搜索</span></h3>(.*?)</div>', response.text, re.S | re.I)[1]
            rs = re.findall('<a.*?>(.*?)</a>', div, re.DOTALL)
        except Exception as e:
            rs = []
        url = 'https://m.sogou.com/web/sugg/{}?vr=1&s=1&source=wapsearch'.format(key)
        response = sess.get(url, headers=Mheaders, timeout=timeout,allow_redirects=False)
        status_code2 = response.status_code
        try:
            sugrec = [li['q'] for li in response.json()['s']]
        except Exception as e:
            sugrec = []
        return rs, sugrec, status_code1 + status_code2
    except Exception as e:
        raise e


@verify
def Msm(key, timeout, Sig_verify):
    '''
    m神马搜索
    :param key:关键词
    :return: 结果集合
    '''
    try:
        url = 'https://m.sm.cn/s?q={}&from=smor&safe=1&snum=6'.format(key)
        sess = requests.session()
        response = sess.get(url, headers=Mheaders, timeout=timeout,allow_redirects=False)
        status_code1 = response.status_code
        html = etree.HTML(response.text)
        rs = html.xpath('//h2[contains(text(), "相关搜索")]/..//span/text()')
        url = 'https://sugs.m.sm.cn/web?t=w&uc_param_str=dnnwnt&scheme=https&fr=android&q={}&&callback=jsonp2'.format(
            key)
        response = sess.get(url, headers=Mheaders, timeout=timeout,allow_redirects=False)
        status_code2 = response.status_code
        try:
            down = re.search('jsonp2\((.*)\);', response.text, re.S | re.I)[1]
            sugrec = [li['w'] for li in eval(down)['r']]
        except Exception as e:
            sugrec = []
        return rs, sugrec, status_code1 + status_code2
    except Exception as e:
        raise e


spiderFunc = {
    'pcbaidu': PCbaidu,
    'pcsogou': PCsogou,
    'mbaidu': Mbaidu,
    'msogou': Msogou,
    'mshenma': Msm
}
