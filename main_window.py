from PyQt5 import QtGui, QtWidgets
from main_window_ui import MainWindowUi
from db_connection import DBConnection
from data_insertion_window import DataInsertionWindow

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__()
        self.ui = MainWindowUi()
        self.ui.setupUi(self)
        self.ui.push_button_add.clicked.connect(self.dataInsertionWindowShow)

        try:
            dbConnection = DBConnection(self)
            dbConnection.cursor.execute("SELECT * FROM user_account")
            account_data = dbConnection.cursor.fetchall()
            dbConnection.cursor.close()
            dbConnection.db.close()

            self.ui.tableWidget.setRowCount(1)
            for i in range(self.ui.tableWidget.rowCount()):
                accountCount = len(account_data)
                self.ui.tableWidget.setRowCount(accountCount)
                i+=1
                for j in range(0,accountCount):
                        self.ui.tableWidget.setItem(j,0, QtWidgets.QTableWidgetItem(account_data[j][0]))
                        self.ui.tableWidget.setItem(j,1, QtWidgets.QTableWidgetItem(str(account_data[j][1])))
                        self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)
                        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        except Exception as e:
            print(e)
    
    def dataInsertionWindowShow(self):
        self.data_insertion_window = DataInsertionWindow()
        self.data_insertion_window.show()