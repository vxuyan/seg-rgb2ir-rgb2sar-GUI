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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTreeView, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1062, 740)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_config = QPushButton(self.centralwidget)
        self.btn_config.setObjectName(u"btn_config")

        self.horizontalLayout.addWidget(self.btn_config)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout.addWidget(self.pushButton_5)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_browser = QHBoxLayout()
        self.horizontalLayout_browser.setObjectName(u"horizontalLayout_browser")
        self.tree_file_browser = QTreeView(self.centralwidget)
        self.tree_file_browser.setObjectName(u"tree_file_browser")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tree_file_browser.sizePolicy().hasHeightForWidth())
        self.tree_file_browser.setSizePolicy(sizePolicy)
        self.tree_file_browser.setMinimumSize(QSize(220, 0))
        self.tree_file_browser.setHeaderHidden(True)

        self.horizontalLayout_browser.addWidget(self.tree_file_browser)

        self.verticalLayout_content = QVBoxLayout()
        self.verticalLayout_content.setObjectName(u"verticalLayout_content")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        self.label_input = QLabel(self.centralwidget)
        self.label_input.setObjectName(u"label_input")
        sizePolicy1.setHeightForWidth(self.label_input.sizePolicy().hasHeightForWidth())
        self.label_input.setSizePolicy(sizePolicy1)
        self.label_input.setMinimumSize(QSize(256, 256))
        self.label_input.setFrameShape(QFrame.Box)
        self.label_input.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_input)

        self.label_output = QLabel(self.centralwidget)
        self.label_output.setObjectName(u"label_output")
        sizePolicy1.setHeightForWidth(self.label_output.sizePolicy().hasHeightForWidth())
        self.label_output.setSizePolicy(sizePolicy1)
        self.label_output.setMinimumSize(QSize(256, 256))
        self.label_output.setFrameShape(QFrame.Box)
        self.label_output.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_output)


        self.verticalLayout_content.addLayout(self.horizontalLayout_2)

        self.hLayout = QHBoxLayout()
        self.hLayout.setObjectName(u"hLayout")
        self.label_loading = QLabel(self.centralwidget)
        self.label_loading.setObjectName(u"label_loading")

        self.hLayout.addWidget(self.label_loading)


        self.verticalLayout_content.addLayout(self.hLayout)

        self.text_log = QTextEdit(self.centralwidget)
        self.text_log.setObjectName(u"text_log")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.text_log.sizePolicy().hasHeightForWidth())
        self.text_log.setSizePolicy(sizePolicy2)

        self.verticalLayout_content.addWidget(self.text_log)


        self.horizontalLayout_browser.addLayout(self.verticalLayout_content)


        self.verticalLayout.addLayout(self.horizontalLayout_browser)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1062, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u5206\u5272\u4ee5\u53ca\u573a\u666f\u8fc1\u79fb\u5de5\u5177", None))
        self.btn_config.setText(QCoreApplication.translate("MainWindow", u"\u5de5\u7a0b\u914d\u7f6e", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u5206\u5272", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"rgb2ir", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"rgb2sar", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u62df", None))
        self.label_input.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u56fe\u50cf", None))
        self.label_output.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u7ed3\u679c", None))
        self.label_loading.setText("")
    # retranslateUi

