# -*- coding: utf-8 -*-

from PyQt5.QtCore import QSettings


class ConfigData(object):

    settings = QSettings("soft","config")


    def setDefalutSplit(self,split):
        self.settings.setValue('splitdef', split)

    def getDefalutSplit(self):
        return self.settings.value('splitdef', ' ')

    def isCustomSplit(self):
        return str(self.settings.value('cusp',False)).lower() == 'true'

    def setCustomSplit(self,isfd):
        self.settings.setValue('cusp', isfd)

    def getTimeColumn(self):
        return self.settings.value('t_c', 0)

    def setTimeColumn(self,column):
        self.settings.setValue('t_c', column)

    def getHeightColumn(self):
        return self.settings.value('h_c', 0)

    def setHeightColumn(self,column):
        self.settings.setValue('h_c', column)

    def getFdColumn(self):
        return self.settings.value('fd_c', 0)

    def setFdColumn(self,column):
        self.settings.setValue('fd_c', column)

    def getTimeUnit(self):
        return self.settings.value('t_u', 's')

    def setTimeUnit(self,column):
        self.settings.setValue('t_u', column)

    def getHeightUnit(self):
        return self.settings.value('h_u', 'm')

    def getHeightUnitNo(self):
        unit = self.getHeightUnit()
        if unit == 'm':
            return 1
        elif unit == 'cm':
            return 1e-2
        elif unit == 'mm':
            return 1e-3
        elif unit == 'um':
            return 1e-6
        elif unit == 'nm':
            return 1e-9

    def getTimeUnitNo(self):
        unit = self.getTimeUnit()
        if unit == 's':
            return 1
        elif unit == 'ms':
            return 1e-3

    def getFDUnitNo(self):
        unit = self.getFdUnit()
        if unit == 'N':
            return 1
        elif unit == 'uN':
            return 1e-6



    def setHeightUnit(self,column):
        self.settings.setValue('h_u', column)

    def getFdUnit(self):
        return self.settings.value('fd_u', 'N')

    def setFdUnit(self,column):
        self.settings.setValue('fd_u', column)

    def isAsDefault(self):
        return str(self.settings.value('as_d', False)).lower() == 'true'

    def setAsDefault(self,isdefault):
        self.settings.setValue('as_d', isdefault)

    def getDataLineColor(self):
        return self.settings.value('color_dataline', "#4ee2ff")

    def setDataLineColor(self,color):
        self.settings.setValue('color_dataline', color)

    def getRetractPointColor(self):
        return self.settings.value('color_retractpoint', "#ff0000")

    def setRetractPointColor(self,color):
        self.settings.setValue('color_retractpoint', color)

    def getSmoothLineColor(self):
        return self.settings.value('color_smoothline', "#00ff00")

    def setSmoothLineColor(self,color):
        self.settings.setValue('color_smoothline', color)

    def getCountPointColor(self):
        return self.settings.value('color_countpoint', "#bc35ff")

    def setCountPointColor(self,color):
        self.settings.setValue('color_countpoint', color)




