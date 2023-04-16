# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Projects\quicks\dev\design\quick_interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Quicks(object):
    def setupUi(self, Quicks):
        Quicks.setObjectName("Quicks")
        Quicks.resize(380, 200)
        Quicks.setMaximumSize(QtCore.QSize(440, 240))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("d:\\Projects\\quicks\\dev\\design\\icons/icon36.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Quicks.setWindowIcon(icon)
        Quicks.setIconSize(QtCore.QSize(36, 36))
        Quicks.setDocumentMode(False)
        self.background = QtWidgets.QWidget(Quicks)
        self.background.setMaximumSize(QtCore.QSize(440, 240))
        self.background.setStyleSheet("background-color: #283043;")
        self.background.setObjectName("background")
        self.linedit_enter_api = QtWidgets.QLineEdit(self.background)
        self.linedit_enter_api.setGeometry(QtCore.QRect(150, 30, 180, 23))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.linedit_enter_api.setFont(font)
        self.linedit_enter_api.setStyleSheet("QLineEdit {\n"
"    padding: 2px;\n"
"    padding-left: 8px;\n"
"    border: 1px solid #dedbe6;\n"
"    border-radius: 8px;\n"
"    color: #dedbe6;\n"
"}")
        self.linedit_enter_api.setText("")
        self.linedit_enter_api.setFrame(True)
        self.linedit_enter_api.setObjectName("linedit_enter_api")
        self.label_enter_api = QtWidgets.QLabel(self.background)
        self.label_enter_api.setGeometry(QtCore.QRect(30, 30, 110, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_enter_api.setFont(font)
        self.label_enter_api.setStyleSheet("QLabel {\n"
"    color: #dedbe6;\n"
"}")
        self.label_enter_api.setTextFormat(QtCore.Qt.AutoText)
        self.label_enter_api.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_enter_api.setObjectName("label_enter_api")
        self.label_max_token = QtWidgets.QLabel(self.background)
        self.label_max_token.setGeometry(QtCore.QRect(30, 80, 120, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.label_max_token.setFont(font)
        self.label_max_token.setStyleSheet("color: #dedbe6;")
        self.label_max_token.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_max_token.setObjectName("label_max_token")
        self.linedit_spinbox = QtWidgets.QSpinBox(self.background)
        self.linedit_spinbox.setGeometry(QtCore.QRect(150, 80, 80, 23))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.linedit_spinbox.setFont(font)
        self.linedit_spinbox.setStyleSheet("QSpinBox {\n"
"    padding: 3px;\n"
"    border: 1px solid #dedbe6;\n"
"    border-radius: 8px;\n"
"    color: #dedbe6;\n"
"}\n"
"\n"
"")
        self.linedit_spinbox.setWrapping(False)
        self.linedit_spinbox.setFrame(True)
        self.linedit_spinbox.setAlignment(QtCore.Qt.AlignCenter)
        self.linedit_spinbox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.linedit_spinbox.setMaximum(4000)
        self.linedit_spinbox.setProperty("value", 1000)
        self.linedit_spinbox.setObjectName("linedit_spinbox")
        self.button_submit = QtWidgets.QPushButton(self.background)
        self.button_submit.setGeometry(QtCore.QRect(130, 140, 120, 25))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.button_submit.setFont(font)
        self.button_submit.setStyleSheet("\n"
"\n"
"QPushButton {\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    background-color: #c42034;\n"
"    color: #dedbe6;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #c93648;\n"
"    color: #dedbe6;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #9c1929;\n"
"    color: #283043;\n"
"}")
        self.button_submit.setObjectName("button_submit")
        self.line = QtWidgets.QFrame(self.background)
        self.line.setGeometry(QtCore.QRect(30, 50, 100, 1))
        self.line.setStyleSheet("background-color: #c42034;\n"
"border-radius: 2px;")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.background)
        self.line_2.setGeometry(QtCore.QRect(30, 100, 100, 1))
        self.line_2.setStyleSheet("background-color: #c42034;\n"
"border-radius: 2px;")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        Quicks.setCentralWidget(self.background)

        self.retranslateUi(Quicks)
        QtCore.QMetaObject.connectSlotsByName(Quicks)

    def retranslateUi(self, Quicks):
        _translate = QtCore.QCoreApplication.translate
        Quicks.setWindowTitle(_translate("Quicks", "Quicks"))
        self.linedit_enter_api.setPlaceholderText(_translate("Quicks", "already no api"))
        self.label_enter_api.setText(_translate("Quicks", "Your API keys:"))
        self.label_max_token.setText(_translate("Quicks", "Max tokens spend:"))
        self.button_submit.setText(_translate("Quicks", "Submit"))