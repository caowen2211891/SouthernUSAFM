# -*- coding: utf-8 -*-
from PyQt5.QtGui import QIcon

from PyQt5.QtWidgets import QHeaderView, QTableWidgetItem, QAbstractItemView, QTableView, QDialog
from PyQt5.QtCore import pyqtSignal

from Ui_Result import Ui_Form


class RusultDailog(QDialog,Ui_Form):

    resultSignal = pyqtSignal(dict)

    def __init__(self,parent,items):
        super(RusultDailog,self).__init__(parent)
        self.items = items
        self.org = items.copy()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowIcon (QIcon('res/pic/test.png'))
        self.tableWidget.setColumnCount(2)
        
        self.tableWidget.setHorizontalHeaderLabels(['Filename','Result'])

        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tableWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setEditTriggers(QTableView.NoEditTriggers)
        # self.tableWidget.setContextMenuPolicy()
        self.setItem()

        self.buttonBox.accepted.connect(self.ok)
        self.buttonBox.rejected.connect(self.cancel)
        self.deleted.clicked.connect(self.delete)
        self.setWindowTitle('result')

    def setItem(self):
        l = len(self.items)
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(l)
        i = 0
        for key,values in  self.items.items():
            keyitem = QTableWidgetItem(str(key))
            valuesitem = QTableWidgetItem(str(values.es))
            self.tableWidget.setItem(i,0,keyitem)
            self.tableWidget.setItem(i,1,valuesitem)
            i = i+1

    def cancel(self):
        self.close()
        self.resultSignal.emit(self.org)

    def delete(self):
        datas = self.tableWidget.selectedItems()
        for i in datas:
            r = self.tableWidget.indexFromItem(i).row()
            key = self.tableWidget.item(r, 0).text()
            if key in self.items.keys():
                self.items.pop(key)
        self.setItem()

    def ok(self):
        self.resultSignal.emit(self.items)
        self.close()
