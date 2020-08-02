# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_win.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(985, 620)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/title.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("QWidget{background-color: rgb(255, 255, 255)}\n"
"QPushButton{border-style:none;}\n"
"QPushButton:hover{color:lightskyblue}\n"
"QPushButton{background-color:white}\n"
"QPushButton{border:2px}\n"
"QPushButton{border-radius:10px}\n"
"QPushButton{padding:2px 4px}\n"
"QPushButton:pressed {  \n"
"    /* 改变背景色 */\n"
"    /* background-color:rgb(180, 180, 180,120); */\n"
"    /* 改变边框风格 */  \n"
"    /* border-style:inset; */\n"
"    /* 使文字有一点移动 */  \n"
"    padding-left:2px;  \n"
"    padding-top:2px;  \n"
"}\n"
"\n"
"QCheckBox::indicator{width: 30px;height: 30px;}\n"
"QCheckBox::indicator:unchecked{image: url(:/newPrefix/多选1.png);}\n"
"QCheckBox::indicator:checked{image: url(:/newPrefix/多选.png);}\n"
"QCheckBox:hover{color:lightskyblue}\n"
"QCheckBox:pressed{\n"
"    padding-left:2px;  \n"
"    padding-top:2px;  \n"
"}\n"
"\n"
"QLineEdit{border: 1px solid #55aaff;}\n"
"QLineEdit{border-radius:5px;}\n"
"QLineEdit:focus{border: 1px solid #78ffeb;}\n"
"\n"
"QTextEdit{border: 1px solid #55aaff;}\n"
"QTextEdit{border-radius:5px;}\n"
"QTextEdit:focus{border: 1px solid #78ffeb;}\n"
"\n"
"QSpinBox{border: 1px solid #55aaff;}\n"
"QSpinBox{border-radius:5px;}\n"
"QSpinBox:focus{border: 1px solid #78ffeb;}\n"
"\n"
"QSpinBox::up-button {subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"    image: url(:/newPrefix/右.png);\n"
"    width: 20px;\n"
"    height: 20px;                \n"
"}\n"
"QSpinBox::down-button {subcontrol-origin:border;\n"
"    subcontrol-position:left;\n"
"    image: url(:/newPrefix/左.png);\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"QSpinBox::up-button:pressed{subcontrol-origin:border;\n"
"    subcontrol-position:right;\n"
"    image: url(:/newPrefix/右.png);\n"
"    width: 20px;\n"
"    height: 20px;\n"
"    padding-left:2px;  \n"
"    padding-top:2px;          \n"
"}\n"
"QSpinBox::down-button:pressed{\n"
"    subcontrol-position:left;\n"
"    image: url(:/newPrefix/左.png);\n"
"    width: 20px;\n"
"    height: 20px;\n"
"    padding-left:2px;  \n"
"    padding-top:2px;  \n"
"}\n"
"")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(9, 9, 202, 620))
        self.widget.setMinimumSize(QtCore.QSize(202, 620))
        self.widget.setMaximumSize(QtCore.QSize(182, 620))
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_3.setMinimumSize(QtCore.QSize(200, 200))
        self.groupBox_3.setMaximumSize(QtCore.QSize(200, 200))
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_3)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_2.addWidget(self.textEdit)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setMinimumSize(QtCore.QSize(200, 200))
        self.groupBox.setMaximumSize(QtCore.QSize(200, 200))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setContentsMargins(9, -1, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox_PCbaidu = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_PCbaidu.setChecked(True)
        self.checkBox_PCbaidu.setObjectName("checkBox_PCbaidu")
        self.verticalLayout.addWidget(self.checkBox_PCbaidu, 0, QtCore.Qt.AlignHCenter)
        self.checkBox_PCsogou = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_PCsogou.setObjectName("checkBox_PCsogou")
        self.verticalLayout.addWidget(self.checkBox_PCsogou, 0, QtCore.Qt.AlignHCenter)
        self.checkBox_Mbaidu = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_Mbaidu.setObjectName("checkBox_Mbaidu")
        self.verticalLayout.addWidget(self.checkBox_Mbaidu, 0, QtCore.Qt.AlignHCenter)
        self.checkBox_Msogou = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_Msogou.setObjectName("checkBox_Msogou")
        self.verticalLayout.addWidget(self.checkBox_Msogou, 0, QtCore.Qt.AlignHCenter)
        self.checkBox_Mshenma = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_Mshenma.setObjectName("checkBox_Mshenma")
        self.verticalLayout.addWidget(self.checkBox_Mshenma, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_2.setMinimumSize(QtCore.QSize(200, 150))
        self.groupBox_2.setMaximumSize(QtCore.QSize(200, 150))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.spinBox_thread = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_thread.setMinimum(1)
        self.spinBox_thread.setObjectName("spinBox_thread")
        self.gridLayout.addWidget(self.spinBox_thread, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.spinBox_time = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_time.setMinimum(1)
        self.spinBox_time.setProperty("value", 3)
        self.spinBox_time.setObjectName("spinBox_time")
        self.gridLayout.addWidget(self.spinBox_time, 3, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.spinBox_level = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_level.setMinimum(1)
        self.spinBox_level.setObjectName("spinBox_level")
        self.gridLayout.addWidget(self.spinBox_level, 1, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.widget_3 = QtWidgets.QWidget(Form)
        self.widget_3.setGeometry(QtCore.QRect(217, 9, 202, 620))
        self.widget_3.setMinimumSize(QtCore.QSize(202, 620))
        self.widget_3.setMaximumSize(QtCore.QSize(202, 620))
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_5 = QtWidgets.QGroupBox(self.widget_3)
        self.groupBox_5.setMinimumSize(QtCore.QSize(200, 250))
        self.groupBox_5.setMaximumSize(QtCore.QSize(200, 250))
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_2.setContentsMargins(10, 10, 10, 15)
        self.gridLayout_2.setHorizontalSpacing(15)
        self.gridLayout_2.setVerticalSpacing(10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_5)
        self.label_3.setMinimumSize(QtCore.QSize(0, 20))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_ip = QtWidgets.QLabel(self.groupBox_5)
        self.label_ip.setObjectName("label_ip")
        self.gridLayout_2.addWidget(self.label_ip, 0, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_5)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 1, 0, 1, 1)
        self.lineEdit_adsl = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_adsl.setObjectName("lineEdit_adsl")
        self.gridLayout_2.addWidget(self.lineEdit_adsl, 1, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox_5)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 2, 0, 1, 1)
        self.lineEdit_user = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_user.setObjectName("lineEdit_user")
        self.gridLayout_2.addWidget(self.lineEdit_user, 2, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox_5)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 3, 0, 1, 1)
        self.lineEdit_pwd = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_pwd.setObjectName("lineEdit_pwd")
        self.gridLayout_2.addWidget(self.lineEdit_pwd, 3, 1, 1, 1)
        self.pushButton_save = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_save.setEnabled(True)
        self.pushButton_save.setMinimumSize(QtCore.QSize(0, 16))
        self.pushButton_save.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/钥匙.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_save.setIcon(icon1)
        self.pushButton_save.setObjectName("pushButton_save")
        self.gridLayout_2.addWidget(self.pushButton_save, 4, 1, 1, 1)
        self.verticalLayout_4.addWidget(self.groupBox_5)
        self.groupBox_4 = QtWidgets.QGroupBox(self.widget_3)
        self.groupBox_4.setMinimumSize(QtCore.QSize(200, 150))
        self.groupBox_4.setMaximumSize(QtCore.QSize(200, 150))
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 3, 0, 1, 1)
        self.label_rnutime = QtWidgets.QLabel(self.groupBox_4)
        self.label_rnutime.setMinimumSize(QtCore.QSize(60, 0))
        self.label_rnutime.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_rnutime.setObjectName("label_rnutime")
        self.gridLayout_3.addWidget(self.label_rnutime, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_result = QtWidgets.QLabel(self.groupBox_4)
        self.label_result.setMinimumSize(QtCore.QSize(60, 0))
        self.label_result.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_result.setObjectName("label_result")
        self.gridLayout_3.addWidget(self.label_result, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_4)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_status = QtWidgets.QLabel(self.groupBox_4)
        self.label_status.setMinimumSize(QtCore.QSize(60, 0))
        self.label_status.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_status.setObjectName("label_status")
        self.gridLayout_3.addWidget(self.label_status, 0, 1, 1, 1)
        self.verticalLayout_4.addWidget(self.groupBox_4)
        self.groupBox_6 = QtWidgets.QGroupBox(self.widget_3)
        self.groupBox_6.setMinimumSize(QtCore.QSize(200, 150))
        self.groupBox_6.setMaximumSize(QtCore.QSize(200, 150))
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_5.setHorizontalSpacing(15)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.pushButton_out = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_out.setMinimumSize(QtCore.QSize(70, 0))
        self.pushButton_out.setMaximumSize(QtCore.QSize(70, 16777215))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/导出.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_out.setIcon(icon2)
        self.pushButton_out.setObjectName("pushButton_out")
        self.gridLayout_5.addWidget(self.pushButton_out, 1, 1, 1, 1)
        self.pushButton_run = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_run.setMinimumSize(QtCore.QSize(70, 0))
        self.pushButton_run.setMaximumSize(QtCore.QSize(70, 16777215))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/开始.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_run.setIcon(icon3)
        self.pushButton_run.setObjectName("pushButton_run")
        self.gridLayout_5.addWidget(self.pushButton_run, 0, 0, 1, 1)
        self.pushButton_bp = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_bp.setMinimumSize(QtCore.QSize(70, 0))
        self.pushButton_bp.setMaximumSize(QtCore.QSize(70, 16777215))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/备份.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_bp.setIcon(icon4)
        self.pushButton_bp.setObjectName("pushButton_bp")
        self.gridLayout_5.addWidget(self.pushButton_bp, 1, 0, 1, 1)
        self.pushButton_stop = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_stop.setMinimumSize(QtCore.QSize(70, 0))
        self.pushButton_stop.setMaximumSize(QtCore.QSize(70, 16777215))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/newPrefix/停止.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_stop.setIcon(icon5)
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.gridLayout_5.addWidget(self.pushButton_stop, 0, 1, 1, 1)
        self.pushButton_contain = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_contain.setMinimumSize(QtCore.QSize(70, 0))
        self.pushButton_contain.setMaximumSize(QtCore.QSize(70, 16777215))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/newPrefix/盒子.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_contain.setIcon(icon6)
        self.pushButton_contain.setObjectName("pushButton_contain")
        self.gridLayout_5.addWidget(self.pushButton_contain, 2, 0, 1, 1)
        self.pushButton_filter = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_filter.setMinimumSize(QtCore.QSize(70, 0))
        self.pushButton_filter.setMaximumSize(QtCore.QSize(70, 16777215))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/newPrefix/过滤.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_filter.setIcon(icon7)
        self.pushButton_filter.setObjectName("pushButton_filter")
        self.gridLayout_5.addWidget(self.pushButton_filter, 2, 1, 1, 1)
        self.verticalLayout_4.addWidget(self.groupBox_6)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(425, 9, 551, 602))
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 602))
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 602))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "挖掘机"))
        self.groupBox_3.setTitle(_translate("Form", "关键词列表"))
        self.groupBox.setTitle(_translate("Form", "搜索引擎"))
        self.checkBox_PCbaidu.setText(_translate("Form", " PC百度"))
        self.checkBox_PCsogou.setText(_translate("Form", " PC搜狗"))
        self.checkBox_Mbaidu.setText(_translate("Form", "  M百度"))
        self.checkBox_Msogou.setText(_translate("Form", "  M搜狗"))
        self.checkBox_Mshenma.setText(_translate("Form", "  M神马"))
        self.groupBox_2.setTitle(_translate("Form", "参数设置"))
        self.label_2.setText(_translate("Form", "超时时间"))
        self.label_7.setText(_translate("Form", "挖词级别"))
        self.label.setText(_translate("Form", "线程数量"))
        self.groupBox_5.setTitle(_translate("Form", "宽带账号"))
        self.label_3.setText(_translate("Form", "当前 I P"))
        self.label_ip.setText(_translate("Form", "0.0.0.0"))
        self.label_9.setText(_translate("Form", "ADSL名称"))
        self.lineEdit_adsl.setText(_translate("Form", "宽带连接"))
        self.label_10.setText(_translate("Form", "账    号"))
        self.lineEdit_user.setText(_translate("Form", "0000"))
        self.label_11.setText(_translate("Form", "密    码"))
        self.lineEdit_pwd.setText(_translate("Form", "1111"))
        self.pushButton_save.setText(_translate("Form", "保存账号"))
        self.groupBox_4.setTitle(_translate("Form", "状态显示"))
        self.label_5.setText(_translate("Form", "运行时间"))
        self.label_rnutime.setText(_translate("Form", "0:00:00"))
        self.label_4.setText(_translate("Form", "搜索结果"))
        self.label_result.setText(_translate("Form", "0"))
        self.label_6.setText(_translate("Form", "运行状态"))
        self.label_status.setText(_translate("Form", "待机"))
        self.groupBox_6.setTitle(_translate("Form", "功能开关"))
        self.pushButton_out.setText(_translate("Form", "导出"))
        self.pushButton_run.setText(_translate("Form", "开始"))
        self.pushButton_bp.setText(_translate("Form", "备份"))
        self.pushButton_stop.setText(_translate("Form", "停止"))
        self.pushButton_contain.setText(_translate("Form", "包含"))
        self.pushButton_filter.setText(_translate("Form", "过滤"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "关键词"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "词频"))
import image_rc
