import sys
from PySide6.QtWidgets import QApplication, QInputDialog
from app.view import PasswordView
from app.model import VaultModel
from app.controller import PasswordController

def main():
    app = QApplication(sys.argv)

    master, ok = QInputDialog.getText(
        None, "Master Password", "Enter master password:"
    )
    if not ok:
        sys.exit(0)

    model = VaultModel(master)
    view = PasswordView()
    PasswordController(view, model)

    view.show()
    sys.exit(app.exec())
