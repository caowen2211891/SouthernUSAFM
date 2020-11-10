# -*- coding: utf-8 -*-
import os
import datetime

id_debug = False

def log(str):
    if id_debug:
        print(str)

def mkdir(path):

    folder = os.path.exists(path)

    if not folder:                   #判断是否存在文件夹如果不存在则创建为文件夹

        os.makedirs(path)            #makedirs 创建文件时如果路径不存在会创建这个路径

def mkcrashfile(path):

    current_path = os.path.abspath(path)

    father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")

    crash_path = father_path + os.path.sep + 'log'

    mkdir(crash_path) 

    # datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

    # os.mknod(father_path)

    return crash_path

def mkzz1file(filename):

#     zz1 = os.path.exists(filename)

#     if zz1:

#         os.remove(filename)

    ZZ1file = open(filename,'a+')

    return ZZ1file



def write_format(file,name,edata):

    if (edata > 0):
        file.write(name + '   %.7e' % (edata))
    else:   
        file.write(name + '  %.7e' % (edata))
        
def write_log_info(filename,logInfo):

    current_path = os.path.abspath(filename)

    father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")

    info_path = father_path + os.path.sep + 'dataInfo'

    mkdir(info_path) 

    filename = info_path + os.path.sep + os.path.basename(filename) + '_info.txt'

    info = open(filename,'w+')

    info.write(logInfo)

    info.close()

def write(filename,datas):

    ZZ1file = mkzz1file(filename)

    for key,values in  datas.items():
        write_format(ZZ1file,key,values.es)
        ZZ1file.write('\n')

    ZZ1file.close()

