# -*- coding: utf-8 -*-

import numpy as np



def compute(sensitivity,springConstant,radius,T_front_list,T_back_list,M_front_list,M_back_list,V_front_list,V_back_list):

    f1=np.polyfit(T_front_list,M_front_list,1)

    f2=np.polyfit(T_back_list,M_back_list,1)

    y1=np.polyfit(T_front_list,V_front_list,1)

    y2=np.polyfit(T_back_list,V_back_list,1)

    M1 = f1[0]

    M2 = f2[0]

    V1 = y1[0]

    V2 = y2[0]

    E=0.75*(1/((abs((M2-M1)/(V2-V1))/sensitivity)-1)*springConstant/(2*radius))

    return E



