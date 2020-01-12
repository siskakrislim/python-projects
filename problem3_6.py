# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 21:40:31 2017

@author: HP
"""

#%%

import sys

def problem3_6(filename, filename1):
    with open(filename, "rt") as infile:
        with open(filename1, "wt") as outfile:
            for row in infile:
                outfile.write("{}\n".format(len(row.strip("\n"))))
if __name__ == "__main__":
    problem3_6(*sys.argv[1:])
   