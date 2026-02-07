import json
from pathlib import Path
from .crypto import encrypt_bytes, decrypt_bytes

from pathlib import Path
import sys

def app_data_dir():
    if sys.platform == "darwin":
        return Path.home() / "Library" / "Application Support" / "PasswordManager"
    else:
        return Path.home() / ".password_manager"

DATA_DIR = app_data_dir()
DATA_DIR.mkdir(parents=True, exist_ok=True)

VAULT_FILE = DATA_DIR / "vault.dat"

class VaultModel:
    def __init__(self, master_password: str):
        self.master_password = master_password
        self.entries = []
        self.load()

    def load(self):
        if not VAULT_FILE.exists():
            self.entries = []
            return

        raw = VAULT_FILE.read_bytes()
        data = json.loads(decrypt_bytes(raw, self.master_password).decode())

        self.entries = data

    def save(self):
        encrypted = encrypt_bytes(
            json.dumps(self.entries).encode(),
            self.master_password
        )
        VAULT_FILE.write_bytes(encrypted)

    def add(self, name, username, password, comment):
        self.entries.append({
            "name": name,
            "username": encrypt_bytes(username.encode(), self.master_password).hex(),
            "password": encrypt_bytes(password.encode(), self.master_password).hex(),
            "comment": comment
        })
        self.save()

    def delete(self, index):
        self.entries.pop(index)
        self.save()

    def update(self, index, name, username, password, comment):
        self.entries[index] = {
            "name": name,
            "username": encrypt_bytes(username.encode(), self.master_password).hex(),
            "password": encrypt_bytes(password.encode(), self.master_password).hex(),
            "comment": comment
        }
        self.save()

    def decode_password(self, index) -> str:
        blob = bytes.fromhex(self.entries[index]["password"])
        return decrypt_bytes(blob, self.master_password).decode()

    def decode_username(self, index) -> str:
        blob = bytes.fromhex(self.entries[index]["username"])
        return decrypt_bytes(blob, self.master_password).decode()
