# This Python file uses the following encoding: utf-8
import sys, json
from pymongo import MongoClient as mongose
from notifypy import Notify as noty
from urllib.request import urlopen as curl

from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem

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
        
        self.updates()
        
    def upgrades(self, opt):
        self.nw.showNormal()
        self.showMinimized()
        self.nw.conf(opt, self.collections)

    def wback(self, event):
        self.hide()
        self.updates()
        self.show()
        event.accept()
        
    def updates(self):
        contacts = [ i for i in self.collections.find() ]
        
        self.ui.tableWidget.setColumnCount(7)
        self.ui.tableWidget.setHorizontalHeaderLabels(['Nombre', 'Apellido', 'Número', 'Correo', 'Dirección', 'Notas', 'Grupo'])
        self.ui.tableWidget.setRowCount(len(contacts))
        for i in range(len(contacts)):
            self.ui.tableWidget.setItem(i, 0, QTableWidgetItem(contacts[i]['name']))
            self.ui.tableWidget.setItem(i, 1, QTableWidgetItem(contacts[i]['lstn']))
            self.ui.tableWidget.setItem(i, 2, QTableWidgetItem(contacts[i]['lada'] + contacts[i]['phne']))
            self.ui.tableWidget.setItem(i, 3, QTableWidgetItem(contacts[i]['work']))
            self.ui.tableWidget.setItem(i, 4, QTableWidgetItem(contacts[i]['addr']))
            self.ui.tableWidget.setItem(i, 5, QTableWidgetItem(contacts[i]['note']))
            self.ui.tableWidget.setItem(i, 6, QTableWidgetItem(contacts[i]['grpo']))

class WEdit(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        
        self.ui = Ui_Window()
        self.ui.setupUi(self)
        self.noty = noty()
        with curl('https://gist.githubusercontent.com/oasis1992/05cd6604834e18e6979a286ed2fcd2e1/raw/303a0d5e9b356a67bfaff070ff746b65d010f4d5/ladas-internacionales.json') as i:
            data = json.load(i)
            for lada in data:
                self.ui.lada.addItem('+' + lada['lada'])
            self.ui.lada.setCurrentText('+52')
        
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
        self.ui.ids.currentIndexChanged.connect(self.uconf)
        
    def conf(self, opt, collections):
        self.collect = collections
        self.ui.ids.setEnabled(bool(opt))
        self.ui.pushButton_2.hide() if not bool(opt) else self.ui.pushButton_2.show()
        self.ui.pushButton.setText('Agregar' if not bool(opt) else 'Actualizar')
        self.ui.ids.clear()
        if opt == 1:
            try:
                alias = [i for i in self.collect.find()]
            except:
                alias = []
            for contact in alias:
                self.ui.ids.addItem(contact['name'])
        self.ui.ids.setCurrentIndex(-1)
        
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
            k = [i for i in self.collect.find({'phne': var['phne']})]
            l = [i for i in self.collect.find({'name': var['name']})]
            j = []
            if len(k) > 0:
                for i in k:
                    j.append([i for i in self.collect.find({'_id': i['_id']})][0]['name'])
                    
                self.noty.title = 'Contactos duplicados'
                self.noty.message = ', '.join(map(str, j)) + f' y {var["name"]} comparten el mismo número'
                self.noty.send()
            if len(l) == 0:
                self.collect.insert_one(var)
                self.close()
            else:
                self.noty.title = 'Usuario no valido'
                self.noty.message = f'{var["name"]} ya existe en el directorio.'
                self.noty.send()
                self.ui.name.setText('')
        else:
            l = [i for i in self.collect.find({'name': var['name']})][0]
            if (len(l) > 0 and l['_id'] == self.cid) or len(l) == 0:
                self.collect.update_one({'_id': self.cid}, {'$set': var})
                self.close()
        
    def changes(self):
        for i in range(len(self.items)):
            if len(self.items[i].text()) > 0:
                self.labels[i].show()
            else:
                self.labels[i].hide()
                
    def uconf(self):
        try:
            info = [i for i in self.collect.find({'name': self.ui.ids.currentText()})][0]
        except:
            info = {'_id': '', 'name': '', 'lstn': '', 'lada': '', 'phne': '', 'work': '', 'addr': '', 'note': '', 'grpo': ''}
        
        self.ui.name.setText(info['name'])
        self.ui.lastname.setText(info['lstn'])
        self.ui.lada.setCurrentText(info['lada'])
        self.ui.number.setText(info['phne'])
        self.ui.work.setText(info['work'])
        self.ui.address.setText(info['addr'])
        self.ui.notes.setText(info['note'])
        self.ui.group.setCurrentText(info['grpo'])
        self.cid = info['_id']

if __name__ == "__main__":
    app = QApplication(sys.argv)
    server = mongose("mongodb://localhost:27017/")
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
