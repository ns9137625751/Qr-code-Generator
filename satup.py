from enum import auto
from cx_Freeze import *
import sys
includefile=['Iconsmind-Outline-QR-Code.ico']
base=None
if sys.platform=='win32':
    base='win32GUI'

shortcut_table=[
    ("DesktopShortcut",
    "DesktopFolder",
    "Qr Generator",
    "TARGETDIR",
    "[TARGETDIR]\Qrcodegenerator.exe",
    None,
    None,
    None,
    None,
    None,
    None,
    "TARGETDIR",
    )
]
msi_data={'Shortcut':shortcut_table}
bdist_msi_options={'data':msi_data}
setup(
    version='1.0',
    description='QR generator software',
    author='Nishant Shekhada',
    name='Nishant',
    options={'build_exe':{'include_files':includefile},'bdist_msi':bdist_msi_options,},
    executables=[
        Executable(
            script="QR_code.py",
            base=base,
            icon='Iconsmind-Outline-QR-Code.ico',
            
        )
    ]
)