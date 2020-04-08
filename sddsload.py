# -*- coding: utf-8 -*-
""" Created on Tue Sep 12 08:36:42 2017

@author: Saike Tian """



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

import sdds

class file():
    
    def __init__(self,input):
        temp = sdds.SDDS(0)
        temp.load(input)
        self.columnData = temp.columnData
        self.columnName = temp.columnName
        self.parameterData = temp.parameterData 
        self.parameterName = temp.parameterName
        
    def col(self,column,page = 1):
        col_data = self.columnData[self.columnName.index(column)]
        col_data_temp = np.array(col_data)
        return col_data_temp[page-1]
    def par(self,parameter,page = 1):
        par_data = self.parameterData[self.parameterName.index(parameter)]
        par_data_temp = np.array(par_data)
        return par_data_temp[page-1]
        
        