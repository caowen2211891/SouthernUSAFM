# -*- coding: utf-8 -*-
from PyQt5.QtGui import QMovie

from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import  Qt

from Ui_Loading import Ui_Dialog


class LoadingDailog(QDialog,Ui_Dialog):

    def __init__(self,parent):
        super(LoadingDailog,self).__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        # self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.gif = QMovie('res/gif/loading.gif')
        self.label.setMovie(self.gif)
        self.gif.start()
        self.label_2.setStyleSheet("background-color :white")

    def dataProgress(self,state,progress,cost,position,total,msg = None):
        if state == 1 or state == 100:
            text = str(progress) + " lines loaded,cost "+ str(cost) + " s" + "-" + str(position)+ "/"+ str(total)
            self.label_2.setText(text)

