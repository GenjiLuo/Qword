import csv
import os
import sys
import time
import datetime
import requests
import configparser
from UI.ui_win import Ui_Form
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QFileDialog, QMessageBox
from spider.search_class import SearchClass
from dialog_win import dialog_wiin
from filter_win import FilterWindow
from contain_win import ContainWindow
from db_class import db_class
from rsa_class import rsa_class

class MainWindow(QMainWindow, Ui_Form):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)
        self.setFixedSize(self.width(), self.height())
        self.tableWidget.setColumnWidth(0, 400)

        self.getIP()
        self.read_config()

        self.pushButton_save.clicked.connect(self.save_config)
        self.pushButton_run.clicked.connect(self.run)
        self.pushButton_stop.clicked.connect(self.stop)
        self.pushButton_bp.clicked.connect(self.open_sub)
        self.pushButton_out.clicked.connect(self.outExcel)
        self.pushButton_contain.clicked.connect(self.open_contain)
        self.pushButton_filter.clicked.connect(self.open_filter)

        self.time_cont = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.run_time)

        self.verify_flag = 1  # 验证标识 1为可以拨号
        self.wordDict = {}    # 结果集
        self.wordCount = 0

        self.rsa = rsa_class()
        self.rsa.Sig_auth.connect(self.close)
        self.rsa.start()

    def close(self):
        QMessageBox.warning(self, '错误', '已过期')
        sys.exit(0)

    def outExcel(self):
        try:
            rowCount = self.tableWidget.rowCount()
            columnCount = self.tableWidget.columnCount()
            fileName, ok = QFileDialog.getSaveFileName(None, "文件保存", "./", "CSV (*.csv)")
            datas = []
            headers = ['关键词', '词频']
            for i in range(rowCount):
                item = []
                try:
                    for j in range(columnCount):
                        item.append(self.tableWidget.item(i, j).text())
                    datas.append(tuple(item))
                except Exception as e:
                    print(e)
            with open(fileName, 'w', encoding='utf8', newline='')as f:
                f_csv = csv.writer(f)
                f_csv.writerow(headers)
                f_csv.writerows(datas)
        except Exception as e:
            print(e)

    def button_status(self, status):
        '''
        控件启用或禁用
        :param status:
        :return:
        '''
        try:
            self.textEdit.setDisabled(status)
            self.checkBox_PCbaidu.setDisabled(status)
            self.checkBox_PCsogou.setDisabled(status)
            self.checkBox_Mbaidu.setDisabled(status)
            self.checkBox_Msogou.setDisabled(status)
            self.checkBox_Mshenma.setDisabled(status)
            self.spinBox_level.setDisabled(status)
            self.spinBox_thread.setDisabled(status)
            self.spinBox_time.setDisabled(status)
            self.pushButton_run.setDisabled(status)
            if status:
                self.time_cont = 0
                self.wordDict = {}
                self.wordCount = 0
                self.timer.start(1000)
                self.label_status.setText('运行中...')
                self.label_status.setStyleSheet('color: rgb(0, 217, 0);')
                self.label_result.setText('0')
            else:
                self.timer.stop()
                self.label_status.setText('结束')
                self.label_status.setStyleSheet('color: red;')
        except Exception as e:
            print(e)

    def run_time(self):
        '''
        计时器
        :return:
        '''
        self.time_cont += 1
        ts = datetime.timedelta(seconds=self.time_cont)
        self.label_rnutime.setText(str(ts))

    def run(self):
        '''
        开始按钮
        :return:
        '''
        try:
            text = self.textEdit.toPlainText()
            if text.strip():
                self.id = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                key_list = text.split('\n')
                engine_list = []
                if self.checkBox_PCbaidu.isChecked():
                    engine_list.append('pcbaidu')
                if self.checkBox_PCsogou.isChecked():
                    engine_list.append('pcsogou')
                if self.checkBox_Mbaidu.isChecked():
                    engine_list.append('mbaidu')
                if self.checkBox_Msogou.isChecked():
                    engine_list.append('msogou')
                if self.checkBox_Mshenma.isChecked():
                    engine_list.append('mshenma')
                level = self.spinBox_level.text()
                thread = self.spinBox_thread.text()
                timeout = self.spinBox_time.text()

                self.button_status(True)
                self.db = db_class()
                self.db.open()
                self.db.start()
                self.searchOBJ = SearchClass(key_list, engine_list, level, thread,timeout)
                self.searchOBJ.Sig_search_result.connect(self.receive)
                self.searchOBJ.Sig_verify.connect(self.verify)
                self.searchOBJ.Sig_search_end.connect(self.end)
                self.searchOBJ.start()
        except Exception as e:
            print(e)

    def end(self):
        self.button_status(False)
        self.db.switch = False

    def receive(self, items):
        '''
        接收数据
        :param items:
        :return:
        '''
        try:
            self.db.q.put([[self.id, key, self.id, key, self.id, key] for key in items])
            self.wordCount += len(items)
            self.label_result.setText(str(self.wordCount))
            for i in items:
                self.wordDict[i] = self.wordDict.get(i, 0) + 1
            result = sorted(self.wordDict.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
            self.write_table(result)
        except Exception as e:
            print(e)

    def write_table(self, items):
        '''
        数据写入表格
        :param items:
        :return:
        '''
        try:
            self.tableWidget.setRowCount(0)
            for n, li in enumerate(items[:5000]):
                self.tableWidget.setRowCount(n + 1)
                self.tableWidget.setItem(n, 0, QTableWidgetItem(str(li[0])))
                self.tableWidget.setItem(n, 1, QTableWidgetItem(str(li[1])))
        except Exception as e:
            print(e)

    def verify(self):
        '''
        验证时，重新拨号
        :return:
        '''
        try:
            pass
            # if self.verify_flag:
            #     self.verify_flag = 0
            #     task = Thread(target=self.connect)
            #     task.start()
        except Exception as e:
            print(e)

    def connect(self):
        '''
        重新拨号
        :return:
        '''
        try:
            name = self.lineEdit_adsl.text()
            username = self.lineEdit_user.text()
            password = self.lineEdit_pwd.text()
            cmdstr = "rasdial %s /disconnect" % name
            os.system(cmdstr)
            time.sleep(1)
            cmd_str = "rasdial %s %s %s" % (name, username, password)
            res = os.system(cmd_str)
            if res == 0:
                self.getIP()
                time.sleep(15)
                self.verify_flag = 1
                return True
            else:
                time.sleep(2)
                self.connect()
        except Exception as e:
            print(e)

    def stop(self):
        '''
        停止按钮
        :return:
        '''
        try:
            if hasattr(self, 'searchOBJ'):
                self.searchOBJ.flag = 0
                self.label_status.setText('关闭中...')
                self.label_status.setStyleSheet('color: #ff55ff;')
        except Exception as e:
            print(e)

    def open_sub(self):
        self.d_win = dialog_wiin()
        self.d_win.show()
        self.d_win.Sig_back.connect(self.load_back)

    def open_contain(self):
        self.ContainWindow = ContainWindow()
        self.ContainWindow.show()

    def open_filter(self):
        self.FilterWindow = FilterWindow()
        self.FilterWindow.show()

    def load_back(self, items):
        try:
            items = sorted(items, key=lambda x: x[1], reverse=True)
            self.write_table(items)
        except Exception as e:
            print(e)

    def getIP(self):
        '''
        得到当前ip
        :return:
        '''
        try:
            response = requests.get(
                'http://api.k780.com/?app=ip.local&appkey=10003&sign=b59bc3ef6191eb9f747dd4e83c99f2a4&format=json')
            ip = response.json()['result']['ip']
            if ip:
                self.label_ip.setText(ip)
        except Exception as e:
            print(e)

    def read_config(self):
        '''
        读取配置文件
        :return:
        '''
        cf = configparser.RawConfigParser()
        cf.read("./config.ini", encoding='utf-8-sig')

        self.lineEdit_adsl.setText(cf.get('setting', 'name'))
        self.lineEdit_user.setText(cf.get('setting', 'usr'))
        self.lineEdit_pwd.setText(cf.get('setting', 'psd'))
        self.spinBox_level.setValue(int(cf.get('setting', 'level')))
        self.spinBox_thread.setValue(int(cf.get('setting', 'thread')))
        self.spinBox_time.setValue(int(cf.get('setting', 'time')))
        self.cookie = cf.get('setting', 'cookie')

    def save_config(self):
        '''
        保存配置文件
        :return:
        '''
        cf = configparser.RawConfigParser()
        cf.read("./config.ini", encoding='utf-8-sig')
        cf.set('setting', 'name', self.lineEdit_adsl.text())
        cf.set('setting', 'usr', self.lineEdit_user.text())
        cf.set('setting', 'psd', self.lineEdit_pwd.text())
        cf.set('setting', 'level', str(self.spinBox_level.value()))
        cf.set('setting', 'thread', str(self.spinBox_thread.value()))
        cf.set('setting', 'time', str(self.spinBox_time.value()))
        cf.write(open('./config.ini', "w", encoding='utf-8-sig'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
