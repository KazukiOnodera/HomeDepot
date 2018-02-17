# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 22:23:34 2016

@author: Kazuki
"""

import pandas as pd
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
prd = hdp.pred_item_in_title(prd)
prd['t_item1'] = prd.t_item1.map(lambda x:hd.str_stem(x))
prd.drop(['t_b4_in_with','t_b4_in','t_b4_with','t_last'], axis=1, inplace=True)
prd['t2'] = prd.t_.map(lambda x:' '.join(x))

s_freq = hd.mk_freq_table(tt.s_)
s_freq = s_freq.to_frame()
s_ind = s_freq.index.tolist()

def is_contain_w(li,w):
    if w in li:
        return True
    return False
    
def is_contain_words(li,words):
    cnt = 0
    for w in words:
        if w in li:
            cnt +=1
    if cnt == len(words):
        return True
    return False


li = []
for w in s_ind:
    li.append(len(prd[prd.t_.map(lambda x:is_contain_w(x,w))]))
s_freq['w'] = li

s_freq['s'] = s_freq.index

hd.out(s_freq[['s','w']],'05tfidf_weight')

