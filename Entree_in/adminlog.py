# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminlog.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import home
import admin1
check = True

class Ui_Form(object):
        
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(650, 450)
        self.awidget = QtWidgets.QWidget(Form)
        self.awidget.setGeometry(QtCore.QRect(20, 20, 590, 420))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.awidget.setFont(font)
        self.awidget.setStyleSheet("QPushButton#alogin{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255,255,255,210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#alogin:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150,123,111,255);\n"
"}\n"
"QPushButton#alogin:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}")
        self.awidget.setObjectName("awidget")
        self.alabel = QtWidgets.QLabel(self.awidget)
        self.alabel.setGeometry(QtCore.QRect(290, 40, 260, 330))
        self.alabel.setStyleSheet("background-color:rgba(255,255,255,255);\n"
"border-bottom-right-radius:50px")
        self.alabel.setText("")
        self.alabel.setObjectName("alabel")
        self.alabel_2 = QtWidgets.QLabel(self.awidget)
        self.alabel_2.setGeometry(QtCore.QRect(40, 25, 270, 360))
        self.alabel_2.setStyleSheet("border-top-left-radius:50px;\n"
"background-color:rgba(0,0,0,80);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));")
        self.alabel_2.setText("")
        self.alabel_2.setObjectName("alabel_2")
        self.alabel_3 = QtWidgets.QLabel(self.awidget)
        self.alabel_3.setGeometry(QtCore.QRect(330, 70, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.alabel_3.setFont(font)
        self.alabel_3.setStyleSheet("color:rgba(0,0,0,200);")
        self.alabel_3.setObjectName("alabel_3")
        self.auserid = QtWidgets.QLineEdit(self.awidget)
        self.auserid.setGeometry(QtCore.QRect(330, 130, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.auserid.setFont(font)
        self.auserid.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.auserid.setObjectName("auserid")
        self.apass = QtWidgets.QLineEdit(self.awidget)
        self.apass.setGeometry(QtCore.QRect(330, 190, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.apass.setFont(font)
        self.apass.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;\n"
"")
        self.apass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.apass.setObjectName("apass")
        self.alogin = QtWidgets.QPushButton(self.awidget)
        self.alogin.setGeometry(QtCore.QRect(330, 260, 191, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.alogin.setFont(font)
        self.alogin.setObjectName("alogin")
        self.clabel_5 = QtWidgets.QLabel(self.awidget)
        self.clabel_5.setGeometry(QtCore.QRect(60, 50, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.clabel_5.setFont(font)
        self.clabel_5.setStyleSheet("color:rgba(255,255,255,220);")
        self.clabel_5.setObjectName("clabel_5")
        self.alabel_6 = QtWidgets.QLabel(self.awidget)
        self.alabel_6.setGeometry(QtCore.QRect(60, 180, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.alabel_6.setFont(font)
        self.alabel_6.setStyleSheet("color:rgba(255,255,255,220);")
        self.alabel_6.setObjectName("alabel_6")
        self.alabel_7 = QtWidgets.QLabel(self.awidget)
        self.alabel_7.setGeometry(QtCore.QRect(100, 190, 201, 191))
        font = QtGui.QFont()
        font.setFamily("Webdings")
        font.setPointSize(150)
        font.setBold(False)
        font.setWeight(50)
        self.alabel_7.setFont(font)
        self.alabel_7.setObjectName("alabel_7")
        self.clback = QtWidgets.QPushButton(self.awidget)
        self.clback.setGeometry(QtCore.QRect(460, 70, 81, 23))
        font = QtGui.QFont()
        font.setFamily("Wingdings 3")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.clback.setFont(font)
        self.clback.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255,255,255,210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150,123,111,255);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}")
        self.clback.setObjectName("clback")

        self.messageLabel = QtWidgets.QLabel(Form)
        self.messageLabel.setGeometry(QtCore.QRect(200, 400, 371, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.messageLabel.setFont(font)
        self.messageLabel.setStyleSheet("color: #6B6B6B;")
        self.messageLabel.setText("")
        self.messageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.messageLabel.setWordWrap(False)
        self.messageLabel.setObjectName("messageLabel")

        self.clback.clicked.connect(self.passage6)
        self.alogin.clicked.connect(self.passage7)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.alabel_3.setText(_translate("Form", "Log In"))
        self.auserid.setPlaceholderText(_translate("Form", "User ID"))
        self.apass.setPlaceholderText(_translate("Form", "Password"))
        self.alogin.setText(_translate("Form", "L o g In"))
        self.clabel_5.setText(_translate("Form", "Entrée-in"))
        self.alabel_6.setText(_translate("Form", "Administrator"))
        self.alabel_7.setText(_translate("Form", " m"))
        self.clback.setText(_translate("Form", "8"))

        global check
        check = True
        if(check):
                global x
                x = Form
                check = False



    def passage7(self):
        self.admin_logincheck(x)

    def post_admin_login(self,x):
        self.window3 = QtWidgets.QMainWindow()
        self.ui = admin1.Ui_Form()
        self.ui.setupUi(self.window3)
        self.window3.show()
        x.close()

    def admin_logincheck(self, x):
        usern = self.auserid.text()
        pass11 = self.apass.text()
        check = False
        if (usern != "" and pass11 != ""):
            check = True
        connection = sqlite3.connect("Project.db")

        result_user = connection.execute(f"SELECT username FROM Admin_Login WHERE username = '{usern}'")
        result_pass = connection.execute(f"SELECT password FROM Admin_Login WHERE password = '{pass11}'")

        usern = result_user.fetchone()
        pass11 = result_pass.fetchone()
        # result1 = result1.fetchall()

        if (usern != None and pass11 != None):
            self.window3 = QtWidgets.QMainWindow()
            self.ui = admin1.Ui_Form()
            self.ui.setupUi(self.window3)
            self.window3.show()
            x.close()
        else:
            if ((usern == None) and (pass11 == None) and (check == False)):
                self.messageLabel.setText("Please Enter Credentials")
            elif ((usern == None) and (pass11 == None) and (check == True)):
                self.messageLabel.setStyleSheet("font-size:29px;\n"
                                                "color: #6B6B6B;")
                self.messageLabel.setText("Invalid Username and Password")
            elif (usern == None):
                self.messageLabel.setText("Invalid Username")
            else:
                self.messageLabel.setText("Invalid Password")
        connection.close()

    def home(self,x):
        self.window4 = QtWidgets.QMainWindow()
        self.ui = home.Ui_Form()
        self.ui.setupUi(self.window4)
        self.window4.show()
        x.close()

    def passage6(self):
        self.home(x)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())