"""
py2app build script for MyApplication

Usage:
	python setup.py py2app -A --packages=PyQt5
        python setup.py py2app --packages=PyQt5 --excludes="PyQt5.uic.port_v3"
"""
from setuptools import setup

APP = ['systray.py']
APP_NAME = "mkchromecast"
DATA_FILES = ['images/google.icns', 'images/google_working.icns']

OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'images/google.icns',
    'includes': ['sip', 'PyQt5', 'PyQt5.QtCore', 'PyQt5.QtGui', 'PyQt5.QtWidgets'],
    'plist': {
        'CFBundleName': APP_NAME,
        'CFBundleDisplayName': APP_NAME,
        'CFBundleGetInfoString': "Cast mac os x audio to your google cast devices",
        'CFBundleIdentifier': "com.mkchromecast.osx",
        'CFBundleVersion': "0.1.5",
        'CFBundleShortVersionString': "0.1.5",
        'NSHumanReadableCopyright': u"Copyright (c) 2016, Muammar El Khatib, All Rights Reserved"
    }
}

setup(
    name=APP_NAME,
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
