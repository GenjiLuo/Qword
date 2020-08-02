# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(247, 384)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/ico/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.loadButton = QtWidgets.QPushButton(self.frame)
        self.loadButton.setMinimumSize(QtCore.QSize(0, 20))
        self.loadButton.setMaximumSize(QtCore.QSize(16777215, 20))
        self.loadButton.setStyleSheet("QPushButton{color:black}\n"
"QPushButton:hover{color:red}\n"
"QPushButton{background-color:#BFEFFF}\n"
"QPushButton{border:2px}\n"
"QPushButton{border-radius:10px}\n"
"QPushButton{padding:2px 4px}")
        self.loadButton.setObjectName("loadButton")
        self.horizontalLayout.addWidget(self.loadButton)
        self.deleButton = QtWidgets.QPushButton(self.frame)
        self.deleButton.setMinimumSize(QtCore.QSize(0, 20))
        self.deleButton.setMaximumSize(QtCore.QSize(16777215, 20))
        self.deleButton.setStyleSheet("QPushButton{color:black}\n"
"QPushButton:hover{color:red}\n"
"QPushButton{background-color:#BFEFFF}\n"
"QPushButton{border:2px}\n"
"QPushButton{border-radius:10px}\n"
"QPushButton{padding:2px 4px}")
        self.deleButton.setObjectName("deleButton")
        self.horizontalLayout.addWidget(self.deleButton)
        self.deleAllButton = QtWidgets.QPushButton(self.frame)
        self.deleAllButton.setMinimumSize(QtCore.QSize(0, 20))
        self.deleAllButton.setMaximumSize(QtCore.QSize(16777215, 20))
        self.deleAllButton.setStyleSheet("QPushButton{color:black}\n"
"QPushButton:hover{color:red}\n"
"QPushButton{background-color:#BFEFFF}\n"
"QPushButton{border:2px}\n"
"QPushButton{border-radius:10px}\n"
"QPushButton{padding:2px 4px}")
        self.deleAllButton.setObjectName("deleAllButton")
        self.horizontalLayout.addWidget(self.deleAllButton)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "备份列表"))
        self.loadButton.setText(_translate("Dialog", "载入备份"))
        self.deleButton.setText(_translate("Dialog", "删除备份"))
        self.deleAllButton.setText(_translate("Dialog", "全部删除"))
import image_rc
