# Form implementation generated from reading ui file 'dialog_lic.ui'
#
# Created by: PyQt6 UI code generator 6.5.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(344, 119)
        Form.setMinimumSize(QtCore.QSize(344, 119))
        Form.setMaximumSize(QtCore.QSize(344, 119))
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(28, 20, 290, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "temi: license"))
        self.pushButton.setText(_translate("Form", "Establecer"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
