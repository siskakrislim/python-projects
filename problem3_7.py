# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 21:31:15 2017

@author: HP
"""

#%%
def problem3_7(csv_pricefile,flower):
    import csv
    f=open(csv_pricefile)
    dict={flower:price for flower,price in csv.reader(f)}
    print(dict[flower])
    f.close()