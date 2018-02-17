# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 22:23:34 2016

@author: Kazuki
"""


import homedepot as hd #comment out syn_tbl
import numpy as np
import pandas as pd
import hdpath as hdp

tt,prd = hd.load_all(onlytrain=True,mk_csv=True)

hd.out(tt,'tt')
hd.out(prd,'prd')

po,ps = hdp.load()
tt = pd.read_csv(ps+'tt.csv')
tt['s_'] = tt.sfix.map(lambda x:hd.str_stem(x)).str.split()
tt['s_'] = tt.s_.map(lambda x:hd.fix_typo(x))
prd = pd.read_csv(ps+'prd.csv')
prd['t_'] = prd.t.map(lambda x:hd.str_stem(x)).str.split()

def is_contain_w(li,w):
    if w in li:
        return True
    return False

def flaten_list(lili):
    li = []
    for i in lili:
        for j in i:
            if j.isalpha() and len(j)>2:
                li.append(j)
    return li
    
def flaten_list_w(lili,w):
    li = []
    for i in lili:
        for j in i:
            if j.isalpha() and len(j)>2:
                li.append([w,j])
    return li

def rem_li_li(li1,li2):
    for i in li2:
        if i in li1:
            li1.remove(i)
            print i
    return li1
    
def shannon(col):
    entropy = - sum([ p * np.log(p) for p in col])
    return entropy
    
def get_entropy(df):
    li=[]
    for i in range(len(df)):
        col = [x for x in df.ix[i] if x>0]
        li.append(shannon(col))
    return li
#==============================================================================
#     entropy
#==============================================================================
merged = tt.merge(prd,on='pid')
merged = merged[merged.r>=3]

words = [x for x in hd.mk_freq_table(merged.s_).index.tolist() if len(x)>2]

for w in words:
    tmp = merged[merged.s_.map(lambda x:is_contain_w(x,w))].t_.tolist()
    if len(tmp)>0:
        tmp = flaten_list_w(tmp,w)
        df = pd.DataFrame(tmp,columns=['s','t'])
        cross = pd.crosstab(df.s,df.t)
        if w == words[0]:
            dist1 = cross
        else:
            dist1 = pd.concat([dist1,cross])

dist1.fillna(0,inplace=True)
dist1 = dist1.div(dist1.sum(1), axis=0)

hd.out(dist1,'r3.0above',True)
dist1 = pd.read_csv(ps+'r2.8above.csv',index_col='s')

dist1['w'] = get_entropy(dist1)

en1 = dist1['w']
en1 = en1.to_frame()
en1['s'] = en1.index
hd.out(en1,'05entropy_weight',True)


#==============================================================================
#     entropy 2
#==============================================================================
merged = tt.merge(prd,on='pid')
rr = merged.r.sort_values(ascending=False).unique().tolist()

for r in rr:
    subset = merged[merged.r==r]
    words = [x for x in hd.mk_freq_table(subset.s_).index.tolist() if len(x)>2]
    for w in words:
        tmp = subset[subset.s_.map(lambda x:is_contain_w(x,w))].t_.tolist()
        if len(tmp)>0:
            tmp = flaten_list_w(tmp,w)
            df = pd.DataFrame(tmp,columns=['s','t'])
            cross = pd.crosstab(df.s,df.t)
            if w == words[0]:
                dist1 = cross
            else:
                dist1 = pd.concat([dist1,cross])
    dist1.fillna(0,inplace=True)
    dist1 = dist1*r

dist1 = dist1.div(dist1.sum(1), axis=0)

hd.out(dist1,'r3.0above',True)
dist1 = pd.read_csv(ps+'r2.8above.csv',index_col='s')

dist1['w'] = get_entropy(dist1)

en1 = dist1['w']
en1 = en1.to_frame()
en1['s'] = en1.index
hd.out(en1,'05entropy_weight',True)














