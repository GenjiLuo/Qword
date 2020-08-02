from UI.Ui_Dialog import Ui_Dialog
from PyQt5.QtWidgets import QDialog, QCheckBox, QListWidgetItem, QWidget, QVBoxLayout
from db_class import db_class
from PyQt5.QtCore import QSize,pyqtSignal


class dialog_wiin(QDialog, Ui_Dialog):
    Sig_back = pyqtSignal(list)

    def __init__(self, parent=None):
        super(dialog_wiin, self).__init__(parent)
        self.setupUi(self)
        self.retranslateUi(self)
        self.db = db_class()
        self.deleButton.clicked.connect(self.delete_back)
        self.deleAllButton.clicked.connect(self.delete_all)
        self.loadButton.clicked.connect(self.load_back)
        self.loadback()

    def delete_back(self):
        self.db.open()
        [self.db.delete(c.text()) for c in self.check_list if c.isChecked()]
        self.db.close()
        self.loadback()

    def delete_all(self):
        self.db.open()
        self.db.all_delete()
        self.db.close()
        self.loadback()

    def load_back(self):
        data = []
        self.db.open()
        for c in self.check_list:
            if c.isChecked():
                data += self.db.select_data(c.text())
        self.Sig_back.emit(data)
        self.close()

    def loadback(self):
        self.check_list = []
        self.listWidget.clear()
        self.db.open()
        back_list = self.db.select_list()
        for b in back_list:
            widget = QWidget()
            Layout = QVBoxLayout()
            check = QCheckBox(b[0], self)
            self.check_list.append(check)
            Layout.addWidget(check)
            widget.setLayout(Layout)
            item = QListWidgetItem()
            item.setSizeHint(QSize(80, 40))
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, widget)
        self.db.close()
