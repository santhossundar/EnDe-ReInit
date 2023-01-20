from PyQt5 import QtGui, QtWidgets
from main_window_ui import MainWindowUi
from db_connection import DBConnection

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__()
        self.ui = MainWindowUi()
        self.ui.setupUi(self)

        try:
            dbConnection = DBConnection()
            dbConnection.cursor.execute("SELECT * FROM user_account")
            data = dbConnection.cursor.fetchall()
            print(data)

        except Exception as e:
            print(e)
    
        