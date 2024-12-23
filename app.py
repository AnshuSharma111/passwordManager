import sys
import os
from PyQt6 import QtWidgets
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize
from welcomeWindow import Ui_welcomeWindow as welcomeWin
from mainWindow import Ui_mainWindow as mainWin
from customWidgets import wrongPassDialog, listItem, createPasswordDialog, createMasterPassword
from helper import fetchLatestData, authenticate, closeConnection, initialise, deleteFromDatabase, checkMasterPassword

basedir = os.path.dirname(__file__)
icon_path = os.path.join(basedir, 'icon.ico')
TITLE = "Password Manager"

# welcome window
class welcomeWindow(QtWidgets.QMainWindow, welcomeWin):
    def __init__(self, *args, obj=None, **kwargs):
        super(welcomeWindow, self).__init__(*args, **kwargs)

        self.setupUi(self)
        self.setWindowTitle(TITLE)
        self.setFixedSize(QSize(800, 558))
        self.attempts = 3

        self.proceedButton.clicked.connect(self.authenticatePassword)
        self.inputField.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

    def authenticatePassword(self):
        isAuthenticated = authenticate(self.inputField.text())
        if isAuthenticated:
            print("Correct Password...Proceeding...")
            self.proceedToMain() # successful attempt
        else:
            dlg = wrongPassDialog()
            dlg.exec()
            self.attempts -= 1 # unsuccessful attempt
            if self.attempts == 0:
                print("Out of Attempts...Closing Application...")
                sys.exit(0)
    
    def proceedToMain(self):
        self.mainWindow = mainWindow()
        self.mainWindow.show()

        self.hide()

# main window
class mainWindow(QtWidgets.QMainWindow, mainWin):
    def __init__(self, *args, obj=None, **kwargs):
        super(mainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        to_render_data = initialise()
        self.setup(to_render_data)
        self.setWindowTitle(TITLE)
        self.setFixedSize(QSize(800, 558))
        self.addPass.clicked.connect(self.addNewItem)
        self.delPass.clicked.connect(self.deleteItem)
        self.passList.setSelectionMode(QtWidgets.QListWidget.SelectionMode.ExtendedSelection)
    
    def setup(self, data):
        for i in data:
            self.addToList(i)
    def addNewItem(self):
        dialog = createPasswordDialog()
        res = dialog.exec()
        if res:
            data = fetchLatestData()
            self.addToList(data)
    def deleteItem(self):
        selectedItems = self.passList.selectedItems()
        deletion_indices = [self.passList.row(x)+1 for x in selectedItems]
        if len(deletion_indices):
            # Remove From Database
            deleteFromDatabase(deletion_indices)

            # Remove Graphically
            self.deleteFromList(selectedItems)
    def addToList(self, data):
        newItem = listItem()
        newItem.updateUI(data)
        listI = QtWidgets.QListWidgetItem(self.passList)

        listI.setSizeHint(newItem.sizeHint())
        
        self.passList.addItem(listI)
        self.passList.setItemWidget(listI, newItem)
    def deleteFromList(self, items):
        for item in items:
            self.passList.removeItemWidget(item)
            self.passList.takeItem(self.passList.row(item))
    def closeEvent(self, event):
        closeConnection()
        event.accept()

app = QtWidgets.QApplication(sys.argv)
app.setApplicationName(TITLE)
app.setWindowIcon(QIcon(icon_path))

# check if master password exits or not
hasMasterPassword = checkMasterPassword()
if not hasMasterPassword:
    dialog = createMasterPassword()
    response = dialog.exec()
    if not response:
        print("Closing Application...")
        sys.exit(0)
else:
    print("Password Exists. Proceeding...")

# Block access to rest of app until authenticated
welcomeWindow = welcomeWindow()
welcomeWindow.show()

sys.exit(app.exec())