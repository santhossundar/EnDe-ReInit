from PyQt5 import QtCore, QtGui, QtWidgets

class DialogUi(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 1250)
        Dialog.setMaximumSize(QtCore.QSize(400, 125))

        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(9, 9, 381, 103))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
    
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")

        self.accountLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.accountLabel.setObjectName("accountLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.accountLabel)
        
        self.accountLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.accountLineEdit.setObjectName("accountLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.accountLineEdit)
        
        self.passwordLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.passwordLabel.setObjectName("passwordLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.passwordLabel)
        
        self.passwordLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.passwordLineEdit.setFrame(True)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.passwordLineEdit)

        self.keyLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.keyLabel.setObjectName("keyLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.keyLabel)

        self.keyLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.keyLineEdit.setObjectName("keyLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.keyLineEdit)

        self.pushButtonSave = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.pushButtonSave)
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Encrypter"))
        self.accountLabel.setText(_translate("accountLabel", "Account"))
        self.passwordLabel.setText(_translate("passwordLabel", "Password"))
        self.keyLabel.setText(_translate("keyLabel", "Key"))
        self.pushButtonSave.setText(_translate("pushButtonSave", "Save"))
