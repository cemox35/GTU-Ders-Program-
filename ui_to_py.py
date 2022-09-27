from PyQt6 import uic

with open('ui_to_py.ui', 'r') as f:
    with open('ui_to_py.py', 'w') as f2:
        uic.compileUi(f, f2)