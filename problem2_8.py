# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 16:31:19 2017

@author: HP
"""

#%%
hourly_temp = [40.0,39.0,37.0,34.0,33.0,34.0,36.0,37.0,38.0,39.0, \
               40.0, 41.0,44.0, 45.0,47.0,48.0,45.0,42.0,39.0,37.0,\
               36.0,35.0,33.0,32.0]
def problem2_8(temp_list):
    sum_ = 0
    for i in temp_list:
        sum_ = sum_ + i
    print("Average:",sum_/len(temp_list))
    a = max(temp_list)
    b = min(temp_list)
    print("High:",a)
    print("Low:",b)