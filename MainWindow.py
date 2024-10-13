from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.addPass = QtWidgets.QPushButton(parent=self.centralwidget)
        self.addPass.setGeometry(QtCore.QRect(20, 30, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.addPass.setFont(font)
        self.addPass.setObjectName("addPass")
        self.changeMasterPass = QtWidgets.QPushButton(parent=self.centralwidget)
        self.changeMasterPass.setGeometry(QtCore.QRect(500, 30, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.changeMasterPass.setFont(font)
        self.changeMasterPass.setObjectName("changeMasterPass")
        self.passList = QtWidgets.QListWidget(parent=self.centralwidget)
        self.passList.setGeometry(QtCore.QRect(20, 80, 761, 471))
        self.passList.setObjectName("passList")
        self.delPass = QtWidgets.QPushButton(parent=self.centralwidget)
        self.delPass.setGeometry(QtCore.QRect(80, 30, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.delPass.setFont(font)
        self.delPass.setObjectName("delPass")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        self.addPass.setText(_translate("mainWindow", "+"))
        self.changeMasterPass.setText(_translate("mainWindow", "⚙Change Master Password"))
        self.delPass.setText(_translate("mainWindow", "-"))
