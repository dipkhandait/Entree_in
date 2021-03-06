# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'collegelog.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import home
import collegereg
import college1
check = True

class Ui_Form(object):
        
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(650, 450)
        self.cwidget = QtWidgets.QWidget(Form)
        self.cwidget.setGeometry(QtCore.QRect(20, 20, 590, 420))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.cwidget.setFont(font)
        self.cwidget.setStyleSheet("QPushButton#clogin{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255,255,255,210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#clogin:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150,123,111,255);\n"
"}\n"
"QPushButton#clogin:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#creg{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255,255,255,210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#creg:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150,123,111,255);\n"
"}\n"
"QPushButton#creg:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}")
        self.cwidget.setObjectName("cwidget")
        self.clabel = QtWidgets.QLabel(self.cwidget)
        self.clabel.setGeometry(QtCore.QRect(290, 40, 260, 330))
        self.clabel.setStyleSheet("background-color:rgba(255,255,255,255);\n"
"border-bottom-right-radius:50px")
        self.clabel.setText("")
        self.clabel.setObjectName("clabel")
        self.clabel_2 = QtWidgets.QLabel(self.cwidget)
        self.clabel_2.setGeometry(QtCore.QRect(40, 25, 270, 360))
        self.clabel_2.setStyleSheet("border-top-left-radius:50px;\n"
"background-color:rgba(0,0,0,80);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));")
        self.clabel_2.setText("")
        self.clabel_2.setObjectName("clabel_2")
        self.clabel_3 = QtWidgets.QLabel(self.cwidget)
        self.clabel_3.setGeometry(QtCore.QRect(330, 60, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.clabel_3.setFont(font)
        self.clabel_3.setStyleSheet("color:rgba(0,0,0,200);")
        self.clabel_3.setObjectName("clabel_3")
        self.cuserid = QtWidgets.QLineEdit(self.cwidget)
        self.cuserid.setGeometry(QtCore.QRect(330, 110, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.cuserid.setFont(font)
        self.cuserid.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.cuserid.setObjectName("cuserid")
        self.cpass = QtWidgets.QLineEdit(self.cwidget)
        self.cpass.setGeometry(QtCore.QRect(330, 170, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.cpass.setFont(font)
        self.cpass.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;\n"
"")
        self.cpass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.cpass.setObjectName("cpass")
        self.clogin = QtWidgets.QPushButton(self.cwidget)
        self.clogin.setGeometry(QtCore.QRect(330, 220, 191, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.clogin.setFont(font)
        self.clogin.setObjectName("clogin")
        self.clabel_4 = QtWidgets.QLabel(self.cwidget)
        self.clabel_4.setGeometry(QtCore.QRect(330, 270, 191, 21))
        self.clabel_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.clabel_4.setStyleSheet("color:rgba(0,0,0,200);")
        self.clabel_4.setAlignment(QtCore.Qt.AlignCenter)
        self.clabel_4.setObjectName("clabel_4")
        self.clabel_5 = QtWidgets.QLabel(self.cwidget)
        self.clabel_5.setGeometry(QtCore.QRect(60, 50, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.clabel_5.setFont(font)
        self.clabel_5.setStyleSheet("color:rgba(255,255,255,220);")
        self.clabel_5.setObjectName("clabel_5")
        self.clabel_6 = QtWidgets.QLabel(self.cwidget)
        self.clabel_6.setGeometry(QtCore.QRect(60, 180, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.clabel_6.setFont(font)
        self.clabel_6.setStyleSheet("color:rgba(255,255,255,220);")
        self.clabel_6.setObjectName("clabel_6")
        self.creg = QtWidgets.QPushButton(self.cwidget)
        self.creg.setGeometry(QtCore.QRect(330, 300, 191, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.creg.setFont(font)
        self.creg.setObjectName("creg")
        self.clabel_7 = QtWidgets.QLabel(self.cwidget)
        self.clabel_7.setGeometry(QtCore.QRect(60, 230, 241, 151))
        font = QtGui.QFont()
        font.setFamily("Webdings")
        font.setPointSize(125)
        font.setBold(False)
        font.setWeight(50)
        self.clabel_7.setFont(font)
        self.clabel_7.setObjectName("clabel_7")
        self.clback = QtWidgets.QPushButton(self.cwidget)
        self.clback.setGeometry(QtCore.QRect(460, 60, 81, 23))
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

        self.clback.clicked.connect(self.passage)
        self.creg.clicked.connect(self.passage8)
        self.clogin.clicked.connect(self.passage7)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.clabel_3.setText(_translate("Form", "Log In"))
        self.cuserid.setPlaceholderText(_translate("Form", "User ID"))
        self.cpass.setPlaceholderText(_translate("Form", "Password"))
        self.clogin.setText(_translate("Form", "L o g In"))
        self.clabel_4.setText(_translate("Form", "Not registered yet?"))
        self.clabel_5.setText(_translate("Form", "Entr??e-in"))
        self.clabel_6.setText(_translate("Form", "College"))
        self.creg.setText(_translate("Form", "Register"))
        self.clabel_7.setText(_translate("Form", " ??"))
        self.clback.setText(_translate("Form", "8"))

        global check
        check = True
        if(check):
                global x
                x = Form
                check = False

    def passage7(self):
        self.college_logincheck(x)

    def post_college_login(self,x):
        self.window3 = QtWidgets.QMainWindow()
        self.ui = college1.Ui_Form()
        self.ui.setupUi(self.window3)
        self.window3.show()
        x.close()

    def college_logincheck(self, x):
        usern = self.cuserid.text()
        pass11 = self.cpass.text()
        check = False
        if (usern != "" and pass11 != ""):
            check = True
        connection = sqlite3.connect("Project.db")

        result_user = connection.execute(f"SELECT College_Name FROM College_Registration WHERE College_Name = '{usern}'")

        result_pass = connection.execute(f"SELECT College_Passwd FROM College_Registration WHERE College_Passwd = '{pass11}'")

        usern = result_user.fetchone()
        pass11 = result_pass.fetchone()

        if (usern != None and pass11 != None):
            try:
                user = usern[0]
                connection = sqlite3.connect("Project.db")
                connection.execute(f"Update Current_login set Currentlog_in='{user}' WHERE No = '{2}'")
                connection.commit()
                connection.close()
            except Exception as e:
                print(e)
            self.window3 = QtWidgets.QMainWindow()
            self.ui = college1.Ui_Form()
            self.ui.setupUi(self.window3)
            self.window3.show()
            x.close()
        else:
            if ((usern == None) and (pass11 == None) and (check == False)):
                self.messageLabel.setText("Please Enter Credentials")
            elif ((usern == None) and (pass11 == None) and (check == True)):
                # self.messageLabel.setStyleSheet("font-size:29px;\n"
                #                                 "color: #6B6B6B;")
                self.messageLabel.setText("Invalid Username and Password")
            elif (usern == None):
                self.messageLabel.setText("Invalid Username")
            else:
                self.messageLabel.setText("Invalid Password")
        connection.close()

    def home(self,x):                            
        self.window1 = QtWidgets.QMainWindow()
        self.ui = home.Ui_Form()
        self.ui.setupUi(self.window1)
        self.window1.show()
        x.close()

    def passage(self):
        self.home(x)

    def collegereg(self,x):                            
        self.window5 = QtWidgets.QMainWindow()
        self.ui = collegereg.Ui_Form()
        self.ui.setupUi(self.window5)
        self.window5.show()
        x.close()

    def passage8(self):
        self.collegereg(x)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
