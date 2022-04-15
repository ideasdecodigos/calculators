# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'properties.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpinBox, QWidget)

class Ui_Properties(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(231, 199)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 20, 211, 131))
        self.frame.setStyleSheet(u"background:#ddd")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.spinBoxDecimal = QSpinBox(self.frame)
        self.spinBoxDecimal.setObjectName(u"spinBoxDecimal")
        self.spinBoxDecimal.setMaximum(20)
        self.spinBoxDecimal.setValue(4)

        self.gridLayout.addWidget(self.spinBoxDecimal, 0, 1, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.comboBoxBgColor = QComboBox(self.frame)
        self.comboBoxBgColor.addItem("")
        self.comboBoxBgColor.addItem("")
        self.comboBoxBgColor.addItem("")
        self.comboBoxBgColor.addItem("")
        self.comboBoxBgColor.addItem("")
        self.comboBoxBgColor.addItem("")
        self.comboBoxBgColor.addItem("")
        self.comboBoxBgColor.addItem("")
        self.comboBoxBgColor.addItem("")
        self.comboBoxBgColor.addItem("")
        self.comboBoxBgColor.addItem("")
        self.comboBoxBgColor.addItem("")
        self.comboBoxBgColor.addItem("")
        self.comboBoxBgColor.addItem("")
        self.comboBoxBgColor.setObjectName(u"comboBoxBgColor")

        self.gridLayout.addWidget(self.comboBoxBgColor, 1, 1, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setTextFormat(Qt.AutoText)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.comboBoxFtColor = QComboBox(self.frame)
        self.comboBoxFtColor.addItem("")
        self.comboBoxFtColor.addItem("")
        self.comboBoxFtColor.addItem("")
        self.comboBoxFtColor.addItem("")
        self.comboBoxFtColor.addItem("")
        self.comboBoxFtColor.addItem("")
        self.comboBoxFtColor.addItem("")
        self.comboBoxFtColor.addItem("")
        self.comboBoxFtColor.addItem("")
        self.comboBoxFtColor.addItem("")
        self.comboBoxFtColor.addItem("")
        self.comboBoxFtColor.addItem("")
        self.comboBoxFtColor.addItem("")
        self.comboBoxFtColor.addItem("")
        self.comboBoxFtColor.setObjectName(u"comboBoxFtColor")

        self.gridLayout.addWidget(self.comboBoxFtColor, 2, 1, 1, 1)

        self.pushButtonSave = QPushButton(self.centralwidget)
        self.pushButtonSave.setObjectName(u"pushButtonSave")
        self.pushButtonSave.setGeometry(QRect(160, 160, 61, 31))
        self.pushButtonReset = QPushButton(self.centralwidget)
        self.pushButtonReset.setObjectName(u"pushButtonReset")
        self.pushButtonReset.setGeometry(QRect(90, 160, 61, 31))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.comboBoxBgColor.setCurrentIndex(0)
        self.comboBoxFtColor.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Decimal Length:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Background-color:", None))
        self.comboBoxBgColor.setItemText(0, QCoreApplication.translate("MainWindow", u"red", None))
        self.comboBoxBgColor.setItemText(1, QCoreApplication.translate("MainWindow", u"white", None))
        self.comboBoxBgColor.setItemText(2, QCoreApplication.translate("MainWindow", u"black", None))
        self.comboBoxBgColor.setItemText(3, QCoreApplication.translate("MainWindow", u"blue", None))
        self.comboBoxBgColor.setItemText(4, QCoreApplication.translate("MainWindow", u"green", None))
        self.comboBoxBgColor.setItemText(5, QCoreApplication.translate("MainWindow", u"yellow", None))
        self.comboBoxBgColor.setItemText(6, QCoreApplication.translate("MainWindow", u"orange", None))
        self.comboBoxBgColor.setItemText(7, QCoreApplication.translate("MainWindow", u"gray", None))
        self.comboBoxBgColor.setItemText(8, QCoreApplication.translate("MainWindow", u"pink", None))
        self.comboBoxBgColor.setItemText(9, QCoreApplication.translate("MainWindow", u"purple", None))
        self.comboBoxBgColor.setItemText(10, QCoreApplication.translate("MainWindow", u"lime", None))
        self.comboBoxBgColor.setItemText(11, QCoreApplication.translate("MainWindow", u"dodgerblue", None))
        self.comboBoxBgColor.setItemText(12, QCoreApplication.translate("MainWindow", u"limegreen", None))
        self.comboBoxBgColor.setItemText(13, QCoreApplication.translate("MainWindow", u"darkred", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Font-color:", None))
        self.comboBoxFtColor.setItemText(0, QCoreApplication.translate("MainWindow", u"red", None))
        self.comboBoxFtColor.setItemText(1, QCoreApplication.translate("MainWindow", u"white", None))
        self.comboBoxFtColor.setItemText(2, QCoreApplication.translate("MainWindow", u"black", None))
        self.comboBoxFtColor.setItemText(3, QCoreApplication.translate("MainWindow", u"blue", None))
        self.comboBoxFtColor.setItemText(4, QCoreApplication.translate("MainWindow", u"green", None))
        self.comboBoxFtColor.setItemText(5, QCoreApplication.translate("MainWindow", u"yellow", None))
        self.comboBoxFtColor.setItemText(6, QCoreApplication.translate("MainWindow", u"orange", None))
        self.comboBoxFtColor.setItemText(7, QCoreApplication.translate("MainWindow", u"gray", None))
        self.comboBoxFtColor.setItemText(8, QCoreApplication.translate("MainWindow", u"pink", None))
        self.comboBoxFtColor.setItemText(9, QCoreApplication.translate("MainWindow", u"purple", None))
        self.comboBoxFtColor.setItemText(10, QCoreApplication.translate("MainWindow", u"lime", None))
        self.comboBoxFtColor.setItemText(11, QCoreApplication.translate("MainWindow", u"dodgerblue", None))
        self.comboBoxFtColor.setItemText(12, QCoreApplication.translate("MainWindow", u"limegreen", None))
        self.comboBoxFtColor.setItemText(13, QCoreApplication.translate("MainWindow", u"darkred", None))

        self.pushButtonSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.pushButtonReset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
    # retranslateUi

