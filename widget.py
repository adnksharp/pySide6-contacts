# This Python file uses the following encoding: utf-8
import sys
from pymongo import MongoClient as mongose

from PySide6.QtWidgets import QApplication, QWidget, QMainWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget
from eform_ui import Ui_Widget as Ui_Window

server = None

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.nw = WEdit()
        self.nw.closeEvent = self.wback
        self.db = server['myContacts']
        
        self.ui.pushButton.clicked.connect(lambda x: self.upgrades(1))
        self.ui.pushButton_2.clicked.connect(lambda x: self.upgrades(0))
        
    def upgrades(self, opt):
        self.nw.showNormal()
        self.showMinimized()
        self.nw.conf(opt)

    def wback(self, event):
        self.hide()
        self.show()
        event.accept()                

class WEdit(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        
        self.ui = Ui_Window()
        self.ui.setupUi(self)
        
        self.items = [
            self.ui.name,
            self.ui.lastname,
            self.ui.work,
            self.ui.address,
            self.ui.notes
        ]
        self.labels = [
            self.ui.label,
            self.ui.label_2,
            self.ui.label_3,
            self.ui.label_4,
            self.ui.label_5
        ]
        
        for i in self.items:
            i.textChanged.connect(self.changes)
        for label in self.labels:
            label.hide()
        
    def conf(self, opt):
        print(opt)
        
    def changes(self):
        for i in range(len(self.items)):
            if len(self.items[i].text()) > 0:
                self.labels[i].show()
            else:
                self.labels[i].hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    server = mongose("mongodb://localhost:27017/")
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
