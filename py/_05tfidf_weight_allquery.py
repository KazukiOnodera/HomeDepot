# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 12:12:26 2016

@author: Kazuki
"""


import pandas as pd
import homedepot as hd
#import homedepot_product as hdp
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


def del_num(li):
    li = [x for x in li if x.isalpha()]
    return li
    
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

tt.s_ = tt.s_.map(lambda x:del_num(x))

query = tt.s_.map(lambda x:' '.join(x)).unique().tolist()

query = map(lambda x: x.split(), query)

li = []
for qq in query:
    li.append([' '.join(qq),len(prd[prd.t_.map(lambda x:is_contain_words(x,qq))])])

df = pd.DataFrame(li,columns=['s','w'])

hd.out(df,'05tfidf_weight_allquery')








