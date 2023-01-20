from PyQt5 import QtCore, QtGui, QtWidgets

class MainWindowUi(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("mainWindow")
        MainWindow.resize(687, 429)
        MainWindow.setMaximumSize(QtCore.QSize(687, 429))

        self.program_icon = QtGui.QIcon()
        self.program_icon.addFile('logo/ende_logo.ico', QtCore.QSize(16,16))
        MainWindow.setWindowIcon(self.program_icon)
        
        self.central_widget = QtWidgets.QWidget(MainWindow)
        self.central_widget.setObjectName("centralWidget")
        
        self.push_button_add = QtWidgets.QPushButton(self.central_widget)
        self.push_button_add.setGeometry(QtCore.QRect(10, 10, 75, 31))
        self.push_button_add.setObjectName("pushButtonAdd")
        MainWindow.setCentralWidget(self.central_widget)
        
        self.menu_bar = QtWidgets.QMenuBar(MainWindow)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menu_bar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menu_bar)
        
        self.status_bar = QtWidgets.QStatusBar(MainWindow)
        self.status_bar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.status_bar)
        
        self.push_button_refresh = QtWidgets.QPushButton(self.central_widget)
        self.push_button_refresh.setObjectName("pushButtonRefresh")
        self.push_button_refresh.setGeometry(QtCore.QRect(90, 10, 75, 31))
        MainWindow.setCentralWidget(self.central_widget)
        
        self.push_button_delete = QtWidgets.QPushButton(self.central_widget)
        self.push_button_delete.setObjectName("pushButtonDelete")
        self.push_button_delete.setGeometry(QtCore.QRect(170, 10, 75, 31))
        MainWindow.setCentralWidget(self.central_widget)

        self.tableWidget = QtWidgets.QTableWidget(self.central_widget)
        
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        
        __qtablewidgetitem = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        
        __qtablewidgetitem1 = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setGeometry(QtCore.QRect(10, 50, 661, 351))
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setTabKeyNavigation(False)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(39)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(330)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        MainWindow.setCentralWidget(self.central_widget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("mainWindow", "EnDe"))
        self.push_button_add.setText(_translate("pushButtonAdd", "Add"))
        self.push_button_refresh.setText(_translate("pushButtonRefresh", "Refresh"))
        self.push_button_delete.setText(_translate("pushButtonDelete", "Delete"))


