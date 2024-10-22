from PyQt6 import QtWidgets
from helper import addToDatabase, setMasterPassword
import pyperclip

class wrongPassDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Wrong Password!")

        QBtn = (
            QtWidgets.QDialogButtonBox.StandardButton.Ok
        )

        self.buttonBox = QtWidgets.QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)

        layout = QtWidgets.QVBoxLayout()
        message = QtWidgets.QLabel("Wrong Password")
        layout.addWidget(message)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)

class pleaseEnterValidData(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Invalid Data")

        QBtn = (
            QtWidgets.QDialogButtonBox.StandardButton.Ok
        )

        self.buttonBox = QtWidgets.QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)

        layout = QtWidgets.QVBoxLayout()
        message = QtWidgets.QLabel("Please fill valid data!")
        layout.addWidget(message)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)

class listItem(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.frame = QtWidgets.QFrame(self)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)

        self.titleLabel = QtWidgets.QLabel('Title', self.frame)
        self.uLabel = QtWidgets.QLabel('Username', self.frame)
        self.pLabel = QtWidgets.QLabel('Password', self.frame)
        self.username = QtWidgets.QLabel('-', self.frame)
        self.password = QtWidgets.QLabel('-', self.frame)
        self.uCopyBtn = QtWidgets.QPushButton('C', self.frame)
        self.pCopyBtn = QtWidgets.QPushButton('C', self.frame)

        self.uCopyBtn.clicked.connect(lambda : pyperclip.copy(self.username.text()))
        self.pCopyBtn.clicked.connect(lambda : pyperclip.copy(self.password.text()))

        gridLayout = QtWidgets.QGridLayout(self.frame)

        gridLayout.addWidget(self.titleLabel, 0, 0, 1, 2)
        gridLayout.addWidget(self.uLabel, 1, 0)
        gridLayout.addWidget(self.username, 1, 1, 1, 5)
        gridLayout.addWidget(self.uCopyBtn, 1, 6)
        gridLayout.addWidget(self.pLabel, 2, 0)
        gridLayout.addWidget(self.password, 2, 1, 1, 5)
        gridLayout.addWidget(self.pCopyBtn, 2, 6)

        trueLayout = QtWidgets.QVBoxLayout(self)
        trueLayout.addWidget(self.frame)
    
    def updateUI(self, data):
        self.titleLabel.setText(data[1])
        self.username.setText(data[2])
        self.password.setText(data[3])

class createPasswordDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Create New Password")

        self.createCancelBtn = QtWidgets.QDialogButtonBox((
            QtWidgets.QDialogButtonBox.StandardButton.Cancel|
            QtWidgets.QDialogButtonBox.StandardButton.Ok
        ))
        self.tLabel = QtWidgets.QLabel("Title")
        self.uLabel = QtWidgets.QLabel("Username")
        self.pLabel = QtWidgets.QLabel("Password")
        self.tLineEdit = QtWidgets.QLineEdit()
        self.uLineEdit = QtWidgets.QLineEdit()
        self.pLineEdit = QtWidgets.QLineEdit()

        self.createCancelBtn.accepted.connect(self.sendData)
        self.createCancelBtn.rejected.connect(self.reject)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.tLabel)
        layout.addWidget(self.tLineEdit)
        layout.addWidget(self.uLabel)
        layout.addWidget(self.uLineEdit)
        layout.addWidget(self.pLabel)
        layout.addWidget(self.pLineEdit)
        layout.addWidget(self.createCancelBtn)

        self.setLayout(layout)
    def sendData(self):
        # Fetch Data From Form
        title = self.tLineEdit.text()
        username = self.uLineEdit.text()
        password = self.pLineEdit.text()
        # Verify Data
        if not title or not username or not password:
            dialog = pleaseEnterValidData()
            dialog.exec()
            return
        # Send it to Database and UI
        addToDatabase(title, username, password)
        self.accept()
    
class createMasterPassword(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Set Master Password")

        self.setMasterPassword = QtWidgets.QDialogButtonBox((
            QtWidgets.QDialogButtonBox.StandardButton.Ok
        ))
        self.pLabel = QtWidgets.QLabel("Set Master Password")
        self.pLineEdit = QtWidgets.QLineEdit()

        self.setMasterPassword.accepted.connect(self.sendData)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.pLabel)
        layout.addWidget(self.pLineEdit)
        layout.addWidget(self.setMasterPassword)

        self.setLayout(layout)
    def sendData(self):
        # Fetch Data From Form
        password = self.pLineEdit.text()
        # Verify Data
        if not password:
            dialog = pleaseEnterValidData()
            dialog.exec()
            return
        # Send it to storage
        setMasterPassword(password)
        self.accept()