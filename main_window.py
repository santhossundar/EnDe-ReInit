from PyQt5 import QtGui, QtWidgets
from main_window_ui import MainWindowUi

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__()
        self.ui = MainWindowUi()
        self.ui.setupUi(self)