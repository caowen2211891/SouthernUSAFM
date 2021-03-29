# -*- coding: utf-8 -*-



class Detail(object):
    def __init__(self,h,pk,er,s,es,pu,hu,hc,ac,r):
        super(Detail, self).__init__()
        self.h = h
        self.s = s
        self.es = es
        self.pu = pu
        self.hu = hu
        self.hc = hc
        self.ac = ac
        self.r = r
        self.pk = pk
        self.er = er

class ResultData(object):

    """docstring for SuccessData"""

    def __init__(self,filename,retractindex,sensitivity,springConstant,beforeIndext = None,afterIndex= None,E = None):

        super(ResultData, self).__init__()
        self.filename = filename
        self.retractindex = retractindex
        self.sensitivity = sensitivity
        self.springConstant = springConstant
        self.beforeIndext = beforeIndext
        self.afterIndex = afterIndex
        self.E = E

class InputParamsData(object):

    def __init__(self,PRSample= None,PRTip= None,Etip= None,TipModel= None):
        super(InputParamsData, self).__init__()
        self.PRSample = PRSample
        self.PRTip = PRTip
        self.Etip = Etip
        self.TipModel = TipModel
        self.c1 = None
        self.c2 = None
        self.c3 = None
        self.c4 = None
        self.radius = None
    
    def setc1c2c3c4(self,c1,c2,c3,c4):
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.c4 = c4

    def setradius(self,radius):
        self.radius = radius

class TableItem(object):

    def __init__(self,filename,detail = None,resultData = None,inputParamsData = None):
        super(TableItem, self).__init__()
        self.filename = filename
        self.detail = detail
        self.resultData = resultData
        self.inputParamsData = inputParamsData
