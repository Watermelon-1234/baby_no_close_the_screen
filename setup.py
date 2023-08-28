import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {'packages': [], 'excludes': []}

setup(  name = 'no kids close computer',
        version = '1.1',
        description = '讓小孩在靠近電腦時黑屏且無法操控電腦',
        options = {'build_exe': build_exe_options},
        executables = [Executable('main.py',base="Win32GUI",icon='autodraw.ico')])