# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 21:07:36 2017

@author: HP
"""

#%%
months=("","January","February","March","April","May","June","July","August","September",
        "October","November","December")
def problem3_3(month, day, year):
    x="{} {}, {}".format(months[month],day,year)
    print(x)
    