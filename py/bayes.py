# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 21:13:39 2016

@author: Kazuki
"""

import pandas as pd
import os
import time
import homedepot as hd

if os.name != 'nt':
    'Mac'
    path_org = "/Users/Kazuki/home-depot/ORG//"
    path_sub = "/Users/Kazuki/home-depot/SUB//"
else:
    'Win'
    path_org = "D:\COMPE\KAGGLE\home-depot\ORG\\"
    path_sub = "D:\COMPE\KAGGLE\home-depot\SUB\\"
    
infile = "train.csv"
train = pd.read_csv(path_org+infile)
#['id', 'product_uid', 'product_title', 'search_term', 'relevance']
train.columns = [['id','pid','t','s','r']]

train['t_'] = train.t.map(lambda x:hd.str_stem(x)).str.split()
train['s_'] = train.s.map(lambda x:hd.str_stem(x)).str.split()

#==============================================================================
# 
#==============================================================================
s_table = hd.mk_freq_table(train.s_)

s_table = s_table.to_frame()


li =[]
for i in s_table.index:
    sum_r = 0
    cnt = 0
    for j in train.index:
        if i in train.s_[j]:
            sum_r += train.r[j]
            cnt += 1
    li.append(float(sum_r)/cnt)
s_table['ave_r'] = li
hd.out(s_table,'s_tbl')


#==============================================================================
# 
#==============================================================================
t_table = hd.mk_freq_table(train.t_)

t_table = t_table.to_frame()


li =[]
for i in t_table.index:
    sum_r = 0
    cnt = 0
    for j in train.index:
        if i in train.t_[j]:
            sum_r += train.r[j]
            cnt += 1
    li.append(float(sum_r)/cnt)
t_table['ave_r'] = li
hd.out(t_table,'t_tbl')