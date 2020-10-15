# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(650, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.verticalLayout.addWidget(self.tableView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.delete_data = QtWidgets.QPushButton(self.centralwidget)
        self.horizontalLayout.addWidget(self.delete_data)
        self.edit_data = QtWidgets.QPushButton(self.centralwidget)
        self.horizontalLayout.addWidget(self.edit_data)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.turnus = QtWidgets.QComboBox(self.centralwidget)
        self.horizontalLayout_2.addWidget(self.turnus)
        self.turnus.addItems(["einmalig", "monatlich", "halbjährlich", "jährlich"])
        self.amount = QtWidgets.QLineEdit(self.centralwidget)
        self.horizontalLayout_2.addWidget(self.amount)
        self.use = QtWidgets.QLineEdit(self.centralwidget)
        self.horizontalLayout_2.addWidget(self.use)
        self.category = QtWidgets.QComboBox(self.centralwidget)
        self.horizontalLayout_2.addWidget(self.category)
        self.date = QtWidgets.QDateEdit(self.centralwidget)
        self.horizontalLayout_2.addWidget(self.date)
        self.add_data = QtWidgets.QPushButton(self.centralwidget)
        self.horizontalLayout_2.addWidget(self.add_data)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 26))
        self.menuDatei = QtWidgets.QMenu(self.menubar)
        self.menuKategorie = QtWidgets.QMenu(self.menubar)
        MainWindow.setMenuBar(self.menubar)
        self.actionChange = QtWidgets.QAction(MainWindow)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionBudget = QtWidgets.QAction(MainWindow)
        self.menuKategorie.addAction(self.actionChange)
        self.menuKategorie.addAction(self.actionBudget)
        self.menuDatei.addAction(self.actionSave)
        self.menubar.addAction(self.menuDatei.menuAction())
        self.menubar.addAction(self.menuKategorie.menuAction())
        self.actionAdd = QtWidgets.QAction(MainWindow)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Finanzen"))
        self.delete_data.setText(_translate("MainWindow", "Löschen"))
        self.edit_data.setText(_translate("MainWindow", "Bearbeiten"))
        self.add_data.setText(_translate("MainWindow", "Hinzufügen"))
        self.menuDatei.setTitle(_translate("MainWindow", "Datei"))
        self.menuKategorie.setTitle(_translate("MainWindow", "Kategorie"))
        self.actionChange.setText(_translate("MainWindow", "Bearbeiten"))
        self.actionSave.setText(_translate("MainWindow", "Speichern"))
        self.actionBudget.setText(_translate("MainWindow", "Budget"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

