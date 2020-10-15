from Views.MainWindow import Ui_MainWindow
from Views.CategoryEditor import Ui_Dialog
from Views.Budgets import Ui_Dialog2
from PyQt5 import QtWidgets, QtCore, QtGui


class Gui(QtWidgets.QMainWindow, Ui_MainWindow):                # Main Window
    def __init__(self):
        super(Gui, self).__init__()
        self.setupUi(self)
        self.setMinimumWidth(650)

        self.tableView.verticalHeader().setVisible(False)       # customize headers
        header = self.tableView.horizontalHeader()
        header.setStretchLastSection(True)
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.amount.setPlaceholderText("Betrag")
        self.use.setPlaceholderText("Zweck")
        self.date.setDate(QtCore.QDate.currentDate())
        self.validator1 = QtGui.QDoubleValidator()
        self.validator2 = QtGui.QRegExpValidator()
        self.amount.setValidator(self.validator1)
        self.use.setValidator(self.validator2)
        self.actionSave.setShortcut("Ctrl+S")
        self.add_data.setShortcut(QtCore.Qt.Key_Return)
        self.tableView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.menuBudget = QtWidgets.QMenu(self.menubar)


class Dialog(QtWidgets.QDialog, Ui_Dialog):                     # category-Dialog
    def __init__(self):
        super(Dialog, self).__init__()
        self.setupUi(self)
        self.setModal(1)


class Dialog2(QtWidgets.QDialog, Ui_Dialog2):                    # budgets-Dialog
    def __init__(self):
        super(Dialog2, self).__init__()
        self.setupUi(self)
        self.setModal(1)
