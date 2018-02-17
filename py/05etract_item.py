# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 10:56:02 2016

@author: onodera
"""

import homedepot as hd #comment out syn_tbl
import pandas as pd
import numpy as np

tr,prd = hd.load_all(onlytrain=True,mk_csv=True)

base = pd.merge(tr,prd,on='pid',how='left')[['pid','t_','s_','r']]

#rr = base.r.sort_values().unique().tolist()
rr = [1., 1.33, 1.67, 2., 2.33, 2.67, 3.]
qq = [x for x in hd.mk_freq_table(base.s_).index.tolist() if len(x)>2 and x.isalpha()]
#==============================================================================
# 
#==============================================================================
def get_item_list_in_list(li1,li2):
    for i in li1:
        if i in li2:
            return i
    return ''

'for query'
def set_flg(base):
    li = []
    li += [(base.item[i] in base.t_[i])*1 for i in base.index]
    return li
    
def get_dict(base):
    di = {}
    for r in rr:
        ba = base[base.r==r][base.item!='']#.reset_index(drop=True,inplace=True)
        if len(ba)>0:
            print r,':',ba.match.mean()
            di[r]=ba.match.mean()
    return di
"for title"
def set_flg2(base):
    li = []
    li += [(base.item[i] in base.s_[i])*1 for i in base.index]
    return li
    
def get_dict2(base):
    di = {}
    for r in rr:
        ba = base[base.r==r][base.item!='']#.reset_index(drop=True,inplace=True)
        if len(ba)>0:
            print r,':',ba.match.mean()
            di[r]=ba.match.mean()
    return di
#==============================================================================
# EXTRACT ITEMS
#==============================================================================

li = []

for q in qq:
    base['item'] = base.s_.map(lambda x:get_item_list_in_list([q],x))
    
    base['match'] = set_flg(base)
    print q
    li.append(get_dict(base))
    
df = pd.DataFrame(li)
col = ['col_'+str(x) for x in rr]
df.columns = col
df.index = qq
hd.out(df,'05item_tbl_query',True)
df = pd.read_csv(hd.path_sub+'05item_tbl_query.csv',index_col=0)

df['sum'] = df[col].sum(1)
df['ave'] = df[col].mean(1)

df.fillna(0,inplace=True)
df = df[df['col_2.33']>0.4][df['col_2.67']>0.5][df['col_3.0']>0.5][df['sum']!=1]

hd.out(df,'05item_tbl_query_selected',True)
#==============================================================================
# EXTRACT ITEMS 2
#==============================================================================

li = []

for q in qq:
    base['item'] = base.t_.map(lambda x:get_item_list_in_list([q],x))
    
    base['match'] = set_flg2(base)
    print q
    li.append(get_dict2(base))
    
df = pd.DataFrame(li)
col = ['col_'+str(x) for x in rr]
df.columns = col
df.index = qq
hd.out(df,'05item_tbl_title',True)
#df = pd.read_csv(hd.path_sub+'05item_tbl_title.csv',index_col=0)

df['sum'] = df[col].sum(1)
df['ave'] = df[col].mean(1)

df.fillna(0,inplace=True)
df = df[df['col_2.0']<0.9][df['col_2.67']>=0.2][df['col_3.0']>=0.3][df['sum']!=1][df['ave']<0.9]

hd.out(df,'05item_tbl_title_selected',True)
#==============================================================================
# OPTIMIZE ITEM ORDER
#==============================================================================

#tmp = ['tile','wall']
#
#items = hdl.items
#
#np.random.shuffle(items)
#base['item'] = base.s_.map(lambda x:get_item_list_in_list(items,x))
#base['match'] = set_flg(base)
#fitness_function(base)









