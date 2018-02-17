# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 17:22:38 2016

@author: onodera
"""
import homedepot as hd
import pandas as pd
import time
import os
# calc time
start = time.time()
ospid = os.getpid()
print 'ospid:',ospid

steps = [200,70,25,10,3,1]

#==============================================================================
tr,prd = hd.load_all(onlytrain=True,mk_csv=True)
base = pd.merge(tr,prd,on='pid',how='left')[['pid','t_','s_','r']]

rr = [2.33, 2.67, 3.] #need 2.?

items = pd.read_csv(hd.path_sub+'05item_tbl_title_selected.csv')['Unnamed: 0'].to_frame()
items.columns = ['terms']
items['order'] = 0
items = items.terms.tolist()

items = pd.read_csv(hd.path_sub+'06sort_items_title.csv',index_col=0)['0'].tolist()
ng = pd.read_csv(hd.path_sub+'06sort_items_title_ng.csv',index_col=0)['0'].tolist()

def is_inc2(items,li):
    cnt = 0
    for i in li:
        if i in items:
            cnt += 1
    if cnt > 1:
        return True
    else:
        return False

def get_item_list_in_list(li1,li2):
    for i in li1:
        if i in li2:
            return i
    return ''

def set_flg(base):
    li = []
    li += [(base.item[i] in base.s_[i])*1 for i in base.index]
    return li

def fitness_function(base):
    ave = 0
    for r in rr[:3]:
        ba = base[base.r==r][base.item!='']#.reset_index(drop=True,inplace=True)
        if len(ba)>0:
            ave += ba.match.mean()
    return ave/3.

#==============================================================================
# 
#==============================================================================
base = base[base.t_.map(lambda x:is_inc2(items,x))]

base['item'] = base.t_.map(lambda x:get_item_list_in_list(items,x))
base['match'] = set_flg(base)
score_best = fitness_function(base)


#ng = []
for j in range(1,100):
    for i in items[::-1]:
        if i not in ng:
            ind_bk = items.index(i)
            items.remove(i)
            items.insert(j,i)
            base['item'] = base.t_.map(lambda x:get_item_list_in_list(items,x))
            base['match'] = set_flg(base)
            score = fitness_function(base)
            print 'item:',i,'   score_best:',score_best,'   score:',score
            if score_best < score:
                score_best = score
            elif score_best == score:
                ng.append(i)
            else:
                items.remove(i)
                items.insert(ind_bk,i)
    df = pd.DataFrame(items)
    hd.out(df,'06sort_items_title',True)
    df = pd.DataFrame(ng)
    hd.out(df,'06sort_items_title_ng',True)

raise
for step in steps:
    for i in items[step:]:
        if i not in ng:
            sw = True
            ins_pos = items.index(i)
            while sw == True:
                ins_pos -= step
                if ins_pos < 0:
                    sw = False
                    break
                ind_bk = items.index(i)
                items.remove(i)
                items.insert(ins_pos,i)
                base['item'] = base.t_.map(lambda x:get_item_list_in_list(items,x))
                base['match'] = set_flg(base)
                score = fitness_function(base)
                print 'item:',i,'   ins_pos:',ins_pos,'   score:',score
                if score_best <= score:
                    score_best = score
                else:
                    items.remove(i)
                    items.insert(ind_bk,i)
                    sw = False

    df = pd.DataFrame(items)
    hd.out(df,'06sort_items_title',True)
    








