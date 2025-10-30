# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'project_config_window.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGridLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_ProjectConfigWindow(object):
    def setupUi(self, ProjectConfigWindow):
        if not ProjectConfigWindow.objectName():
            ProjectConfigWindow.setObjectName(u"ProjectConfigWindow")
        ProjectConfigWindow.resize(481, 159)
        self.verticalLayout = QVBoxLayout(ProjectConfigWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_input = QLabel(ProjectConfigWindow)
        self.label_input.setObjectName(u"label_input")

        self.gridLayout.addWidget(self.label_input, 0, 0, 1, 1)

        self.line_input = QLineEdit(ProjectConfigWindow)
        self.line_input.setObjectName(u"line_input")

        self.gridLayout.addWidget(self.line_input, 0, 1, 1, 1)

        self.btn_select_input = QPushButton(ProjectConfigWindow)
        self.btn_select_input.setObjectName(u"btn_select_input")

        self.gridLayout.addWidget(self.btn_select_input, 0, 2, 1, 1)

        self.label_input_2 = QLabel(ProjectConfigWindow)
        self.label_input_2.setObjectName(u"label_input_2")

        self.gridLayout.addWidget(self.label_input_2, 1, 0, 1, 1)

        self.line_input_2 = QLineEdit(ProjectConfigWindow)
        self.line_input_2.setObjectName(u"line_input_2")

        self.gridLayout.addWidget(self.line_input_2, 1, 1, 1, 1)

        self.btn_select_input_2 = QPushButton(ProjectConfigWindow)
        self.btn_select_input_2.setObjectName(u"btn_select_input_2")

        self.gridLayout.addWidget(self.btn_select_input_2, 1, 2, 1, 1)

        self.label_output = QLabel(ProjectConfigWindow)
        self.label_output.setObjectName(u"label_output")

        self.gridLayout.addWidget(self.label_output, 2, 0, 1, 1)

        self.line_output = QLineEdit(ProjectConfigWindow)
        self.line_output.setObjectName(u"line_output")

        self.gridLayout.addWidget(self.line_output, 2, 1, 1, 1)

        self.btn_select_output = QPushButton(ProjectConfigWindow)
        self.btn_select_output.setObjectName(u"btn_select_output")

        self.gridLayout.addWidget(self.btn_select_output, 2, 2, 1, 1)

        self.label_seg_weight = QLabel(ProjectConfigWindow)
        self.label_seg_weight.setObjectName(u"label_seg_weight")

        self.gridLayout.addWidget(self.label_seg_weight, 3, 0, 1, 1)

        self.line_seg_weight = QLineEdit(ProjectConfigWindow)
        self.line_seg_weight.setObjectName(u"line_seg_weight")

        self.gridLayout.addWidget(self.line_seg_weight, 3, 1, 1, 1)

        self.btn_select_seg_weight = QPushButton(ProjectConfigWindow)
        self.btn_select_seg_weight.setObjectName(u"btn_select_seg_weight")

        self.gridLayout.addWidget(self.btn_select_seg_weight, 3, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.buttonBox = QDialogButtonBox(ProjectConfigWindow)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(ProjectConfigWindow)
        self.buttonBox.accepted.connect(ProjectConfigWindow.accept)
        self.buttonBox.rejected.connect(ProjectConfigWindow.reject)

        QMetaObject.connectSlotsByName(ProjectConfigWindow)
    # setupUi

    def retranslateUi(self, ProjectConfigWindow):
        ProjectConfigWindow.setWindowTitle(QCoreApplication.translate("ProjectConfigWindow", u"Dialog", None))
        self.label_input.setText(QCoreApplication.translate("ProjectConfigWindow", u"\u8f93\u5165\u6587\u4ef6\u5939:", None))
        self.line_input.setText("")
        self.btn_select_input.setText(QCoreApplication.translate("ProjectConfigWindow", u"\u9009\u62e9...", None))
        self.label_input_2.setText(QCoreApplication.translate("ProjectConfigWindow", u"\u8f85\u52a9\u8f93\u5165\u6587\u4ef6\u5939:", None))
        self.line_input_2.setText("")
        self.btn_select_input_2.setText(QCoreApplication.translate("ProjectConfigWindow", u"\u9009\u62e9...", None))
        self.label_output.setText(QCoreApplication.translate("ProjectConfigWindow", u"\u8f93\u51fa\u6587\u4ef6\u5939:", None))
        self.line_output.setText("")
        self.btn_select_output.setText(QCoreApplication.translate("ProjectConfigWindow", u"\u9009\u62e9...", None))
        self.label_seg_weight.setText(QCoreApplication.translate("ProjectConfigWindow", u"\u5206\u5272\u6743\u91cd:", None))
        self.line_seg_weight.setText("")
        self.btn_select_seg_weight.setText(QCoreApplication.translate("ProjectConfigWindow", u"\u9009\u62e9...", None))
    # retranslateUi

