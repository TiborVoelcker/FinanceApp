# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Kategorien.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(355, 353)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.add_category = QtWidgets.QPushButton(Dialog)
        self.verticalLayout.addWidget(self.add_category)
        self.delete_category = QtWidgets.QPushButton(Dialog)
        self.verticalLayout.addWidget(self.delete_category)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.listView = QtWidgets.QListView(Dialog)
        self.gridLayout_2.addWidget(self.listView, 0, 0, 1, 1)
        self.Ok = QtWidgets.QPushButton(Dialog)
        self.gridLayout_2.addWidget(self.Ok, 1, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Kategorien"))
        self.add_category.setText(_translate("Dialog", "Hinzufügen"))
        self.delete_category.setText(_translate("Dialog", "Löschen"))
        self.Ok.setText(_translate("Dialog", "Bestätigen"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

