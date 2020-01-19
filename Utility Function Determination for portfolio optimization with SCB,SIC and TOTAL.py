# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 10:53:20 2020

@author: Dell
"""

import  numpy as np
import pandas as pd
import scipy as sp

paths=[r'C:\Users\Dell\Desktop\data\SIC VWAP closing prces.xlsx',\
       r'C:\Users\Dell\Desktop\data\TOTAL VWAP closing prces.xlsx',\
          r'C:\Users\Dell\Desktop\data\SCB VWAP closing prces.xlsx' ]

path=r'C:\Users\Dell\Desktop\data\SIC VWAP closing prces.xlsx'
#calculating returns
def returnCalculation(dataPath):
    dataRead=pd.read_excel(dataPath)
    dataClose=dataRead['Closing Price VWAP (GHS)']
    returns=dataClose.pct_change()
    return returns


rets=[]
for path in paths :
    getRets=returnCalculation(path)
    rets.append(getRets)

#defining utility function
def utilityFunction(retData,a=5):
    dailyAVG=sp.mean(retData)
    dailyVariance=sp.var(retData)
    annualMean=(1+dailyAVG)**252
    annualVAR=dailyVariance*252
    return annualMean-0.5*a*annualVAR

utilitiesMeasures=[utilityFunction(_) for _ in rets]

'''
we pick the highest utility measure since its the most appropriate using 
the 'a' that is risk averseness where 1 is highest risk averseness and 10 is the
lowest risk averseness

'''
def meanAndVarAnnual(retData):
    dailyAVG=sp.mean(retData)
    dailyVariance=sp.var(retData)
    annualMean=(1+dailyAVG)**252
    annualVAR=dailyVariance*252
    return annualMean,annualVAR


meanAndVar=[meanAndVarAnnual(_) for _ in rets]

print(meanAndVar)
print()
print(utilitiesMeasures)


    

    