from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
    QLineEdit, QTableWidget, QTableWidgetItem, QMessageBox
)

class PasswordView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Manager")

        layout = QVBoxLayout(self)

        self.search = QLineEdit()
        self.search.setPlaceholderText("Search...")
        layout.addWidget(self.search)

        self.table = QTableWidget(0, 4)
        self.table.setHorizontalHeaderLabels(
            ["Name", "Username", "Password", "Comment"]
        )
        layout.addWidget(self.table)

        btns = QHBoxLayout()
        self.add_btn = QPushButton("Add")
        self.edit_btn = QPushButton("Edit")
        self.del_btn = QPushButton("Delete")
        self.decode_btn = QPushButton("Decode Password")

        for b in (self.add_btn, self.edit_btn, self.del_btn, self.decode_btn):
            btns.addWidget(b)

        layout.addLayout(btns)

    def error(self, msg):
        QMessageBox.critical(self, "Error", msg)
