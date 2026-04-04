# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'popup_editor.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPlainTextEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_PopupEditer(object):
    def setupUi(self, PopupEditer):
        if not PopupEditer.objectName():
            PopupEditer.setObjectName(u"PopupEditer")
        PopupEditer.resize(800, 500)
        self.verticalLayout = QVBoxLayout(PopupEditer)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.titleLabel = QLabel(PopupEditer)
        self.titleLabel.setObjectName(u"titleLabel")

        self.verticalLayout.addWidget(self.titleLabel)

        self.editorBox = QPlainTextEdit(PopupEditer)
        self.editorBox.setObjectName(u"editorBox")

        self.verticalLayout.addWidget(self.editorBox)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.ContinueButton = QPushButton(PopupEditer)
        self.ContinueButton.setObjectName(u"ContinueButton")

        self.buttonLayout.addWidget(self.ContinueButton)


        self.verticalLayout.addLayout(self.buttonLayout)


        self.retranslateUi(PopupEditer)

        QMetaObject.connectSlotsByName(PopupEditer)
    # setupUi

    def retranslateUi(self, PopupEditer):
        PopupEditer.setWindowTitle(QCoreApplication.translate("PopupEditer", u"Popup Editor", None))
        self.titleLabel.setText(QCoreApplication.translate("PopupEditer", u"Cover Letter Editer", None))
        self.ContinueButton.setText(QCoreApplication.translate("PopupEditer", u"Save", None))
    # retranslateUi

