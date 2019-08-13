import sys
from cx_Freeze import setup, Executable
import os
# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os","numpy","scipy","skimage","pandas","requests","cv2","socket","tkinter","ipaddress"]}
os.environ['TCL_LIBRARY']= r'C:\Users\camacc\Anaconda3\Library\lib\tcl8'
os.environ['TK_LIBRARY']= r'C:\Users\camacc\Anaconda3\Library\lib\tk8.6'

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "Offocus",
        version = "0.1",
        description = "My GUI application!",
        options = {"build_exe": build_exe_options},
        executables = [Executable("main.py", base=base)])