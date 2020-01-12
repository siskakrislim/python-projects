# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 16:02:00 2017

@author: HP
"""

#%%
import random

def problem2_6():
    random.seed(431)
    dice = random.randint
    print(*(dice(1,6) + dice(1,6) for _ in range(100)), sep="\n")
    
    
