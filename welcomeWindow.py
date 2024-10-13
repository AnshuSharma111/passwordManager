from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_welcomeWindow(object):
    def setupUi(self, welcomeWindow):
        welcomeWindow.setObjectName("welcomeWindow")
        welcomeWindow.resize(800, 601)
        self.centralwidget = QtWidgets.QWidget(parent=welcomeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title_label = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(False)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")
        self.verticalLayout.addWidget(self.title_label)
        self.textLabel1 = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        self.textLabel1.setFont(font)
        self.textLabel1.setObjectName("textLabel1")
        self.verticalLayout.addWidget(self.textLabel1)
        self.inputField = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.inputField.setObjectName("inputField")
        self.verticalLayout.addWidget(self.inputField)
        self.proceedButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.proceedButton.setObjectName("proceedButton")
        self.verticalLayout.addWidget(self.proceedButton)
        welcomeWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=welcomeWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        welcomeWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=welcomeWindow)
        self.statusbar.setObjectName("statusbar")
        welcomeWindow.setStatusBar(self.statusbar)

        self.retranslateUi(welcomeWindow)
        QtCore.QMetaObject.connectSlotsByName(welcomeWindow)

    def retranslateUi(self, welcomeWindow):
        _translate = QtCore.QCoreApplication.translate
        welcomeWindow.setWindowTitle(_translate("welcomeWindow", "MainWindow"))
        self.title_label.setText(_translate("welcomeWindow", "Password Manager"))
        self.textLabel1.setText(_translate("welcomeWindow", "Enter Master Password"))
        self.proceedButton.setText(_translate("welcomeWindow", "Proceed"))
