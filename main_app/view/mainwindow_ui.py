# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(820, 520)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_input = QLabel(self.centralwidget)
        self.label_input.setObjectName(u"label_input")

        self.gridLayout.addWidget(self.label_input, 0, 0, 1, 1)

        self.line_input = QLineEdit(self.centralwidget)
        self.line_input.setObjectName(u"line_input")

        self.gridLayout.addWidget(self.line_input, 0, 1, 1, 1)

        self.btn_select_input = QPushButton(self.centralwidget)
        self.btn_select_input.setObjectName(u"btn_select_input")

        self.gridLayout.addWidget(self.btn_select_input, 0, 2, 1, 1)

        self.label_output = QLabel(self.centralwidget)
        self.label_output.setObjectName(u"label_output")

        self.gridLayout.addWidget(self.label_output, 1, 0, 1, 1)

        self.line_output = QLineEdit(self.centralwidget)
        self.line_output.setObjectName(u"line_output")

        self.gridLayout.addWidget(self.line_output, 1, 1, 1, 1)

        self.btn_select_output = QPushButton(self.centralwidget)
        self.btn_select_output.setObjectName(u"btn_select_output")

        self.gridLayout.addWidget(self.btn_select_output, 1, 2, 1, 1)

        self.label_weight = QLabel(self.centralwidget)
        self.label_weight.setObjectName(u"label_weight")

        self.gridLayout.addWidget(self.label_weight, 2, 0, 1, 1)

        self.line_weight = QLineEdit(self.centralwidget)
        self.line_weight.setObjectName(u"line_weight")

        self.gridLayout.addWidget(self.line_weight, 2, 1, 1, 1)

        self.btn_select_weight = QPushButton(self.centralwidget)
        self.btn_select_weight.setObjectName(u"btn_select_weight")

        self.gridLayout.addWidget(self.btn_select_weight, 2, 2, 1, 1)

        self.label_model = QLabel(self.centralwidget)
        self.label_model.setObjectName(u"label_model")

        self.gridLayout.addWidget(self.label_model, 3, 0, 1, 1)

        self.combo_model = QComboBox(self.centralwidget)
        self.combo_model.addItem("")
        self.combo_model.addItem("")
        self.combo_model.addItem("")
        self.combo_model.setObjectName(u"combo_model")

        self.gridLayout.addWidget(self.combo_model, 3, 1, 1, 1)

        self.btn_run = QPushButton(self.centralwidget)
        self.btn_run.setObjectName(u"btn_run")

        self.gridLayout.addWidget(self.btn_run, 3, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.hLayout = QHBoxLayout()
        self.hLayout.setObjectName(u"hLayout")
        self.label_loading = QLabel(self.centralwidget)
        self.label_loading.setObjectName(u"label_loading")

        self.hLayout.addWidget(self.label_loading)


        self.verticalLayout.addLayout(self.hLayout)

        self.text_log = QTextEdit(self.centralwidget)
        self.text_log.setObjectName(u"text_log")

        self.verticalLayout.addWidget(self.text_log)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 820, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Multi-Model Inference GUI", None))
        self.label_input.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u6587\u4ef6\u5939:", None))
        self.line_input.setText(QCoreApplication.translate("MainWindow", u"C:\\Users\\yanxu\\Desktop\\test\\inputs", None))
        self.btn_select_input.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9...", None))
        self.label_output.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u6587\u4ef6\u5939:", None))
        self.line_output.setText(QCoreApplication.translate("MainWindow", u"C:\\Users\\yanxu\\Desktop\\test\\outputs", None))
        self.btn_select_output.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9...", None))
        self.label_weight.setText(QCoreApplication.translate("MainWindow", u"\u6743\u91cd\u76ee\u5f55:", None))
        self.line_weight.setText(QCoreApplication.translate("MainWindow", u"C:\\Users\\yanxu\\Desktop\\test\\weights", None))
        self.btn_select_weight.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9...", None))
        self.label_model.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6a21\u578b:", None))
        self.combo_model.setItemText(0, QCoreApplication.translate("MainWindow", u"seg", None))
        self.combo_model.setItemText(1, QCoreApplication.translate("MainWindow", u"rgb2ir", None))
        self.combo_model.setItemText(2, QCoreApplication.translate("MainWindow", u"rgb2sar", None))

        self.btn_run.setText(QCoreApplication.translate("MainWindow", u"\u8fd0\u884c\u6a21\u578b", None))
        self.label_loading.setText("")
    # retranslateUi

