import PyInstaller.__main__
import shutil
import os

file_name = 'malicious.py'
exe_name = 'benign.exe'
icon = 'Firefox.ico'
pwd = os.getcwd()
usb_dir = os.path.join(pwd, 'USB')

if os.path.isfile(exe_name):
    os.remove(exe_name)

# Create executable from Python script
PyInstaller.__main__.run([
    file_name,
    '--onefile',
    '--clean',
    '--log-level=ERROR',
    '--name='+exe_name,
    '--icon='+icon
])

# Clean up after PyInstaller
shutil.move(os.path.join(pwd, 'dist', exe_name), pwd)
shutil.rmtree('dist')
shutil.rmtree('build')
# shutil.rmtree('__pycache__')
os.remove(exe_name+'.spec')
