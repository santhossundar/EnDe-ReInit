import sys
from PyQt5 import QtGui, QtWidgets
from main_window import MainWindow

def main():
    app = QtWidgets.QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

