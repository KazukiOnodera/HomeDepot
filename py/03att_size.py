# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 18:30:36 2016

@author: Kazuki
"""

import homedepot as hd
import pandas as pd
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


"""product_table"""
prd = pd.concat([train,test])
del train
del test
prd = prd.drop_duplicates(subset='pid')
prd.drop(['id','s', 'r'], axis=1, inplace=True)


prd = prd.sort_values(by='pid')
prd.reset_index(drop=True,inplace=True)

def rep_alpha(s):
    if isinstance(s,str):
        if ' in' in s:
            s = s.translate(None,' in')
        if ' lb' in s:
            s = s.translate(None,' lb')
        if ' ' in s:
            s = s.translate(None,' ')
    return s
    
def get_size(prd):
    pid = prd.pid.tolist()
    att = hd.load_att()
    att = att[att.pid.isin(pid)]
    depth = att[att.name.str.contains('Depth')==True]
    depth.value = depth.value.map(lambda x:rep_alpha(x))
    depth = depth[depth.value.str.replace(".","").str.isdigit()==True]
    
    height = att[att.name.str.contains('Height')==True]
    height.value = height.value.map(lambda x:rep_alpha(x))
    height = height[height.value.str.replace(".","").str.isdigit()==True]
    
    width = att[att.name.str.contains('Width')==True]
    width.value = width.value.map(lambda x:rep_alpha(x))
    width = width[width.value.str.replace(".","").str.isdigit()==True]
    
    weight = att[att.name.str.contains('Weight')==True]
    weight.value = weight.value.map(lambda x:rep_alpha(x))
    weight = weight[weight.value.str.replace(".","").str.isdigit()==True]
    del weight['name']
    
    merged = pd.concat([depth,height,width])
    del merged['name']
    merged.sort_values(by='pid',inplace=True)
    merged.reset_index(drop=True,inplace=True)
    
    li = []
    for pid in merged.pid.unique().tolist():
        li.append([int(pid),' '.join(merged[merged.pid==pid].value.tolist())])
    size = pd.DataFrame(li,columns=['pid','att_size'])
    prd = pd.merge(prd,size,on='pid',how='left')
    
    li = []
    for pid in weight.pid.unique().tolist():
        li.append([int(pid),' '.join(weight[weight.pid==pid].value.tolist())])
    weight = pd.DataFrame(li,columns=['pid','att_weight'])
    prd = pd.merge(prd,weight,on='pid',how='left')
    
    return prd
    
prd = get_size(prd)
prd.fillna('',inplace=True)

hd.out(prd[['pid','att_size','att_weight']],'03att_size_weight')





