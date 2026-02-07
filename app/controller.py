from PySide6.QtWidgets import QInputDialog, QTableWidgetItem
from .model import VaultModel

class PasswordController:
    def __init__(self, view, model: VaultModel):
        self.view = view
        self.model = model

        self.refresh()

        view.add_btn.clicked.connect(self.add)
        view.del_btn.clicked.connect(self.delete)
        view.decode_btn.clicked.connect(self.decode)
        view.search.textChanged.connect(self.refresh)

    def refresh(self):
        query = self.view.search.text().lower()
        self.view.table.setRowCount(0)

        for i, e in enumerate(self.model.entries):
            name = e["name"]
            username = self.model.decode_username(i)
            comment = e["comment"]

            if query and query not in name.lower() and query not in comment.lower():
                continue

            row = self.view.table.rowCount()
            self.view.table.insertRow(row)

            self.view.table.setItem(row, 0, QTableWidgetItem(name))
            self.view.table.setItem(row, 1, QTableWidgetItem(username))
            self.view.table.setItem(row, 2, QTableWidgetItem("••••••"))
            self.view.table.setItem(row, 3, QTableWidgetItem(comment))

    def current_index(self):
        row = self.view.table.currentRow()
        return row if row >= 0 else None

    def add(self):
        name, ok = QInputDialog.getText(self.view, "Name", "Name:")
        if not ok: return
        user, ok = QInputDialog.getText(self.view, "Username", "Username:")
        if not ok: return
        pwd, ok = QInputDialog.getText(self.view, "Password", "Password:")
        if not ok: return
        com, _ = QInputDialog.getText(self.view, "Comment", "Comment:")

        self.model.add(name, user, pwd, com)
        self.refresh()

    def delete(self):
        idx = self.current_index()
        if idx is None:
            return
        self.model.delete(idx)
        self.refresh()

    def decode(self):
        idx = self.current_index()
        if idx is None:
            return

        pwd = self.model.decode_password(idx)
        self.view.table.setItem(idx, 2, QTableWidgetItem(pwd))
