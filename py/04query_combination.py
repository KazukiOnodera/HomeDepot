# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 00:19:22 2016

@author: Kazuki
"""

import pandas as pd
import homedepot as hd
#import homedepot_product as hdp
import hdpath


mod = 3

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

tt = tt[tt.id%4==mod].reset_index(drop=True)
prd = prd[prd.pid.isin(tt.pid)].reset_index(drop=True)

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
""""============================
    PRODUCT FEATURES
    ============================"""
print '========== PRODUCT =========='
prd = prd.sort_values(by='pid')
"TITLE"
prd.reset_index(drop=True,inplace=True)
prd['tlen'] = prd.t.str.len()
prd['t_'] = prd.t.map(lambda x:hd.str_stem(x)).str.split()
prd.loc[:,'t_len'] = prd.t_.str.len()

merged = pd.merge(tt,prd[['pid','t_']],on='pid',how='left')

tt = hd.rep_comb(merged)

tt.s = tt.s_.map(lambda x:' '.join(x))

tt['comb'] = 1 - (tt['s_len'] == tt.s_.str.len())*1

hd.out(tt[['id','s','typo','comb']],'04query_comb'+str(mod))

raise Exception('SUCCESS')
#==============================================================================
# CONCAT
#==============================================================================
for i in range(4):
    if i == 0:
        tt = pd.read_csv(path_sub+'04query_comb'+str(i)+'.csv')
    else:
        tt = pd.concat([tt,pd.read_csv(path_sub+'04query_comb'+str(i)+'.csv')])
    tt.sort_values(by='id',inplace=True)

hd.out(tt[['id','s','typo','comb']],'04query_comb')