# This Python file uses the following encoding: utf-8
import sys
from pymongo import MongoClient as mongose
from notifypy import Notify as noty

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
        self.collections = self.db['contacts']
        
        self.ui.pushButton.clicked.connect(lambda x: self.upgrades(1))
        self.ui.pushButton_2.clicked.connect(lambda x: self.upgrades(0))
        
    def upgrades(self, opt):
        self.nw.showNormal()
        self.showMinimized()
        self.nw.conf(opt, self.collections)

    def wback(self, event):
        self.hide()
        self.show()
        event.accept()                

class WEdit(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        
        self.ui = Ui_Window()
        self.ui.setupUi(self)
        self.noty = noty()
        
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
        self.ui.lineEdit.hide()
        self.ui.pushButton.clicked.connect(self.updates)
        self.ui.group.currentIndexChanged.connect(self.groupOptions)
        
    def conf(self, opt, collections):
        self.collect = collections
        self.ui.ids.setEnabled(bool(opt))
        self.ui.pushButton_2.hide() if not bool(opt) else self.ui.pushButton_2.show()
        self.ui.pushButton.setText('Agregar' if not bool(opt) else 'Actualizar')
        if opt == 1:
            try:
                alias = [ i for i in self.collect.find() ]
            except:
                alias = []
            print(alias)
        
    def updates(self):
        var = {
            'name': self.ui.name.text(),
            'lstn': self.ui.lastname.text(),
            'lada': self.ui.lada.currentText(),
            'phne': self.ui.number.text(),
            'work': self.ui.work.text(),
            'addr': self.ui.address.text(),
            'note': self.ui.notes.text(),
            'grpo': self.ui.group.currentText()
        }
        if var['lada'] == '':
            var['lada'] = '+52'
        if var['name'] == '' or not var['phne'].isnumeric() or len(var['phne']) != 10:
                return
        if not self.ui.ids.isEnabled():
            k = [i for i in self.collect.find({}, {'phne': var['phne']})]
            j = []
            if len(k) > 0:
                for i in k:
                    j.append([i for i in self.collect.find({'_id': i['_id']})][0]['name'])
                    
                self.noty.title = 'Contactos duplicados'
                self.noty.message = ', '.join(map(str, j)) + f' y {var["name"]} comparten el mismo número'
                self.noty.send()
            self.collect.insert_one(var)
            self.close()
        
    def changes(self):
        for i in range(len(self.items)):
            if len(self.items[i].text()) > 0:
                self.labels[i].show()
            else:
                self.labels[i].hide()
                
    def groupOptions(self):
        if self.ui.group.currentIndex() == self.ui.group.count() - 1:
            self.ui.lineEdit.show()
        else:
            self.ui.lineEdit.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    server = mongose("mongodb://localhost:27017/")
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
