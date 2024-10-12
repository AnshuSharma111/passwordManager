import sys
from PyQt6 import QtWidgets, uic
from MainWindow import Ui_MainWindow
from datasecurity import *

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.proceedButton.clicked.connect(lambda : authenticate(self.inputField.toPlainText()))

app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()