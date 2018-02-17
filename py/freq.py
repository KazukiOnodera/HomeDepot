# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 12:28:13 2016

@author: onodera
"""

import homedepot as hd
import pandas as pd
import os
from stemming.porter2 import stem

if os.name != 'nt':
    'Mac'
    path_org = "/Users/Kazuki/home-depot/ORG//"
    path_sub = "/Users/Kazuki/home-depot/SUB//"
#    path_org = "/Users/Kazuki/Documents/home-depot/ORG//"
else:
    'Win'
    path_org = "D:\COMPE\KAGGLE\home-depot\ORG\\"
    path_sub = "D:\COMPE\KAGGLE\home-depot\SUB\\"
    
items = hd.power+hd.materials+hd.colors+hd.case+hd.mobility

li = []
for i in items:
    li.append(stem(i))
li = list(set(li))

