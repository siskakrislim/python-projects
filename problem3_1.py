# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 11:27:04 2017

@author: HP
"""

#%%
def problem3_1(txtfilename):
    with open(txtfilename, "rt") as infile:
        line = infile.read()
        print("{}\n\nThere are {} letters in the file.".format(line, len(line)))