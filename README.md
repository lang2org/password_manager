# password manager

# Build environment
 Python 3.12.3
 pip install --upgrade pip
 pip install pyside6 cryptography
 pip install pyinstaller 
 
# How to build
 python3 -m venv venv
 source venv/bin/activate
 
 pyinstaller \
  --name PasswordManager \
  --windowed \
  --onefile \
  run.py
 
  deactivate
  
# How to run
   ./dist/PasswordManager
   python run.py
   python -m app.main

# Data location
    linux: ~/.password_manager/vault.dat
