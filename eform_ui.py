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
    QLabel, QLineEdit, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(416, 457)
        self.verticalLayout = QVBoxLayout(Widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.comboBox_3 = QComboBox(Widget)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.verticalLayout.addWidget(self.comboBox_3)

        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(Widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout.addWidget(self.lineEdit)

        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(Widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout.addWidget(self.lineEdit_2)

        self.label_3 = QLabel(Widget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.lineEdit_3 = QLineEdit(Widget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.verticalLayout.addWidget(self.lineEdit_3)

        self.groupBox = QGroupBox(Widget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout.addWidget(self.comboBox)

        self.lineEdit_4 = QLineEdit(self.groupBox)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.horizontalLayout.addWidget(self.lineEdit_4)


        self.verticalLayout.addWidget(self.groupBox)

        self.label_4 = QLabel(Widget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.lineEdit_5 = QLineEdit(Widget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.verticalLayout.addWidget(self.lineEdit_5)

        self.label_5 = QLabel(Widget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.lineEdit_6 = QLineEdit(Widget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.verticalLayout.addWidget(self.lineEdit_6)

        self.label_6 = QLabel(Widget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.comboBox_2 = QComboBox(Widget)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.verticalLayout.addWidget(self.comboBox_2)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Editar contactos", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Nombre", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Widget", u"Nombre", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Apellido", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Widget", u"Apellido", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Empresa", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("Widget", u"Empresa", None))
        self.groupBox.setTitle(QCoreApplication.translate("Widget", u"Telefono", None))
        self.comboBox.setPlaceholderText(QCoreApplication.translate("Widget", u"Lada", None))
        self.lineEdit_4.setPlaceholderText("")
        self.label_4.setText(QCoreApplication.translate("Widget", u"Direcci\u00f3n", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("Widget", u"Direcci\u00f3n", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"Nota", None))
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("Widget", u"Nota", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"Grupo", None))
        self.comboBox_2.setPlaceholderText(QCoreApplication.translate("Widget", u"Grupo", None))
    # retranslateUi

