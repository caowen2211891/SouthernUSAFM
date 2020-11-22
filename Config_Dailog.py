# -*- coding: utf-8 -*-
from PyQt5.QtGui import QIcon, QDoubleValidator

from Ui_Config import Ui_Form

import numpy as np
from PyQt5.QtWidgets import QColorDialog, QDialog

from SoftConfig import ConfigData


class ConfigDailog(QDialog,Ui_Form):
    splitData = {'Space':' ','Tab':'\t',',':',',';':';'}
    colorData = {}
    color = '#000000'


    t = 0
    al = 0
    id = 0

    def __init__(self,parent):
        super(ConfigDailog,self).__init__(parent)
        self.cf = ConfigData()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowIcon (QIcon('res/pic/test.png'))
        self.showSplit()
        if self.cf.isCustomSplit():
            self.custom_split.setChecked(True)
            self.spilt.setText(self.cf.getDefalutSplit())
            self.split_comboBox.setEnabled(False)
        else:
            self.custom_split.setChecked(False)
            self.spilt.setEnabled(False)
            text = self.cf.getDefalutSplit()
            if text == ' ':
                self.split_comboBox.setCurrentText('Space')
            elif text == '\t':
                self.split_comboBox.setCurrentText('Tab')
            else:
                self.split_comboBox.setCurrentText(text)

        self.custom_split.stateChanged.connect(self.splitchange)

        for index in range(20):
            self.t_comboBox.addItem(str(index+1))
            self.al_comboBox.addItem(str(index+1))
            self.id_comboBox.addItem(str(index+1))

        self.t_comboBox.setCurrentIndex(self.cf.getTimeColumn())
        self.al_comboBox.setCurrentIndex(self.cf.getFdColumn())
        self.id_comboBox.setCurrentIndex(self.cf.getHeightColumn())
        self.t_unitcomboBox.setCurrentText(self.cf.getTimeUnit())
        self.al_unitcomboBox.setCurrentText(self.cf.getFdUnit())
        self.id_unitcomboBox.setCurrentText(self.cf.getHeightUnit())
        if self.cf.getFdUnit() == 'uV' or self.cf.getFdUnit() == 'V':
            self.SpringConstantEdit.setEnabled(True)
            self.SensitivityEdit.setEnabled(True)
        else :
            self.SpringConstantEdit.setEnabled(False)
            self.SensitivityEdit.setEnabled(False)
        
        self.al_unitcomboBox.currentTextChanged.connect(self.on_al_unitcomboBox_select)

        self.colorData['DataLine'] = self.cf.getDataLineColor()
        self.colorData['RetractPoint'] = self.cf.getRetractPointColor()
        self.colorData['SmoothLine'] = self.cf.getSmoothLineColor()
        self.colorData['CountPoint'] = self.cf.getCountPointColor()
        self.showColor()
        self.color = self.cf.getDataLineColor()
        self.colorButton.setStyleSheet('QWidget {background-color:%s}'%self.color)
        self.colorButton.clicked.connect(self.colorClick)
        self.color_comboBox.currentTextChanged.connect(self.colorchange)

        self.time_coefficient_edit.setText(self.cf.getTimeCoefficient())
        self.applied_coefficient_edit.setText(self.cf.getAppliedCoefficient())
        self.indentation_coefficient_edit.setText(self.cf.getIndentationCoefficient())
        self.SpringConstantEdit.setText(self.cf.getSpringConstant())
        self.SensitivityEdit.setText(self.cf.getSensitivity())
        self.time_coefficient_edit.setValidator(QDoubleValidator())
        self.applied_coefficient_edit.setValidator(QDoubleValidator())
        self.indentation_coefficient_edit.setValidator(QDoubleValidator())
        self.SpringConstantEdit.setValidator(QDoubleValidator())
        self.SensitivityEdit.setValidator(QDoubleValidator())

        self.buttonBox.accepted.connect(self.ok)
        self.buttonBox.rejected.connect(self.cancel)
        # self.exec()

    def colorchange(self,text):
        if text == 'DataLine':
            self.colorButton.setStyleSheet('QWidget {background-color:%s}' % self.cf.getDataLineColor())
        elif text == 'RetractPoint':
            self.colorButton.setStyleSheet('QWidget {background-color:%s}' % self.cf.getRetractPointColor())
        elif text == 'SmoothLine':
            self.colorButton.setStyleSheet('QWidget {background-color:%s}' % self.cf.getSmoothLineColor())
        elif text == 'CountPoint':
            self.colorButton.setStyleSheet('QWidget {background-color:%s}' % self.cf.getCountPointColor())

    def on_al_unitcomboBox_select(self,arg):
        if arg == 'uV' or arg == 'V':
            self.SpringConstantEdit.setEnabled(True)
            self.SensitivityEdit.setEnabled(True)
        else:
            self.SpringConstantEdit.setEnabled(False)
            self.SensitivityEdit.setEnabled(False)

    def colorClick(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.colorButton.setStyleSheet('QWidget {background-color:%s}' % col.name())
            self.colorData[self.color_comboBox.currentText()] = col.name()


    def cancel(self):
        self.close()

    def splitchange(self,btn):
        if btn == 0:
            self.spilt.setEnabled(False)
            self.split_comboBox.setEnabled(True)
        elif btn == 2:
            self.spilt.setEnabled(True)
            self.split_comboBox.setEnabled(False)

    def showColor(self):
        self.color_comboBox.clear()
        for key in self.colorData:
            self.color_comboBox.addItem(key)

    def showSplit(self):
        self.split_comboBox.clear()
        for key in self.splitData:
            self.split_comboBox.addItem(key)


    def ok(self):
        if self.custom_split.checkState() == 2:
            self.cf.setCustomSplit(True)
            self.cf.setDefalutSplit(self.spilt.text())
        else:
            self.cf.setCustomSplit(False)
            self.cf.setDefalutSplit(self.splitData[self.split_comboBox.currentText()])

        self.cf.setTimeColumn(self.t_comboBox.currentIndex())
        self.cf.setFdColumn(self.al_comboBox.currentIndex())
        self.cf.setHeightColumn(self.id_comboBox.currentIndex())
        self.cf.setTimeUnit(self.t_unitcomboBox.currentText())
        self.cf.setFdUnit(self.al_unitcomboBox.currentText())
        self.cf.setHeightUnit(self.id_unitcomboBox.currentText())

        self.cf.setDataLineColor(self.colorData['DataLine'])
        self.cf.setRetractPointColor(self.colorData['RetractPoint'])
        self.cf.setSmoothLineColor(self.colorData['SmoothLine'])
        self.cf.setCountPointColor(self.colorData['CountPoint'])

        self.cf.setTimeCoefficient(str(np.array(self.time_coefficient_edit.text(), dtype=np.float64)))
        self.cf.setAppliedCoefficient(str(np.array(self.applied_coefficient_edit.text(), dtype=np.float64)))
        self.cf.setIndentationCoefficient(str(np.array(self.indentation_coefficient_edit.text(), dtype=np.float64)))
        self.cf.setSpringConstant(str(np.array(self.SpringConstantEdit.text(), dtype=np.float64)))
        self.cf.setSensitivity(str(np.array(self.SensitivityEdit.text(), dtype=np.float64)))


        self.cf.setAsDefault(True)
        self.cancel()

    