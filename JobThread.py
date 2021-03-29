# -*- coding: utf-8 -*-
from PyQt5.QtCore import pyqtSignal, QThread
import DataObtain
from DataBean import InputParamsData
import math
import calculate_FD

class WorkThread(QThread):
    trigger = pyqtSignal(int)
    successSignal = pyqtSignal(list)

    def __int__(self):
        super(WorkThread, self).__init__()

    def addData(self,listitems,callBack):
        self.listitems = listitems
        self.callBack = callBack

    def run(self):
        datas = DataObtain.getData(self.listitems,self.callBack)
        self.successSignal.emit(datas)

class CalculateThread(QThread):
    successSignal = pyqtSignal(list)
    def __int__(self):
        super(CalculateThread, self).__init__()

        # datas[-sourceData--fileName
        #                  --T_list
        #                  --m_list
        #                  --V_list
        #                  --beforeCount
        #                  --afterCount
        #                  --index
        #       -inputParamsData
        #       -resultmap
    def setCalculateData(self,datas):
        self.datas = datas
    
    def run(self):
        for data in self.datas:
            try:
                self.compute_s(data)
                self.compute_es(data)
                self.compute_h(data)
            except Exception as e:
                print(e)
        self.successSignal.emit(self.datas)
    
    def compute_s(self,data):
        sourceData = data['sourceData']
        resultmap = data['resultmap']
        index = sourceData['index']
        beforeCount = sourceData['beforeCount']
        afterCount = sourceData['afterCount']
        resultmap['pu'] = sourceData['V_list'][index]
        resultmap['hu'] = sourceData['m_list'][index]
        before = index - beforeCount
        after = index + afterCount
        if(after >= len(sourceData['T_list'])):
            after = len(sourceData['T_list'])-1
        if after <= 0:
            after = 0
        if(before < 0):
            before = 0
        if before == 0 or before == index or after == index:
            raise ValueError('Compute S Error ')
        resultmap['s'] = calculate_FD.computeS(
            sourceData['T_list'][before:index], sourceData['T_list'][index:after],
            sourceData['m_list'][before:index], sourceData['m_list'][index:after],
            sourceData['V_list'][before:index], sourceData['V_list'][index:after])


    def compute_es(self,data):
        # Es = (1 - PRsample ^ 2) / (1 / Er - PK）
        # compute pk
        # PK = (1 - PRtip ^ 2) / Etip
        inputParamsData = data['inputParamsData']
        resultmap = data['resultmap']
        PRtip = inputParamsData.PRTip
        Etip = inputParamsData.Etip
        pr = inputParamsData.PRSample
        TipModel = inputParamsData.TipModel
        if Etip == 0:
            raise ValueError('Param Etip Is 0 ')
        resultmap['pk'] = (1-PRtip**2)/Etip
        # compute er
        if TipModel == 0:
            # Er = 3.14159 ^ 0.5 * 0.5 * S / (Ac ^ 0.5)
            temp = 3.14159**0.5
            # Hc = Hu - 0.72 * Pu / S
            # Ac = C1hc ^ 2 + C2hc + C3hc ^ 0.5 + C4hc ^ 0.25
            resultmap['hc'] = resultmap['hu']-0.72*resultmap['pu']/resultmap['s']
            if resultmap['hc'] < 0:
                raise ValueError('Param Hc < 0')
            resultmap['ac'] = inputParamsData.c1*(resultmap['hc']**2)+inputParamsData.c2*resultmap['hc']+inputParamsData.c3*(resultmap['hc']**0.5)+inputParamsData.c4*(resultmap['hc']**0.25)
            tempac = resultmap['ac']**0.5
            if tempac == 0:
                raise ValueError('Param Ac Is 0')
            resultmap['er'] = temp*0.5*resultmap['s']/tempac
        elif TipModel == 1:
            # Er = S / (2 *（R * Hu） ^ 0.5)
            temp = (inputParamsData.radius*resultmap['hu'])**0.5
            if temp == 0:
                raise ValueError('Param radius or hu Is 0')
            resultmap['er'] = resultmap['s']/(2*temp)
        else:
            # Er = S / (2R)
            if inputParamsData.radius == 0:
                raise ValueError('Param radius Is 0')
            resultmap['er'] = resultmap['s']/(2 * inputParamsData.radius)
        # compute es
        if 1/resultmap['er']-resultmap['pk'] == 0:
            raise ValueError('Param er == pk')
        resultmap['es'] = (1 - pr**2)/(1/resultmap['er']-resultmap['pk'])
    
    def compute_h(self,data):
        inputParamsData = data['inputParamsData']
        resultmap = data['resultmap']
        TipModel = inputParamsData.TipModel
        if TipModel == 0:
            # H=Pu/Ac
            if math.isclose(resultmap['ac'],0e-9,rel_tol=1e-9):
                return
            resultmap['hh'] = resultmap['pu']/resultmap['ac']
        elif TipModel == 1:
            # H=Pu/(3.14159*R*hu)
            if math.isclose(inputParamsData.radius,0e-9,rel_tol=1e-9):
                return
            resultmap['hh'] = resultmap['pu']/(3.14159*inputParamsData.radius*resultmap['hu'])
        else:
            # H=Pu/(3.14159*R^2)
            if math.isclose(inputParamsData.radius,0e-9,rel_tol=1e-9):
                return
            resultmap['hh'] = resultmap['pu']/(3.14159 * (inputParamsData.radius**2))

