from PyQt5 import QtGui, QtWidgets
from main_window_ui import MainWindowUi
from db_connection import DBConnection
from data_insertion_window import DataInsertionWindow
from decryption_window import DecryptionWindow

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__()
        self.ui = MainWindowUi()
        self.ui.setupUi(self)
        self.dbConnection = DBConnection(self)
        self.setData()
        self.ui.push_button_add.clicked.connect(self.dataInsertionWindowShow)
        self.ui.push_button_refresh.clicked.connect(self.refresh)
        self.ui.push_button_delete.clicked.connect(self.delete)
        self.ui.tableWidget.cellDoubleClicked.connect(self.decryptionWindowShow)

    def setData(self):
        try:
            self.dbConnection.cursor.execute("SELECT * FROM user_account")
            account_data = self.dbConnection.cursor.fetchall()

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

    def refresh(self):
        self.setData()

    def delete(self):
        try:
            ind = self.ui.tableWidget.selectionModel().selectedRows()
            ind2 = self.ui.tableWidget.selectionModel().currentIndex()
            val = ind2.sibling(ind2.row(), ind2.column()).data()
            
            for i in sorted(ind):
                self.ui.tableWidget.removeRow(i.row())
                
            self.dbConnection.cursor.execute("DELETE FROM user_account WHERE account = (?)", (val,))
            self.dbConnection.db.commit()
            
        except Exception:
            print('Nothing Selected')

    def decryptionWindowShow(self):
        index = self.ui.tableWidget.selectionModel().currentIndex()
        value = index.sibling(index.row(), index.column()).data()

        self.decryptionWindow = DecryptionWindow(value)
        self.decryptionWindow.show()