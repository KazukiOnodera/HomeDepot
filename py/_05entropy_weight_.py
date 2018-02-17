# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 22:23:34 2016

@author: Kazuki
"""

import pandas as pd
import numpy as np
import homedepot as hd
import homedepot_product as hdp
import hdpath

path_org,path_sub = hdpath.load()
    
infile = "train.csv"
train = pd.read_csv(path_org+infile)
#['id', 'product_uid', 'product_title', 'search_term', 'relevance']
train.columns = [['id','pid','t','s','r']]

infile = "product_descriptions.csv"
desc = pd.read_csv(path_org+infile)
#['product_uid', 'product_description']
desc.columns = [['pid','d']]

infile = "test.csv"
test = pd.read_csv(path_org+infile)
#['id', 'product_uid', 'product_title', 'search_term']
test.columns = [['id','pid','t','s']]

"""train test"""
tt = pd.concat([train,test])
tt.reset_index(drop=True,inplace=True)
"""product_table"""
prd = pd.concat([train,test])
prd = prd.drop_duplicates(subset='pid')
prd.drop(['id','s', 'r'], axis=1, inplace=True)

""""============================
    SEARCH TERMS FEATURES
    ============================"""
print '========== SEARCH =========='
tt['slen'] = tt.s.str.len()
tt['sfix'] = tt.s.map(lambda x:hd.fix_typo_google(x))
tt['s_'] = tt.sfix.map(lambda x:hd.str_stem(x)).str.split()
tt['s_'] = tt.s_.map(lambda x:hd.fix_typo(x))
tt['typo'] = 1-(tt.s.map(lambda x:hd.str_stem(x)).str.split()==tt.s_)*1
#    tt['s_'] = tt.s_.map(lambda x:del_ng(x))
tt['s_len'] = tt.s_.str.len()
del tt['t']
del test;del train;del desc
""""============================
    PRODUCT FEATURES
    ============================"""
print '========== PRODUCT =========='
prd = prd.sort_values(by='pid')
"TITLE"
prd.reset_index(drop=True,inplace=True)
prd['tlen'] = prd.t.str.len()
prd['t_'] = prd.t.map(lambda x:hd.str_stem(x)).str.split()
#    prd['t_'] = prd.t_.map(lambda x:del_ng(x))
prd.loc[:,'t_len'] = prd.t_.str.len()
prd = hdp.pred_item_in_title(prd)
prd['t_item1'] = prd.t_item1.map(lambda x:hd.str_stem(x))
prd.drop(['t_b4_in_with','t_b4_in','t_b4_with','t_last'], axis=1, inplace=True)
prd['t2'] = prd.t_.map(lambda x:' '.join(x))


def is_contain_w(li,w):
    if w in li:
        return True
    return False

def flaten_list(lili,w):
    li = []
    for i in lili:
        for j in i:
            if j.isalpha() and len(j)>2:
                li.append([w,j])
    return li
    
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
#     
#==============================================================================
merged = tt.merge(prd,on='pid')
merged = merged[merged.r>2.8]

words = hd.mk_freq_table(merged.s_).index.tolist()

for w in words:
    tmp = merged[merged.t_.map(lambda x:is_contain_w(x,w))].t_.tolist()
    if len(tmp)>0:
        tmp = flaten_list(tmp,w)
        df = pd.DataFrame(tmp,columns=['s','t'])
        cross = pd.crosstab(df.s,df.t)
        if w == words[0]:
            cross_tbl = cross
        else:
            cross_tbl = pd.concat([cross_tbl,cross])

cross_tbl.fillna(0,inplace=True)
cross_tbl = cross_tbl.div(cross_tbl.sum(1), axis=0)

cross_tbl['w'] = get_entropy(cross_tbl)

subset = cross_tbl['w']
subset = subset.to_frame()
subset['s'] = subset.index

hd.out(subset[['s','w']],'06entropy_weight1')
#cross_tbl['sum'] = cross_tbl.sum(axis=1)

raise Exception("!!!!!!!!")

merged = tt.merge(prd,on='pid')
merged = merged[merged.r<1.5]

words = hd.mk_freq_table(merged.s_).index.tolist()

for w in words:
    tmp = merged[merged.t_.map(lambda x:is_contain_w(x,w))].t_.tolist()
    if len(tmp)>0:
        tmp = flaten_list(tmp,w)
        df = pd.DataFrame(tmp,columns=['s','t'])
        cross = pd.crosstab(df.s,df.t)
        if w == words[0]:
            cross_tbl = cross
        else:
            cross_tbl = pd.concat([cross_tbl,cross])

cross_tbl.fillna(0,inplace=True)
cross_tbl = cross_tbl.div(cross_tbl.sum(1), axis=0)

cross_tbl['w'] = get_entropy(cross_tbl)

subset = cross_tbl['w']
subset = subset.to_frame()
subset['s'] = subset.index

hd.out(subset[['s','w']],'06entropy_weight2')


#==============================================================================
# 
#==============================================================================
w = 'bracket'
prd[prd.t_.map(lambda x:is_contain_w(x,w))].shape

words = ['angl','bracket']
prd[prd.t_.map(lambda x:is_contain_words(x,words))].t_shape















title_freq = tt.t_item1.value_counts()
train_title_freq = tt[tt.r>0].t_item1.value_counts()
test_title_freq = tt[~np.isnan(tt.r)].t_item1.value_counts()
search_freq = tt.s_item1.value_counts()

hd.out(train,'train')