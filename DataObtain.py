# -*- coding: utf-8 -*-

import linecache

import numpy as np
import pandas as pd

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

def getData(files):
    list = files
    # 返回的左下列表的数据
    Datas = []
    length = len(list)
    if length<=0:
        return Datas
    for n in range(len(list)):
        try:
            retracttime = -1
            last_retract_index = -1
            T_back_list = []
            m_back_list = []
            V_back_list = []
            sensitivity = -1
            springConstant = -1
            m_index = cf.getHeightColumn()
            v_index = cf.getFdColumn()
            s_index = cf.getTimeColumn()

            m_unit = cf.getHeightUnitNo()
            v_unit = cf.getFDUnitNo()
            s_unit = cf.getTimeUnitNo()
            fname = list[n]
            if fname.endswith('.txt'):
                lines = linecache.getlines(fname)
                line_len = len(lines)
                for i in range(line_len):
                    values = lines[i].split(cf.getDefalutSplit())
                    try:
                        m_back_data = np.array(values[m_index], dtype=np.float64)
                        V_back_data = np.array(values[v_index], dtype=np.float64)
                        T_back_data = np.array(values[s_index], dtype=np.float64)
                        m_back_list.append(m_back_data * m_unit)
                        V_back_list.append(V_back_data * v_unit)
                        T_back_list.append(T_back_data * s_unit)
                    except Exception as e1:
                        print(e1)
            elif fname.endswith('.xlsx'):
                df = pd.read_excel(fname,header=None,usecols=[m_index, v_index,s_index])
                data = df.apply(pd.to_numeric, errors='coerce').dropna(how='any')
                m_back_list = np.array(data[m_index] * m_unit, dtype=np.float64)
                V_back_list = np.array(data[v_index] * v_unit, dtype=np.float64)
                T_back_list = np.array(data[s_index] * s_unit, dtype=np.float64)
            Datas.append(SuccessData(n, retracttime, sensitivity, springConstant, m_back_list, V_back_list, T_back_list,
                                     last_retract_index))
        except Exception as e:
            print(e)
    return Datas


