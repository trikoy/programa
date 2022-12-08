from PyQt5 import QtCore, QtGui, QtWidgets
from pingpong import pingpong_igrat








class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(40, 40, 741, 481))
        self.groupBox_2.setObjectName("groupBox_2")
        self.pingpong_igrat = QtWidgets.QPushButton(self.groupBox_2)
        self.pingpong_igrat.setGeometry(QtCore.QRect(390, 130, 111, 31))
        self.pingpong_igrat.setObjectName("pingpong_igrat")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(140, 50, 111, 71))
        self.label_2.setObjectName("label_2")
        self.shuter_igra = QtWidgets.QPushButton(self.groupBox_2)
        self.shuter_igra.setGeometry(QtCore.QRect(140, 130, 111, 31))
        self.shuter_igra.setObjectName("shuter_igra")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(390, 50, 111, 71))
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(260, 50, 111, 71))
        self.label_3.setObjectName("label_3")
        self.labirint_igrat = QtWidgets.QPushButton(self.groupBox_2)
        self.labirint_igrat.setGeometry(QtCore.QRect(260, 130, 111, 31))
        self.labirint_igrat.setObjectName("labirint_igrat")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(40, 400, 71, 41))
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox.setGeometry(QtCore.QRect(150, 220, 341, 181))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(110, 60, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 100, 113, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.login = QtWidgets.QPushButton(self.groupBox)
        self.login.setGeometry(QtCore.QRect(60, 140, 93, 28))
        self.login.setObjectName("login")
        self.leave = QtWidgets.QPushButton(self.groupBox)
        self.leave.setGeometry(QtCore.QRect(180, 140, 93, 28))
        self.leave.setObjectName("leave")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pingpong_igrat.clicked.connect(pingpong_igrat)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_2.setTitle(_translate("MainWindow", "GroupBox"))
        self.pingpong_igrat.setText(_translate("MainWindow", "Грати Пинг понг"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.shuter_igra.setText(_translate("MainWindow", "Грати Шутер"))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
        self.labirint_igrat.setText(_translate("MainWindow", "Грати Лабиринт"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.login.setText(_translate("MainWindow", "логин"))
        self.leave.setText(_translate("MainWindow", "вийти"))









if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
