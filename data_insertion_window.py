from PyQt5 import QtCore, QtGui, QtWidgets
from data_insertion_window_ui import DialogUi
from db_connection import DBConnection
import sqlite3

class DataInsertionWindow(QtWidgets.QDialog):
    def __init__(self, parent = None):
        super(DataInsertionWindow, self).__init__()
        self.ui = DialogUi()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('logo/ende_logo.ico'))
        self.dbConnection = DBConnection(self)
            


        



    

