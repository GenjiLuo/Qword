# -*- coding:utf-8 -*-
import urllib3
from db_class import db_class
from spider.spider_class import spiderFunc
from PyQt5.QtCore import pyqtSignal, QThread
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import sys
sys.setrecursionlimit(1000000000)


class SearchClass(QThread):
    urllib3.disable_warnings()

    # 创建信号结果list传给主窗口
    Sig_search_result = pyqtSignal(list)
    Sig_search_end = pyqtSignal()
    Sig_verify = pyqtSignal()

    def __init__(self, id=None, keys_list=None, engine_list=None, level=None, thread=None, timeout=None):
        super(SearchClass, self).__init__()

        self.flag = 1
        self.id = id
        self.keys_list = keys_list
        self.engine_list = engine_list
        self.level = int(level)
        self.timeout = int(timeout)
        self.threadPool = ThreadPoolExecutor(max_workers=int(thread))
        self.old_set = set()
        self.db = db_class()
        self.getList()

    def getList(self):
        with open('filter.txt', 'r', encoding='utf-8') as f:
            self.filter = [li for li in f.read().split('\n') if li.strip()]
        with open('contain.txt', 'r', encoding='utf-8') as f:
            self.contain =[li for li in f.read().split('\n') if li.strip()]

    def run(self):
        try:
            self.db.open()
            self.db.start()
            for key in self.keys_list:
                if self.flag:
                    for engine in self.engine_list:
                        result = self.get_data(spiderFunc[engine], key, 0)
                        self.thread_pool(spiderFunc[engine], set(result), 1)
        except Exception as e:
            print(e)
        finally:
            self.db.switch = False
            self.Sig_search_end.emit()

    def get_data(self, func, key, count):
        try:
            result = func(key, self.timeout, self.Sig_verify)
            if self.filter:
                result = [li for li in result if all(F.upper() not in li.upper() for F in self.filter if F.strip())]
            if self.contain:
                result = [li for li in result if any(C.upper() in li.upper() for C in self.contain if C.strip())]
            self.db.q.put([[self.id, key, self.id, key, self.id, key] for key in result])
            time.sleep(0.5)
            self.Sig_search_result.emit(result)
            return set(result)
        except Exception as e:
            if count < 5:
                count += 1
                return self.get_data(func, key, count)
            return set()

    def thread_pool(self, func, key_set, count):
        try:
            result_set = set()
            if self.level > count:
                self.old_set |= key_set
                self.task_list = []
                if self.flag:
                    self.task_list = [self.threadPool.submit(self.get_data, func, key, 0) for key in key_set]
                for future in as_completed(self.task_list):
                    try:
                        result_set |= future.result()
                    except Exception as e:
                        pass
                count += 1
                result_set = result_set - self.old_set
                return self.thread_pool(func, result_set, count)
        except Exception as e:
            print(e)
