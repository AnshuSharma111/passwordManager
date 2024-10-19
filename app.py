import sys
import os
from PyQt6 import QtWidgets
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize
from welcomeWindow import Ui_welcomeWindow as welcomeWin
from mainWindow import Ui_mainWindow as mainWin
from customWidgets import wrongPassDialog, listItem, createPasswordDialog
from helper import fetchLatestData, authenticate, closeConnection, initialise

basedir = os.path.dirname(__file__)
icon_path = os.path.join(basedir, 'icon.ico')
TITLE = "Password Manager"

# 0 -> welcomeWin, 1 -> mainWin
def changeWindow(cur, windowIndex):
    cur.hide()
    if windowIndex == 0:
        welcomeWindow.show()
    else:
        mainWindow.show()

# welcome window
class welcomeWindow(QtWidgets.QMainWindow, welcomeWin):
    def __init__(self, *args, obj=None, **kwargs):
        super(welcomeWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.setWindowTitle(TITLE)
        self.setFixedSize(QSize(800, 558))

        self.proceedButton.clicked.connect(self.proceed)
    
    def proceed(self):
        isAuthenticated = authenticate(self.inputField.toPlainText())
        if isAuthenticated:
            changeWindow(self, 1)
        else:
            dlg = wrongPassDialog()
            dlg.exec()

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
    def addToList(self, data):
        newItem = listItem()
        newItem.updateUI(data)
        listI = QtWidgets.QListWidgetItem(self.passList)

        listI.setSizeHint(newItem.sizeHint())
        
        self.passList.addItem(listI)
        self.passList.setItemWidget(listI, newItem)
    def deleteItem(self):
        toDelete = self.passList.selectedIndexes()
        deletion_indices = []
        for index in toDelete:
            deletion_indices.append(index.row())
    def closeEvent(self, event):
        closeConnection()
        event.accept()

app = QtWidgets.QApplication(sys.argv)
app.setApplicationName(TITLE)
app.setWindowIcon(QIcon(icon_path))

welcomeWindow = welcomeWindow()
mainWindow = mainWindow()

welcomeWindow.show()

sys.exit(app.exec())