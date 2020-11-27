# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Essam Ali\Desktop\Bookstore\AddClient.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        
        Form.setObjectName("Form")
        Form.resize(527, 269)
        Form.setMinimumSize(QtCore.QSize(527, 269))
        Form.setMaximumSize(QtCore.QSize(527, 269))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resources/library.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.Phone = QtWidgets.QLineEdit(Form)
        self.Phone.setGeometry(QtCore.QRect(270, 100, 241, 31))
        self.Phone.setObjectName("Phone")
        
        self.label_18 = QtWidgets.QLabel(Form)
        self.label_18.setGeometry(QtCore.QRect(30, 100, 221, 31))
        self.label_18.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label_18.setObjectName("label_18")
        self.ClientName = QtWidgets.QLineEdit(Form)
        self.ClientName.setGeometry(QtCore.QRect(270, 40, 241, 31))
        self.ClientName.setObjectName("ClientName")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 40, 221, 31))
        self.label.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.AddBtn = QtWidgets.QPushButton(Form)
        self.AddBtn.setGeometry(QtCore.QRect(300, 200, 181, 41))
        self.AddBtn.setObjectName("AddBtn")
        
        self.CancelBtn = QtWidgets.QPushButton(Form)
        self.CancelBtn.setGeometry(QtCore.QRect(30, 200, 181, 41))
        self.CancelBtn.setObjectName("CancelBtn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Add client"))
        
        self.label_18.setText(_translate("Form", "phone"))
        self.label.setText(_translate("Form", "client name"))
        self.AddBtn.setText(_translate("Form", "Add client"))
        self.CancelBtn.setText(_translate("Form", "Cancel"))
