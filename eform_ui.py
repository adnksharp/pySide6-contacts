# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'eform.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(370, 491)
        self.verticalLayout = QVBoxLayout(Widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.ids = QComboBox(Widget)
        self.ids.setObjectName(u"ids")

        self.verticalLayout.addWidget(self.ids)

        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.label)

        self.name = QLineEdit(Widget)
        self.name.setObjectName(u"name")

        self.verticalLayout.addWidget(self.name)

        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.label_2)

        self.lastname = QLineEdit(Widget)
        self.lastname.setObjectName(u"lastname")

        self.verticalLayout.addWidget(self.lastname)

        self.groupBox = QGroupBox(Widget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lada = QComboBox(self.groupBox)
        self.lada.setObjectName(u"lada")

        self.horizontalLayout.addWidget(self.lada)

        self.number = QLineEdit(self.groupBox)
        self.number.setObjectName(u"number")

        self.horizontalLayout.addWidget(self.number)


        self.verticalLayout.addWidget(self.groupBox)

        self.label_3 = QLabel(Widget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.label_3)

        self.work = QLineEdit(Widget)
        self.work.setObjectName(u"work")

        self.verticalLayout.addWidget(self.work)

        self.label_4 = QLabel(Widget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.label_4)

        self.address = QLineEdit(Widget)
        self.address.setObjectName(u"address")

        self.verticalLayout.addWidget(self.address)

        self.label_5 = QLabel(Widget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.label_5)

        self.notes = QLineEdit(Widget)
        self.notes.setObjectName(u"notes")

        self.verticalLayout.addWidget(self.notes)

        self.label_6 = QLabel(Widget)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.label_6)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.group = QComboBox(Widget)
        self.group.addItem("")
        self.group.addItem("")
        self.group.addItem("")
        self.group.addItem("")
        self.group.addItem("")
        self.group.setObjectName(u"group")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.group.sizePolicy().hasHeightForWidth())
        self.group.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.group)

        self.lineEdit = QLineEdit(Widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_2.addWidget(self.lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton = QPushButton(Widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(Widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.pushButton_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Editar contactos", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Nombre", None))
        self.name.setPlaceholderText(QCoreApplication.translate("Widget", u"Nombre", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Apellido", None))
        self.lastname.setPlaceholderText(QCoreApplication.translate("Widget", u"Apellido", None))
        self.groupBox.setTitle(QCoreApplication.translate("Widget", u"Telefono", None))
        self.lada.setPlaceholderText(QCoreApplication.translate("Widget", u"Lada", None))
        self.number.setPlaceholderText("")
        self.label_3.setText(QCoreApplication.translate("Widget", u"Empresa", None))
        self.work.setPlaceholderText(QCoreApplication.translate("Widget", u"Empresa", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"Direcci\u00f3n", None))
        self.address.setPlaceholderText(QCoreApplication.translate("Widget", u"Direcci\u00f3n", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"Nota", None))
        self.notes.setPlaceholderText(QCoreApplication.translate("Widget", u"Nota", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"Grupo", None))
        self.group.setItemText(0, QCoreApplication.translate("Widget", u"Contactos de emergencia", None))
        self.group.setItemText(1, QCoreApplication.translate("Widget", u"Familia", None))
        self.group.setItemText(2, QCoreApplication.translate("Widget", u"Trabajo", None))
        self.group.setItemText(3, QCoreApplication.translate("Widget", u"Amigos", None))
        self.group.setItemText(4, QCoreApplication.translate("Widget", u"Nuevo grupo", None))

        self.group.setPlaceholderText(QCoreApplication.translate("Widget", u"Grupo", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"Agregar", None))
        self.pushButton_2.setText(QCoreApplication.translate("Widget", u"Eliminar", None))
    # retranslateUi

