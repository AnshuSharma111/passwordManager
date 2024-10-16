from PyQt6 import QtWidgets

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

class listItem(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        frame = QtWidgets.QFrame(self)
        frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)

        titleLabel = QtWidgets.QLabel('Title', frame)
        uLabel = QtWidgets.QLabel('Username', frame)
        pLabel = QtWidgets.QLabel('Password', frame)
        username = QtWidgets.QLabel('-', frame)
        password = QtWidgets.QLabel('-', frame)
        uCopyBtn = QtWidgets.QPushButton('C', frame)
        pCopyBtn = QtWidgets.QPushButton('C', frame)

        gridLayout = QtWidgets.QGridLayout(frame)

        gridLayout.addWidget(titleLabel, 0, 0, 1, 2)
        gridLayout.addWidget(uLabel, 1, 0)
        gridLayout.addWidget(username, 1, 1, 1, 5)
        gridLayout.addWidget(uCopyBtn, 1, 2)
        gridLayout.addWidget(pLabel, 2, 0)
        gridLayout.addWidget(password, 2, 1, 1, 5)
        gridLayout.addWidget(pCopyBtn, 2, 2)

        trueLayout = QtWidgets.QVBoxLayout(self)
        trueLayout.addWidget(frame)