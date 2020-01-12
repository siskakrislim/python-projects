# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 16:08:23 2017

@author: HP
"""

#%%
def problem2_7():
    a = input("Enter length of side one: ")
    b = input("Enter length of side two: ")
    c = input("Enter length of side three: ")
    numA = float(a)
    numB = float(b)
    numC = float(c)
    s = float((1/2)*(numA + numB + numC))
    area = float((s*(s-numA)*(s-numB)*(s-numC))**(1/2))
    print("Area of a triangle with sides",numA,numB,numC,"is",area)