# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_Detail.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(345, 206)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label_hc = QtWidgets.QLabel(Dialog)
        self.label_hc.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.label_hc.setObjectName("label_hc")
        self.gridLayout.addWidget(self.label_hc, 6, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 5, 0, 1, 1)
        self.label_ac = QtWidgets.QLabel(Dialog)
        self.label_ac.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.label_ac.setObjectName("label_ac")
        self.gridLayout.addWidget(self.label_ac, 5, 1, 1, 1)
        self.label_hu = QtWidgets.QLabel(Dialog)
        self.label_hu.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.label_hu.setObjectName("label_hu")
        self.gridLayout.addWidget(self.label_hu, 3, 1, 1, 1)
        self.label_pu = QtWidgets.QLabel(Dialog)
        self.label_pu.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.label_pu.setObjectName("label_pu")
        self.gridLayout.addWidget(self.label_pu, 2, 1, 1, 1)
        self.label_es = QtWidgets.QLabel(Dialog)
        self.label_es.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.label_es.setObjectName("label_es")
        self.gridLayout.addWidget(self.label_es, 4, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 3, 0, 1, 1)
        self.label_h = QtWidgets.QLabel(Dialog)
        self.label_h.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.label_h.setObjectName("label_h")
        self.gridLayout.addWidget(self.label_h, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_s = QtWidgets.QLabel(Dialog)
        self.label_s.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.label_s.setObjectName("label_s")
        self.gridLayout.addWidget(self.label_s, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 7, 0, 1, 1)
        self.label_r = QtWidgets.QLabel(Dialog)
        self.label_r.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.label_r.setObjectName("label_r")
        self.gridLayout.addWidget(self.label_r, 7, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_hc.setText(_translate("Dialog", "0"))
        self.label_5.setText(_translate("Dialog", "hc"))
        self.label_13.setText(_translate("Dialog", "Ac"))
        self.label_ac.setText(_translate("Dialog", "0"))
        self.label_hu.setText(_translate("Dialog", "0"))
        self.label_pu.setText(_translate("Dialog", "0"))
        self.label_es.setText(_translate("Dialog", "0"))
        self.label_9.setText(_translate("Dialog", "Pu"))
        self.label_7.setText(_translate("Dialog", "Es"))
        self.label.setText(_translate("Dialog", "H"))
        self.label_11.setText(_translate("Dialog", "Hu"))
        self.label_h.setText(_translate("Dialog", "0"))
        self.label_2.setText(_translate("Dialog", "S"))
        self.label_s.setText(_translate("Dialog", "0"))
        self.label_3.setText(_translate("Dialog", "R"))
        self.label_r.setText(_translate("Dialog", "0"))

