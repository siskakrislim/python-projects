# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 13:55:10 2017

@author: HP
"""

#%%
def problem1_7():
    b1 = input("Enter the length of one of the bases: ")
    b11 = float(b1)
    b2 = input("Enter the length of the other base: ")
    b22 = float(b2)
    h = input("Enter the height: ")
    h1 = float(h)
    A = float(1/2)*(b11+b22)*(h1)
    print ("The area of a trapezoid with bases",b11,"and",b22,"and","height",h1,"is",A)
      