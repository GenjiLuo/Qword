# -*- coding: utf-8 -*-
import sqlite3
import os
import time
from PyQt5.QtCore import QThread
from queue import Queue


class db_class(QThread):

    def __init__(self, bid=None):
        super(db_class, self).__init__()

        self.q = Queue(maxsize=0)
        self.bid = bid
        self.switch = True

    # 连接数据库
    def open(self):
        self.conn = sqlite3.connect('db.db', check_same_thread=False)
        self.conn.isolation_level = None
        self.cursor = self.conn.cursor()

    # 插入备份数据
    def insert(self, data):
        sql = '''
            INSERT OR REPLACE INTO keys (id,uid,word,count)    
            VALUES (COALESCE((select id from keys where uid = ? AND word = ?),null),
                ?,
                ?, 
                COALESCE((select count + 1 from keys where uid = ? AND word = ?),1)
                );
                '''
        self.conn.executemany(sql, data)
        self.conn.commit()
        return self.cursor.rowcount

    # 查询列表
    def select_list(self):
        try:
            sql = "select distinct uid from keys;"
            self.cursor.execute(sql)
            self.cursor.rowcount
            values = self.cursor.fetchall()
            return values
        except Exception as e:
            print(e)

    # 查询相关搜索数据表
    def select_data(self, uid):
        try:
            sql = "select word,count from keys where uid='%s';" % (uid)
            self.cursor.execute(sql)
            self.cursor.rowcount
            values = self.cursor.fetchall()
            return values
        except Exception as e:
            print(e)

    # 删除数据
    def delete(self, uid):
        try:
            sql = 'DELETE FROM keys WHERE uid = "%s";' % uid
            self.conn.execute(sql)
            self.conn.execute("VACUUM")
            self.conn.commit()
            return self.cursor.rowcount
        except Exception as e:
            print(e)

    # 删除数据
    def all_delete(self):
        try:
            sql = "DELETE FROM keys;"
            sql1 = "DELETE FROM sqlite_sequence;"
            self.conn.execute(sql)
            self.conn.execute(sql1)
            self.conn.execute("VACUUM")
            self.conn.commit()
            return self.cursor.rowcount
        except Exception as e:
            print(e)

    # 关闭连接
    def close(self):
        self.conn.close()

    # 添加待存储数据到队列
    def add_list(self, keys):
        self.q.put(keys)

    # 执行函数
    def run(self):
        try:
            while self.switch:
                time.sleep(0.1)
                if not self.q.empty():
                    self.insert(self.q.get())
        except Exception as e:
            print(e)
        finally:
            self.close()


if __name__ == '__main__':
    db = db_class()
    db.open()
    s = db.select_list()
    print(s)
    db.close()
    pass
