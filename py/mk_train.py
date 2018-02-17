# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 22:23:34 2016

@author: Kazuki
"""

import homedepot as hd #comment out syn_tbl
import numpy as np
import pandas as pd

tr,prd = hd.load_all(onlytrain=True,mk_csv=True)

merged = pd.merge(tr,prd,on='pid',how='left')
merged = merged[['s_','t_','r']]


def is_contain_w(li,w):
    if w in li:
        return True
    return False
#    
def is_contain_li(li,ng):
    for n in ng:
        if n in li:
            return True
    return False

#==============================================================================
# 
#==============================================================================
w='angl'

angl = merged[merged.t_.map(lambda x:is_contain_w(x,w))]\
        [merged.s_.map(lambda x:is_contain_w(x,w))]


words = np.random.choice(merged.s_)
w = np.random.choice(words)
tmp = merged[merged.t_.map(lambda x:is_contain_w(x,w))]\
        [merged.s_.map(lambda x:is_contain_w(x,w))]












