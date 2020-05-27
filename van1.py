# -*- coding: utf-8 -*-
"""
Created on Wed May 20 20:44:28 2020

@author: VanNguyen
"""
import os
import pandas as pd
import numpy as np
import fnmatch
import matplotlib.pyplot as plt
import seaborn as sns
#from mpld3 import plugins
#import pymrmr
import sklearn
def vansum(a,b):
    print("Start to work...")
    c = (a*a + b*b)/2
    print("Van sum is", c)
    return c
def vanmt(c):
    print("sum increase 2")
    d = c + 2
    print("Van sum is", d)
    return d

def main():
 c = vansum(a,b)
 d = vanmt(c)
if __name__ == "__main__":
    main()