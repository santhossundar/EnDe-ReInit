from PyQt5 import QtCore, QtGui, QtWidgets
from decryption_window_ui import Ui_Dialog
from db_connection import DBConnection
import hashlib
from Cryptodome.Cipher import AES
import sqlite3

class DecryptionWindow(QtWidgets.QDialog):
    def __init__(self, parent = None):
        super(DecryptionWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('logo/ende_logo.ico'))