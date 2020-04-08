# -*- coding: utf-8 -*-
""" Created on Tue Sep 12 08:36:42 2017

@author: Saike Tian """

import sdds
import os
import sys
import platform
import subprocess
import numpy as np

# Check the Python Version
ver = platform.architecture()[0]
ver_python = platform.python_version()

if ver == '64bit':
    if ver_python[0:3] == '3.7':
        sys.path.append(r'D:\IHEPBox\python_def\SDDSPython3.7-x64\DLLs')
        sys.path.append(r'D:\IHEPBox\python_def\SDDSPython3.7-x64\Lib')
        sys.path.append(r'D:\IHEPBox\python_def\SDDSPython3.7-x64\SDDS_demo')
    else:
        sys.path.append(r'D:\IHEPBox\python_def\SDDSPython3.8-x64\DLLs')
        sys.path.append(r'D:\IHEPBox\python_def\SDDSPython3.8-x64\Lib')
        sys.path.append(r'D:\IHEPBox\python_def\SDDSPython3.8-x64\SDDS_demo')
else:
    if ver_python[0:3] == '3.7':
        sys.path.append(r'D:\IHEPBox\python_def\SDDSPython3.7\DLLs')
        sys.path.append(r'D:\IHEPBox\python_def\SDDSPython3.7\Lib')
        sys.path.append(r'D:\IHEPBox\python_def\SDDSPython3.7\SDDS_demo')
    else:
        sys.path.append(r'D:\IHEPBox\python_def\SDDSPython3.8\DLLs')
        sys.path.append(r'D:\IHEPBox\python_def\SDDSPython3.8\Lib')
        sys.path.append(r'D:\IHEPBox\python_def\SDDSPython3.8\SDDS_demo')


def col(filename, column, page=1):

    steam = os.popen('sdds2stream -col=%s -page=%int %s' %
                     (column, page, filename))
    transfer = steam.read().split('\n')
    col_data = [float(x) for x in transfer if x]
    return col_data


def par(filename, parameter, page=1):
    try:
        par_data = subprocess.run(
            'sdds2stream -par=%s -page=%int %s' % (parameter, page, filename))
        par_data = float(par_data)
    except:
        steam = os.popen('sdds2stream -par=%s -page=%int %s' %
                         (parameter, page, filename))
        transfer = steam.read()
        par_data = float(transfer)
    return par_data


def col_page(filename, column, page=1):
    temp = sdds.SDDS(0)
    temp.load(filename)
    # temp.columnData[column_index][page]
    col_data = temp.columnData[temp.columnName.index(column)]
    col_data_temp = np.array(col_data)
    return col_data_temp[page-1]


def par_page(filename, parameter, page=1):
    temp = sdds.SDDS(0)
    temp.load(filename)
    par_data = temp.parameterData[temp.parameterName.index(parameter)]
    par_data_temp = np.array(par_data)
    return par_data_temp[page-1]
