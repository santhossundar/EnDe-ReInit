from PyQt5 import QtCore, QtGui, QtWidgets
from data_insertion_window_ui import DialogUi
from db_connection import DBConnection
from encrypter import ende
import sqlite3

class DataInsertionWindow(QtWidgets.QDialog):
    def __init__(self, parent = None):
        super(DataInsertionWindow, self).__init__()
        self.ui = DialogUi()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('logo/ende_logo.ico'))
        self.ui.pushButtonSave.clicked.connect(self.insertData)

    def insertData(self):
        self.dbConnection = DBConnection(self)
        account = self.ui.accountLineEdit.text()
        password = self.ui.passwordLineEdit.text()
        key = self.ui.keyLineEdit.text()

        encrypted_password = ende(key, password).createCipher()

        if (account != '' and password != '' and key != ''):
            self.dbConnection.cursor.execute("INSERT INTO user_account (account, password) VALUES (?,?)" ,(account, memoryview(encrypted_password)))
            self.dbConnection.db.commit()
            self.dbConnection.cursor.close()
            self.dbConnection.db.close()
            QtWidgets.QDialog.close(self)
        else:
            QtWidgets.QMessageBox.information(QtWidgets.QMessageBox(), 'Error', 'All Fields are required!')

        



    

