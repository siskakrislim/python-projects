# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 17:05:03 2017

@author: HP
"""

#%%
import random
def problem2_4():
    random.seed(70)
    numlis=[]
    for i in range(0,10):
        numlis.append(30 + 5*random.random())
    print(numlis)
