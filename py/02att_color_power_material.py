# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 17:33:57 2016

@author: Kazuki
"""
#import math
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

def get_att_sub(base,name):
    pid = base.pid.tolist()
    att = hd.load_att()
    att = att[att.name==name]
    del att['name']
    att.columns = [['pid',name]]
    att = att[att.pid.isin(pid)]
    att[name] = att[name].map(lambda x:hd.str_stem(x)).str.split()
    dup_pids = att[att.pid.duplicated()].pid.tolist()
    dup_inds = att[att.pid.duplicated()].index.tolist()#second ind
    if len(dup_pids)>0:
        for i,j in zip(dup_pids,dup_inds):
            att[name][j] = sum(att[att.pid==i][name].tolist(),[])
        att.drop_duplicates(subset='pid',keep='last',inplace=True)
    return pd.merge(base,att,on='pid',how='left')
    
prd = get_att_sub(prd,'Color')
prd = get_att_sub(prd,'Color Family')
prd = get_att_sub(prd,'Color/Finish')
prd = get_att_sub(prd,'Finish')
prd = get_att_sub(prd,'Finish Family')
prd = get_att_sub(prd,'Material')
prd = get_att_sub(prd,'Mount Type')
prd = get_att_sub(prd,'Fuel Type')
prd = get_att_sub(prd,'Power Type')
prd = get_att_sub(prd,'Bulb Type')

prd.reset_index(drop=True,inplace=True)
#==============================================================================
# 
#==============================================================================
li_color =[]
li_power =[]
li_mate = []
prd = prd.fillna(-1)
prd.rename(columns={'Material':'att_material'},inplace=True)
for i in prd.index:
    color = []
    power = []
    mate = []
    if prd['Color'][i] != -1:
        color +=  prd['Color'][i]
    if prd['Color Family'][i] != -1:
        color +=  prd['Color Family'][i]
    if prd['Color/Finish'][i] != -1:
        color +=  prd['Color/Finish'][i]
    if prd['Finish'][i] != -1:
        color +=  prd['Finish'][i]
    if prd['Finish Family'][i] != -1:
        color +=  prd['Finish Family'][i]
        
    if prd['Mount Type'][i] != -1:
        power +=  prd['Mount Type'][i]
    if prd['Fuel Type'][i] != -1:
        power +=  prd['Fuel Type'][i]
    if prd['Power Type'][i] != -1:
        power +=  prd['Power Type'][i]
    if prd['Bulb Type'][i] != -1:
        power +=  prd['Bulb Type'][i]
        
    if prd['att_material'][i] != -1:
        mate += prd['att_material'][i]
        
    li_color.append(' '.join(color))
    li_power.append(' '.join(power))
    li_mate.append(' '.join(mate))
    
prd['att_color'] = li_color
prd['att_power'] = li_power
prd['att_material'] = li_mate
prd.drop(['Color','Color Family','Color/Finish','Finish','Finish Family',
          'Mount Type','Fuel Type','Power Type','Bulb Type'],axis=1, 
          inplace=True)

prd['att_material'] = prd.att_material.map(lambda x:hd.str_stem(x))

hd.out(prd[['pid','att_color','att_power','att_material']],'02att_color_power_material')
















