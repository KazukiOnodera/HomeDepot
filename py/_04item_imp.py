# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 22:23:34 2016

@author: Kazuki
"""

import homedepot as hd #comment out syn_tbl
import numpy as np
import pandas as pd

tr,prd = hd.load_all(onlytrain=True,mk_csv=True)

#hd.out(tr,'tr')
#hd.out(prd,'prd')
#==============================================================================
# new game
#==============================================================================

merged = pd.merge(tr,prd,on='pid',how='left')
merged = merged[['s_','t_','r']]

allave = merged.r.mean()

def del_num(li):
    li = [x for x in li if x.isalpha()]
    return li
    
def is_contain_w(li,w):
    if w in li:
        return True
    return False
#    
def is_contain_li(li,ng):
    for n in ng:
        if n in li:
            return True
    return False


words = [x for x in hd.mk_freq_table(merged.s_).index.tolist() if len(x)>2]

li = []
for w in words:
#    other = list(words)
#    other.remove(w)
    
    contain_s = merged[merged.t_.map(lambda x:is_contain_w(x,w))]\
                      [merged.s_.map(lambda x:is_contain_w(x,w))]
    print w,':','MEAN',round(contain_s.r.mean(),3),'STD',round(contain_s.r.std(),3)
    li.append([w,round(contain_s.r.mean(),3)])
df = pd.DataFrame(li,columns=['s','imp'])

df.fillna(0,inplace=True)
hd.out(df,'04item_imp')

#==============================================================================
# 
#==============================================================================

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
#     1
#==============================================================================
merged = pd.merge(tr,prd,on='pid',how='left')
merged = merged[['s_','t_','r']]
subset = merged[merged.r>=2.3]
#li_r = subset.r.sort_values(ascending=False).unique().tolist()
query = [x for x in hd.mk_freq_table(subset.s_).index.tolist() if len(x)>2]

imp = []
for q in query:
    contain = subset[subset.t_.map(lambda x:is_contain_w(x,q))]
    cnt_t = len(contain)
    cnt_q = len(contain[contain.s_.map(lambda x:is_contain_w(x,q))])
    if cnt_t>0:
    #    print q,float(cnt_q)/cnt_t
        imp.append([q,cnt_q,cnt_t,float(cnt_q)/cnt_t])
    
df = pd.DataFrame(imp,columns=['s','cnt_q','cnt_t','imp'])

df_ = df[df.cnt_t>50]

hd.out(df_,'04item_imp2')










