from PyQt5 import QtGui, QtWidgets, QtCore
import sys
import ctypes
from Views.Configuration import Gui, Dialog, Dialog2
from Models import TableModel2, TableModel
import pickle
LENGTH_OF_TURNUS = 3                                # number of years, for how long the turnus should generate data


if __name__ == "__main__":
    def insert():
        if view.turnus.currentIndex() == 0:
            model.insertRow([view.date.date(), view.use.text(), view.category.currentText(),
                             view.amount.text()])
        if view.turnus.currentIndex() == 1:
            for i in range(12*LENGTH_OF_TURNUS):
                model.insertRow([view.date.date().addMonths(i), view.use.text(), view.category.currentText(),
                                 view.amount.text()])
        if view.turnus.currentIndex() == 2:
            for i in range(2*LENGTH_OF_TURNUS):
                model.insertRow([view.date.date().addMonths(i*6), view.use.text(), view.category.currentText(),
                                 view.amount.text()])
        if view.turnus.currentIndex() == 3:
            for i in range(LENGTH_OF_TURNUS):
                model.insertRow([view.date.date().addYears(i), view.use.text(), view.category.currentText(),
                                 view.amount.text()])
        view.turnus.setCurrentIndex(0)
        view.use.clear()
        view.amount.clear()

    def change():
        for index in view.tableView.selectedIndexes():                              # Dependencies of cell contents
            if index.column() == 0:
                model.changeCell(0, index, view.date.date())
            elif index.column() == 1:
                model.changeCell(1, index, view.use.text())
            elif index.column() == 2:
                model.changeCell(2, index, view.category.currentText())
            elif index.column() == 3:
                model.changeCell(3, index, view.amount.text())
            else:
                pass
        view.use.clear()
        view.amount.clear()
        view.date.setDate(QtCore.QDate.currentDate())

    def remove():
        model.removeRows(view.tableView.selectedIndexes())

    def insert2():
        model2.insertRow()

    def remove2():
        model2.removeRow(view2.listView.selectedIndexes())

    def save():
        model.save()
        model2.save()

    def load_model():
        model = TableModel(headers)
        pickle_in = open("Data/data.pickle", "rb")
        temp_data = pickle.load(pickle_in)
        pickle_in.close()
        model.load(temp_data)
        return model

    def load_model2():
        model2 = TableModel2()
        pickle_in = open("Data/category.pickle", "rb")
        temp_data = pickle.load(pickle_in)
        pickle_in.close()
        model2.load(temp_data)
        return model2


    # make Taskbar-Icon visible
    myappid = 'mycompany.myproduct.subproduct.version'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    # start App
    app = QtWidgets.QApplication(sys.argv)

    # set Icon
    app_Icon = QtGui.QIcon("Resources/coins.png")
    app.setWindowIcon(app_Icon)

    # data
    headers = ["Datum", "Zweck", "Kategorie", "Betrag", "Kontostand"]

    # models
    try:
        model = load_model()
        model2 = load_model2()
    except OSError:
        model = TableModel(headers)
        model2 = TableModel2()

    # views
    view = Gui()
    view2 = Dialog()
    view3 = Dialog2()

    # set models
    view.tableView.setModel(model)
    view2.listView.setModel(model2)
    view.category.setModel(model2)
    view3.tableView.setModel(model2)

    # bindings
    view.add_data.clicked.connect(insert)
    view.delete_data.clicked.connect(remove)
    view.edit_data.clicked.connect(change)
    view.actionChange.triggered.connect(view2.show)
    view.actionSave.triggered.connect(save)
    view.actionBudget.triggered.connect(view3.show)
    view2.add_category.clicked.connect(insert2)
    view2.delete_category.clicked.connect(remove2)
    view2.Ok.clicked.connect(view2.close)
    view3.pushButton.clicked.connect(view3.close)

    view.show()

    sys.exit(app.exec_())
