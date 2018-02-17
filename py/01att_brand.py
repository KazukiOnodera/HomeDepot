# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 22:36:45 2016

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
"TITLE"
prd.loc[:,'t_'] = prd.t.map(lambda x:hd.str_stem(x)).str.split()
prd.reset_index(drop=True,inplace=True)


name ='MFG Brand Name'
pid = prd.pid.tolist()
att = hd.load_att()
att = att[att.name==name]
del att['name']
att.columns = [['pid',name]]
att = att[att.pid.isin(pid)]
att[name] = att[name].map(lambda x:hd.str_stem(x))

prd = pd.merge(prd,att,on='pid',how='left')

prd = prd.drop_duplicates(subset='pid')
prd.reset_index(drop=True,inplace=True)
prd.rename(columns={'MFG Brand Name':'p_brand'},inplace=True)
prd['p_brand'] = prd.p_brand.fillna('null')
brand = prd.p_brand.str.lower().unique().tolist()
brand.remove('null')

def revise_brand(prd,brand):
    for i in prd.index:
        if prd.p_brand[i] == 'null':
            for j in range(4):
                if ' '.join(prd.t_[i][:j]) in brand:
                    br = ' '.join(prd.t_[i][:j])
                    prd.p_brand[i]=br
                    break
    return prd
    
prd = revise_brand(prd,brand)


hd.out(prd[['pid','p_brand']],'01att_brand')

