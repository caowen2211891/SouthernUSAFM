# -*- coding: utf-8 -*-
from PyQt5.QtGui import QIcon

from PyQt5.QtWidgets import QWidget,QToolButton,QHBoxLayout,QHeaderView, QTableWidgetItem, QAbstractItemView, QTableView, QDialog,QPushButton
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
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setHorizontalHeaderLabels(['Filename','Result'])
        self.tableWidget.horizontalHeader().setVisible(False)
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

    def updateTable(self,id):
        print(id)

    def buttonForRow(self,id):
        widget=QWidget()
        # 修改
        updateBtn = QToolButton(self)
        # updateBtn.setToolButtonStyle(Qt.ToolButtonIconOnly)
        updateBtn.setIcon(QIcon('res/pic/plus.png'))
        updateBtn.clicked.connect(lambda:self.updateTable(id))

        # 查看
        viewBtn = QPushButton('查看')
        

        viewBtn.clicked.connect(lambda: self.updateTable(id))

        # 删除
        deleteBtn = QPushButton('-')
        deleteBtn.clicked.connect(lambda:self.updateTable(id))


        hLayout = QHBoxLayout()
        hLayout.addWidget(updateBtn)
        hLayout.addWidget(viewBtn)
        hLayout.addWidget(deleteBtn)
        hLayout.setContentsMargins(5,2,5,2)
        widget.setLayout(hLayout)
        return widget


    def setItem(self):
        l = len(self.items)
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(l)
        i = 0
        for key,values in  self.items.items():
            keyitem = QTableWidgetItem(str(key))
            valuesitem = QTableWidgetItem(str(values.es))
            self.tableWidget.setItem(i,0,keyitem)
            # self.tableWidget.setItem(i,1,valuesitem)
            self.tableWidget.setCellWidget(i, 1,self.buttonForRow(str(key)))
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
