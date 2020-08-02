# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_contain.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(204, 340)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/ico/增.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("QDialog{background-color: rgb(230, 230, 230)}\n"
"\n"
"QPushButton{background-color: rgb(230, 230, 230)}\n"
"QPushButton{border-style:none;}\n"
"QPushButton:hover{color:lightskyblue}\n"
"QPushButton{border:1px}\n"
"QPushButton{border-radius:20px}\n"
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
"QTextEdit{\n"
"    border: 1px solid #55aaff;\n"
"    border-radius:10px;\n"
"    background-color: rgb(230, 230, 230);\n"
"}\n"
"")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(2, 2, 2, 10)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout.addWidget(self.textEdit)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(Dialog)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_OK = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_OK.setMinimumSize(QtCore.QSize(50, 0))
        self.pushButton_OK.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_OK.setObjectName("pushButton_OK")
        self.horizontalLayout_2.addWidget(self.pushButton_OK)
        self.pushButton_cancel = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_cancel.setMinimumSize(QtCore.QSize(50, 0))
        self.pushButton_cancel.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout_2.addWidget(self.pushButton_cancel)
        self.verticalLayout.addWidget(self.widget_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "添加"))
        self.pushButton_OK.setText(_translate("Dialog", "包含"))
        self.pushButton_cancel.setText(_translate("Dialog", "取消"))
import image_rc
