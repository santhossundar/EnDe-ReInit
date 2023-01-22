from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 100)
        Dialog.setMaximumSize(QtCore.QSize(400, 100))

        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(9, 9, 381, 75))
        self.formLayoutWidget.setObjectName("formLayoutWidget")

        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")

        self.keyLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.keyLabel.setObjectName("keyLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.keyLabel)

        self.keyLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.keyLineEdit.setObjectName("keyLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.keyLineEdit)

        self.pushButtonDecrypt = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButtonDecrypt.setObjectName("pushButtonDecrypt")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pushButtonDecrypt)
        
        self.passwordLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.passwordLineEdit.setReadOnly(True)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.passwordLineEdit)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Decrypter"))
        self.keyLabel.setText(_translate("keyLabel", "Key"))
        self.pushButtonDecrypt.setText(_translate("pushButtonDecrypt", "Decrypt"))
        self.passwordLineEdit.setPlaceholderText(_translate("passwordLineEdit", "Your Password"))
