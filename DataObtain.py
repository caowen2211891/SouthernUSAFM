# -*- coding: utf-8 -*-

import linecache

import numpy as np
import pandas as pd
import FileWriter
import os
from SoftConfig import ConfigData


class SuccessData(object):

    """docstring for SuccessData"""

    def __init__(self,n,retracttime,sensitivity,springConstant,m_back_list,V_back_list,T_back_list,last_retract_index):

        super(SuccessData, self).__init__()

        self.position = n

        self.retracttime = retracttime

        self.sensitivity = sensitivity

        self.springConstant = springConstant

        self.m_list = m_back_list

        self.V_list = V_back_list

        self.T_list = T_back_list

        self.retract_index = last_retract_index

cf = ConfigData()

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False

def getFirstNumber(s):
    l = s.split(' ')
    for i in l:
        if is_number(i):
            return i
    return -1

# def backProgress(callback):
#     if()

def getData(files):
    list = files
    # 返回的左下列表的数据
    Datas = []
    length = len(list)
    if length<=0:
        return Datas

    ##indentation
    m_index = cf.getHeightColumn()
    ##applied
    v_index = cf.getFdColumn()
    ##time
    s_index = cf.getTimeColumn()

    m_unit = cf.getHeightUnitNo()
    v_unit = cf.getFDUnitNo()
    s_unit = cf.getTimeUnitNo()

    timeCoefficient = np.array(cf.getTimeCoefficient(), dtype=np.float64)
    appliedCoefficient = np.array(cf.getAppliedCoefficient(), dtype=np.float64)
    indentationCoefficient = np.array(cf.getIndentationCoefficient(), dtype=np.float64)
    print("Completed",0,"%")
    for n in range(len(list)):
        fname = list[n]
        fileinfo = 'file: ' + os.path.basename(fname)+ '\n'
        fileinfo = fileinfo + 'settings: '+ '\n'
        fileinfo = fileinfo+ "%-20s\t\t%-20s\t\t%-20s\t\t%-20s\n"%("type","index","Coefficient","unit")+"-" * 50
        fileinfo = fileinfo+'\n'
        fileinfo = fileinfo+ "%-20s\t\t%-20s\t\t%-20s\t\t%-20s\n"%("time",str(s_index+1),str(timeCoefficient),str(cf.getTimeUnit()))
        fileinfo = fileinfo+ "%-20s\t\t%-20s\t\t%-20s\t\t%-20s\n"%("applied",str(v_index+1),str(appliedCoefficient),str(cf.getFdUnit()))
        fileinfo = fileinfo+ "%-20s\t\t%-20s\t\t%-20s\t\t%-20s\n"%("indentation",str(m_index+1),str(indentationCoefficient),str(cf.getHeightUnit()))
        spstr = cf.getDefalutSplit()
        if spstr == ' ':
            spstr = 'Space'
        elif spstr == '\t':
            spstr ='Tab'
        fileinfo = fileinfo + '\nsplit by: '+ spstr + '\n\n\n'
        try:
            retracttime = -1
            last_retract_index = -1
            T_back_list = []
            m_back_list = []
            V_back_list = []
            sensitivity = -1
            springConstant = -1

            if fname.endswith('.txt'):
                lines = linecache.getlines(fname)
                line_len = len(lines)
                for i in range(line_len):
                    linedata = lines[i].lower()
                    if sensitivity == -1 and 'sensitivity' in linedata:
                        sensitivity = getFirstNumber(linedata)
                    if springConstant == -1 and 'springconstant' in linedata:
                        springConstant = getFirstNumber(linedata)
                    values = linedata.split(cf.getDefalutSplit())
                    try:
                        m_back_data = np.array(values[m_index], dtype=np.float64) *indentationCoefficient
                        V_back_data = np.array(values[v_index], dtype=np.float64) *appliedCoefficient
                        T_back_data = np.array(values[s_index], dtype=np.float64) *timeCoefficient
                        m_back_list.append(m_back_data * m_unit)
                        V_back_list.append(V_back_data * v_unit)
                        T_back_list.append(T_back_data * s_unit)
                    except Exception as e1:
                        fileinfo = fileinfo + 'line ' + str(i+1) + ' ' + lines[i] + ' cause:' + str(e1) + '\n' 
                    if i%1 == 0 or i==line_len:
                        print("Completed",int(round(float(i)/line_len * 100)),"%")
            elif fname.endswith('.xlsx') or fname.endswith('.xls'):
                lines_number = sum(1 for line in open(fname))
                lines_in_chunk = 10 # I don't know what size is better
                counter = 0
                completed = 0
                df = pd.read_excel(fname,chunksize=lines_in_chunk,header=None,usecols=[m_index, v_index,s_index])
                for chunk in df:
                    counter += lines_in_chunk
                    new_completed = int(round(float(counter)/lines_number * 100))
                    if (new_completed > completed): 
                        completed = new_completed
                        print("Completed",completed,"%")
                data = df.apply(pd.to_numeric, errors='coerce').dropna(how='any')
                m_back_list = np.array(data[m_index] * m_unit, dtype=np.float64)*indentationCoefficient
                V_back_list = np.array(data[v_index] * v_unit, dtype=np.float64)*appliedCoefficient
                T_back_list = np.array(data[s_index] * s_unit, dtype=np.float64)*timeCoefficient
            Datas.append(SuccessData(n, retracttime, sensitivity, springConstant, m_back_list, V_back_list, T_back_list,
                                     last_retract_index))
        except Exception as e:
            print(e)
            fileinfo = fileinfo + str(e)
        FileWriter.write_log_info(fname,fileinfo)
    return Datas
