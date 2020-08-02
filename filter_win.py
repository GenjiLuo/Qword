from PyQt5.QtCore import Qt
from UI.Ui_filter import Ui_Dialog
from PyQt5.QtWidgets import QDialog, QMessageBox


class FilterWindow(QDialog, Ui_Dialog):

    def __init__(self):
        super(FilterWindow, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

        self.setWindowFlags(
            Qt.Window | Qt.FramelessWindowHint | Qt.WindowSystemMenuHint | Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint | Qt.WindowStaysOnTopHint)  # 窗口无边框

        self.pushButton_OK.clicked.connect(self.save)
        self.pushButton_cancel.clicked.connect(self.close)

        with open('filter.txt', 'r', encoding='utf-8') as f:
            self.textEdit.setText(f.read())

    def save(self):
        text = self.textEdit.toPlainText()
        with open('filter.txt', 'w', encoding='utf-8') as f:
            f.write(text)
        self.close()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False