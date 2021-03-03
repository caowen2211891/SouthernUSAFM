# -*- coding: utf-8 -*-

import linecache
import chardet
import numpy as np
import pandas as pd
import FileWriter
import os
from SoftConfig import ConfigData

from datetime import datetime
import time
from decimal import Decimal


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

def getEncode(fname):
    with open(fname,'rb') as fo:
        encode = chardet.detect(fo.readline())['encoding']
    return encode

def getTxTFileMaySpstr(fname):
    encode = getEncode(fname)
    df = pd.read_csv(fname,sep='@',error_bad_lines=False,header=None,encoding=encode).dropna()
    floatReg = "(\\-|\\+)?\\d+(\\.\\d+)?"
    floatRegs= [floatReg,floatReg,floatReg]
    tab= df[df[0].str.contains('\t'.join(floatRegs))]
    space = df[df[0].str.contains(' '.join(floatRegs))]
    if tab.shape[0] > 50:
        return '\t'
    elif space.shape[0] > 50:
        return ' '
    return False

def mayShouldChangeSpstr(fname,result):
    if fname.endswith('.txt'):
        maySpstr = getTxTFileMaySpstr(fname)
        if cf.getDefalutSplit() == '\t' and maySpstr == ' ':
            result[0] = '\t'
            result[1] = maySpstr
            return True
        elif cf.getDefalutSplit() == ' ' and maySpstr == '\t':
            result[0] = ' '
            result[1] = maySpstr
            return True
    return False

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
            start = datetime.now()

            if fname.endswith('.xlsx') or fname.endswith('.xls'):
                df = pd.read_excel(fname,header=None).dropna()
                sensitivity_df = df[df[0].str.contains("sensitivity")]
                if sensitivity_df.shape[0] > 0:
                    sensitivity = getFirstNumber(sensitivity_df.iloc[0,0])
                springconstant_df = df[df[0].str.contains("springConstant")]
                if springconstant_df.shape[0] > 0:
                    springConstant = getFirstNumber(springconstant_df.iloc[0,0])
                
                df = pd.read_excel(fname,header=None,usecols=[m_index, v_index,s_index])
                data = df.apply(pd.to_numeric, errors='coerce').dropna(how='any')
                m_back_list = np.array(data[m_index] * m_unit, dtype=np.float64)*indentationCoefficient
                V_back_list = np.array(data[v_index] * v_unit, dtype=np.float64)*appliedCoefficient
                T_back_list = np.array(data[s_index] * s_unit, dtype=np.float64)*timeCoefficient

            elif fname.endswith('.txt'):
                encode = getEncode(fname)
                df = pd.read_csv(fname,sep='@',error_bad_lines=False,header=None,encoding=encode).dropna()
                sensitivity_df = df[df[0].str.contains("sensitivity")]
                if sensitivity_df.shape[0] > 0:
                    sensitivity = getFirstNumber(sensitivity_df.iloc[0,0])
                springconstant_df = df[df[0].str.contains("springConstant")]
                if springconstant_df.shape[0] > 0:
                    springConstant = getFirstNumber(springconstant_df.iloc[0,0])
                    
                df = pd.read_csv(fname,sep=cf.getDefalutSplit(),error_bad_lines=False,header=None,encoding=encode)
                data = df.apply(pd.to_numeric, errors='coerce').dropna(how='any')
                m_back_list = np.array(data[m_index] * m_unit, dtype=np.float64)*indentationCoefficient
                V_back_list = np.array(data[v_index] * v_unit, dtype=np.float64)*appliedCoefficient
                T_back_list = np.array(data[s_index] * s_unit, dtype=np.float64)*timeCoefficient
            else:
                print("not support")
            print("cost: "+str(datetime.now() - start) + "")
            Datas.append(SuccessData(n, retracttime, sensitivity, springConstant, m_back_list, V_back_list, T_back_list,
                                     last_retract_index))
        except Exception as e:
            print(e)
            fileinfo = fileinfo + str(e)
        FileWriter.write_log_info(fname,fileinfo)
    return Datas
