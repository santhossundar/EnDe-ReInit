from PyQt5 import QtCore, QtGui, QtWidgets
from decryption_window_ui import Ui_Dialog
from db_connection import DBConnection
import hashlib
from Cryptodome.Cipher import AES
import sqlite3

class DecryptionWindow(QtWidgets.QDialog):
    def __init__(self, password, parent = None):
        super(DecryptionWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('logo/ende_logo.ico'))
        self.password = password

        self.dbConnection = DBConnection()
        self.dbConnection.cursor.execute("SELECT * FROM user_account")
        accountData = self.dbConnection.cursor.fetchall()

        for i in range(len(accountData)):
            if(str(accountData[i][1]) == self.password):
                self.bytePassword = accountData[i][1]
            elif (accountData[i][0] == self.password):
                self.bytePassword = accountData[i][1]
            
        self.dbConnection.cursor.close()
        self.dbConnection.db.close()

        self.ui.pushButtonDecrypt.clicked.connect(self.decryptPassword)

    def decryptPassword(self):
        key = self.ui.keyLineEdit.text()
        
        hashedKeySalt = dict()
        userKey = bytes(key, "utf-8")
        userSalt = bytes(key[::-1], "utf-8")
        hashType = "SHA256"
        hash = hashlib.new(hashType)
        hash.update(userKey)
        hashedKeySalt["key"] = bytes(hash.hexdigest()[:32], "utf-8")
        hash = hashlib.new(hashType)
        hash.update(userSalt)
        hashedKeySalt["salt"] = bytes(hash.hexdigest()[:16], "utf-8")

        deCipherObject = AES.new(hashedKeySalt["key"],AES.MODE_CFB,hashedKeySalt["salt"])
        decryptedContent = deCipherObject.decrypt(self.bytePassword)
        
        self.ui.passwordLineEdit.setText(str(decryptedContent).replace('b', '').replace('\'',''))