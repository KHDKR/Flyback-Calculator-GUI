# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FlybackGUI.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1089, 568)
        Form.setSizeIncrement(QSize(2, 1))
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.Computer))
        Form.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(700, 350))
        self.label.setMaximumSize(QSize(1400, 700))
        self.label.setSizeIncrement(QSize(2, 1))
        self.label.setBaseSize(QSize(800, 400))
        self.label.setTextFormat(Qt.TextFormat.PlainText)
        self.label.setPixmap(QPixmap(u"MainCircuit.jpg"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u53cd\u6fc0\u5f0f\u5f00\u5173\u7535\u6e90\u8ba1\u7b97\u5668", None))
        self.label.setText("")
    # retranslateUi

