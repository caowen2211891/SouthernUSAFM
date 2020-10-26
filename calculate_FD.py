# -*- coding: utf-8 -*-

import numpy as np




def computeS(T_front_list,T_back_list,M_front_list,M_back_list,V_front_list,V_back_list):

    f1=np.polyfit(T_front_list,M_front_list,1)

    f2=np.polyfit(T_back_list,M_back_list,1)

    y1=np.polyfit(T_front_list,V_front_list,1)

    y2=np.polyfit(T_back_list,V_back_list,1)
    # 位移-时间曲线卸载前
    M1 = f1[0]
    # 位移-时间曲线卸载后
    M2 = f2[0]
    # 力-时间曲线卸载前
    V1 = y1[0]
    # 力-时间曲线卸载后
    V2 = y2[0]

    s=abs((V2-V1)/(M2-M1))

    return s



