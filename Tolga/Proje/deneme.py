from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(376, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 351, 421))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.txtUserInput = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtUserInput.setObjectName("txtUserInput")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtUserInput)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.txtSifre = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txtSifre.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtSifre.setObjectName("txtSifre")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtSifre)
        self.btGiris = QtWidgets.QPushButton(self.formLayoutWidget)
        self.btGiris.setObjectName("btGiris")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.btGiris)
        self.btIptal = QtWidgets.QPushButton(self.formLayoutWidget)
        self.btIptal.setObjectName("btIptal")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.btIptal)
        self.lblSonuc = QtWidgets.QLabel(self.formLayoutWidget)
        self.lblSonuc.setText("")
        self.lblSonuc.setObjectName("lblSonuc")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lblSonuc)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 376, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Kullanıcı Adı:"))
        self.label_2.setText(_translate("MainWindow", "Şifre:"))
        self.btGiris.setText(_translate("MainWindow", "Giriş Yap"))
        self.btIptal.setText(_translate("MainWindow", "İptal"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



