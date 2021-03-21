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
        self.label_h.setText(str(self.detail.h) if hasattr(self.detail,'h') else 'None') 
        self.label_s.setText(str(self.detail.s) if hasattr(self.detail,'s') else 'None') 
        self.label_pu.setText(str(self.detail.pu) if hasattr(self.detail,'pu') else 'None') 
        self.label_hu.setText(str(self.detail.hu) if hasattr(self.detail,'hu') else 'None') 
        self.label_es.setText(str(self.detail.es) if hasattr(self.detail,'es') else 'None') 
        self.label_ac.setText(str(self.detail.ac) if hasattr(self.detail,'ac') else 'None') 
        self.label_hc.setText(str(self.detail.hc) if hasattr(self.detail,'hc') else 'None') 
        self.label_r.setText(str(self.detail.r) if hasattr(self.detail,'r') else 'None') 
        self.label_pk.setText(str(self.detail.pk) if hasattr(self.detail,'pk') else 'None') 
        self.label_er.setText(str(self.detail.er) if hasattr(self.detail,'er') else 'None') 


