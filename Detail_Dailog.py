# -*- coding: utf-8 -*-
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog

from DataBean import Detail
from Ui_Detail import Ui_Dialog


class DetailDailog(QDialog,Ui_Dialog):

    def __init__(self,parent,detail:Detail):
        super(DetailDailog,self).__init__(parent)
        self.detail = detail
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowIcon(QIcon('res/pic/test.png'))
        self.setWindowTitle('Detail')
        self.label_h.setText(str(self.detail.h))
        self.label_s.setText(str(self.detail.s))
        self.label_pu.setText(str(self.detail.pu))
        self.label_hu.setText(str(self.detail.hu))
        self.label_es.setText(str(self.detail.es))
        self.label_ac.setText(str(self.detail.ac))
        self.label_hc.setText(str(self.detail.hc))
        self.label_r.setText(str(self.detail.r))


