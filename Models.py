from PyQt5 import QtCore
import pickle

COLUMN_COUNT = 5
COLUMN_COUNT2 = 3


class TableModel(QtCore.QAbstractTableModel):                       # Model for data
    def __init__(self, temp_headers):
        QtCore.QAbstractTableModel.__init__(self)
        self.__data = []
        self.__headers = temp_headers

    def save(self):
        data = self.__data
        pickle_out = open("Data/data.pickle", "wb")
        pickle.dump(data, pickle_out)
        pickle_out.close()

    def load(self, data):
        self.__data = data

    def rowCount(self, parent):
        return len(self.__data)

    def columnCount(self, parent):
        return COLUMN_COUNT

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            row = index.row()
            column = index.column()
            value = self.__data[row][column]
            return value

    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return self.__headers[section]

    def find_place(self, date):
        i = 0
        for row in self.__data:
            diff = self.__data[i][0].toJulianDay() - date.toJulianDay()
            if diff > 0:
                return i
            i += 1
        return i

    def insertRow(self, new_row, parent=QtCore.QModelIndex()):
        self.beginInsertRows(parent, len(self.__data), len(self.__data))
        if new_row[3].find(",") != -1:
            new_row[3] = new_row[3].replace(',', '.')
        if new_row[3] == "":
            new_row[3] = 0
        new_row[3] = float(new_row[3])

        row = self.find_place(new_row[0])
        new_row.append(0)
        self.__data.insert(row, new_row)
        self.updateCredit(row)
        self.endInsertRows()
        return True

    def removeRows(self, selected, parent=QtCore.QModelIndex()):
        if selected:
            for i in selected:
                row = selected[0].row()
                self.beginRemoveRows(parent, row, row)
                self.__data.pop(row)
                self.endRemoveRows()
                self.updateCredit(row)
            return True
        else:
            return False

    def changeCell(self, column, index, new_data):
        if new_data != "":
            row = index.row()
            if column == 3:
                if new_data.find(",") != -1:
                    new_data = new_data.replace(',', '.')
                new_data = float(new_data)
            self.__data[row][column] = new_data
            if column == 0:
                old_row = row
                row = self.find_place(new_data)
                self.__data.insert(row, self.__data[old_row])
                self.__data.pop(old_row+1)
            self.updateCredit(row)
            return True
        else:
            return False

    def updateCredit(self, row):
        for i in range(row, len(self.__data)):
            if self.__data[i][3] == "":
                self.__data[i][3] = 0
            if i == 0:
                self.__data[i][4] = self.__data[i][3]
            else:
                self.__data[i][4] = self.__data[i-1][4] + self.__data[i][3]
        self.dataChanged.emit(self.index(row, 0), self.index(len(self.__data), 4))

    """def today(self):
        index = self.__data.index(QtCore.QDate.currentDate())
        print(index)"""


class TableModel2(QtCore.QAbstractTableModel):                     # Model for Kategorien and Budget
    def __init__(self):
        QtCore.QAbstractTableModel.__init__(self)
        self.__data = []

    def save(self):
        pickle_out = open("Data/category.pickle", "wb")
        pickle.dump(self.__data, pickle_out)
        pickle_out.close()

    def load(self, data):
        self.__data = data

    def rowCount(self, parent):
        return len(self.__data)

    def columnCount(self, parent):
        return COLUMN_COUNT2

    def data(self, index, role):
        if role == QtCore.Qt.EditRole:
            value = self.__data[index.row()][index.column()]
            return value

        if role == QtCore.Qt.DisplayRole:
            value = self.__data[index.row()][index.column()]
            return value

    def flags(self, index):
        return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        if role == QtCore.Qt.EditRole:
            if value:
                row = index.row()
                column = index.column()
                self.__data[row][column] = value
                self.dataChanged.emit(index, index)
                return True
            return False

    def insertRow(self, parent=QtCore.QModelIndex()):
        self.beginInsertRows(parent, len(self.__data), len(self.__data))
        self.__data.append(["Neue Kategorie",0,0])
        self.endInsertRows()
        return True

    def removeRow(self, x, parent=QtCore.QModelIndex()):
        if x:
            self.beginRemoveRows(parent, x[0].row(), x[-1].row())
            for i in x:
                self.__data.pop(x[0].row())
            self.endRemoveRows()
            return True
        else:
            return False

        # TODO: einnahme, ausgabe
