# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 21:10:29 2017

@author: HP
"""

#%%
import random
numList=[]
random.seed(500)
for i in range(0,25):
    numList.append(round(100*random.random(),1))
#%%
def problem4_2(ran_list):
    import statistics
    print(statistics.mean(ran_list))
    print(statistics.stdev(ran_list))