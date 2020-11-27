# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Essam Ali\Desktop\Bookstore\Login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        
        LoginWindow.setObjectName("LoginWindow")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resources/library.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        LoginWindow.setWindowIcon(icon)
        LoginWindow.resize(617, 442)
        LoginWindow.setMinimumSize(QtCore.QSize(617, 442))
        LoginWindow.setMaximumSize(QtCore.QSize(617, 442))
        LoginWindow.setAutoFillBackground(False)
        LoginWindow.setStyleSheet("QWidget#centralwidget{\n"
"background-image: url(:/resources/background.jpg);\n"
"}")
        LoginWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(40, 20, 551, 391))
        self.widget.setStyleSheet("QWidget#widget{\n"
"background-color: rgba(255, 255, 255,100);\n"
"\n"
"background-image: url();\n"
"}")
        self.widget.setObjectName("widget")
        self.LoginButton = QtWidgets.QPushButton(self.widget)
        self.LoginButton.setGeometry(QtCore.QRect(170, 310, 201, 51))
        self.LoginButton.setStyleSheet("")
        self.LoginButton.setAutoDefault(False)
        self.LoginButton.setDefault(False)
        self.LoginButton.setObjectName("LoginButton")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(40, 180, 111, 31))
        self.label_2.setStyleSheet("font: 16pt \"Times New Roman\";\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(40, 250, 111, 31))
        self.label_3.setStyleSheet("font: 16pt \"Times New Roman\";\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_3.setObjectName("label_3")
        self.usrNameField = QtWidgets.QLineEdit(self.widget)
        self.usrNameField.setGeometry(QtCore.QRect(190, 170, 281, 51))
        self.usrNameField.setAutoFillBackground(False)
        self.usrNameField.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.usrNameField.setText("")
        self.usrNameField.setFrame(True)
        self.usrNameField.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.usrNameField.setObjectName("usrNameField")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 20, 551, 131))
        self.label.setStyleSheet("image: url(:/resources/person.png);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.passwordField = QtWidgets.QLineEdit(self.widget)
        self.passwordField.setGeometry(QtCore.QRect(190, 240, 281, 51))
        self.passwordField.setAutoFillBackground(False)
        self.passwordField.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.passwordField.setInputMask("")
        self.passwordField.setText("")
        self.passwordField.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordField.setObjectName("passwordField")
        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Login"))
        self.LoginButton.setText(_translate("LoginWindow", "Login"))
        self.label_2.setText(_translate("LoginWindow", "Username"))
        self.label_3.setText(_translate("LoginWindow", "Password"))
        self.usrNameField.setPlaceholderText(_translate("LoginWindow", "username"))
        self.passwordField.setPlaceholderText(_translate("LoginWindow", "password"))
import Resources_rc

