# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 09:52:48 2016

@author: onodera
"""

import homedepot as hd #comment out syn_tbl
import pandas as pd
import numpy as np

train,prd = hd.load_all(onlytrain=True,mk_csv=True)
items = pd.read_csv(hd.path_sub+'06sort_items_query.csv',index_col=0)['0'].tolist()
train['s_item_myrule'] = train.s_.map(lambda x:hd.get_sitem(x))
train['s_item_list'] = train.s_.map(lambda x:hd.get_item_list_in_list(items,x))
train['s_item'] = ''
for i in train.index:
    if train['s_item_list'].values[i]=='':
        train['s_item'].values[i] = train['s_item_myrule'].values[i]
    else:
        train['s_item'].values[i] = train['s_item_list'].values[i]
            
items = pd.read_csv(hd.path_sub+'06sort_items_title.csv',index_col=0)['0'].tolist()
prd['t_item_myrule'] = hd.hdp.pred_item_in_title(prd)
prd['t_item_myrule'] = prd.t_item_myrule.map(lambda x:hd.str_stem(x))
prd['t_item_list'] = prd.t_.map(lambda x:hd.get_item_list_in_list(items,x))
prd['t_item'] = ''
for i in prd.index:
    if prd['t_item_list'].values[i]=='':
        prd['t_item'].values[i] = prd['t_item_myrule'].values[i]
    else:
        prd['t_item'].values[i] = prd['t_item_list'].values[i]
merged = pd.merge(train,prd,on='pid',how='left')
#==============================================================================
# 
#==============================================================================
#merged = merged[['s_','t_','r']]
#
#def del_num(li):
#    li = [x for x in li if x.isalpha()]
#    return li
#    
#def is_contain_w(li,w):
#    if w in li:
#        return True
#    return False
##    
#def is_contain_li(li,ng):
#    for n in ng:
#        if n in li:
#            return True
#    return False
#
#
#w = 'drill'
#w2 = 'driver'
#
#contain_s = merged[merged.t_.map(lambda x:not is_contain_w(x,w))]\
#                        [merged.s_.map(lambda x: is_contain_w(x,w))]
#
#hd.mk_freq_table(contain_s[contain_s.r>2.7].t_)
#                        [merged.s_.map(lambda x:not is_contain_li(x,other))]

#merged.t_ = merged.t_.map(lambda x:del_num(x))
#merged.s_ = merged.s_.map(lambda x:del_num(x))
#
#
#
#
#words = np.random.choice(merged.s_)
#w = np.random.choice(words)
#other = list(words)
#other.remove(w)
#
##w ='white'
#for w in words:
#    other = list(words)
#    other.remove(w)
#    
#    contain_s = merged[merged.t_.map(lambda x:is_contain_w(x,w))]\
#                        [merged.s_.map(lambda x:is_contain_w(x,w))]
##                        [merged.s_.map(lambda x:not is_contain_li(x,other))]
#    print w,':','MEAN',round(contain_s.r.mean(),3),'STD',round(contain_s.r.std(),3)
    
#    contain_s = contain_t[contain_t.s_.map(lambda x:is_contain_w(x,w))]\
#                        [contain_t.s_.map(lambda x:not is_contain_li(x,other))]
#    print w,':',contain_s.r.mean()
#    
#    contain_s = contain_t[contain_t.s_.map(lambda x:not is_contain_w(x,w))]\
#                        [contain_t.s_.map(lambda x:is_contain_li(x,other))]
#    print w,':',contain_s.r.mean()
    
#    contain_s = merged[merged.t_.map(lambda x:is_contain_li(x,other))]\
#                        [merged.s_.map(lambda x:is_contain_li(x,other))]\
#                        [merged.s_.map(lambda x:not is_contain_w(x,w))]
#    print w,':',contain_s.r.mean()
#                        
#    contain_s = merged[merged.t_.map(lambda x:is_contain_li(x,other))]\
#                        [merged.s_.map(lambda x:not is_contain_li(x,other))]\
#                        [merged.s_.map(lambda x: is_contain_w(x,w))]
#    print w,':',contain_s.r.mean()
    


#==============================================================================
# 
#==============================================================================

subset = merged[merged.s_len<3][merged.r>=2.6][merged.t_item!='']#\
#        [['t','t_','t_item_myrule','t_item_imp','t_item_weight','s','s_',
#          's_item_myrule', 's_item_imp','s_item_weight','r']]

def iscontain(subset):
    li = []
    for i in subset.index:
        if not hd.is_list_in_list(subset.s_[i],subset.t_[i]):
            li.append([subset.s_item[i],subset.t_item[i]])
    return pd.DataFrame(li,columns=['s_item','t_item'])

df = iscontain(subset)

df['st'] = df.s_item+' '+df.t_item

freq = df.st.value_counts()
df = freq.to_frame()

def ret0(s):
    return s.split()[0]
def ret1(s):
    return s.split()[1]

df['s']= df.index.map(lambda x:ret0(x))
df['t']= df.index.map(lambda x:ret1(x))

df = df[df.st>2][df.s!=df.t][df.s.map(len)>2]

hd.out(df[['s','t']],'07syn')

raise

for i in train.index:
    if 'screww' in train.s[i]:
        print train.s_[i],i


for i in range(30):
    print train.s_item1[i],hd.get_syn(train.s_item1[i])



























