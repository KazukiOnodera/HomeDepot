# -*- coding: utf-8 -*-
"""
Created on Mon Feb 29 13:13:41 2016

@author: onodera
"""

import pandas as pd
import numpy as np
import time
import homedepot as hd
import xgboost as xgb
from sklearn.cross_validation import train_test_split
reload(hd)

#seed = 1457665531 # fix
seed = int(time.time())
np.random.seed(seed)

sub = hd.load_sub()
sub.drop(['relevance'], axis=1, inplace=True)

words = [1,2,3,4]
for w in words:
    tt,prd = hd.load_all(word=w)
    test_id = tt[np.isnan(tt.r)]['id']
    test_id = test_id.to_frame()
    #raise Exception("SUCCESS!!!")
    
    #==============================================================================
    # train test
    #==============================================================================
    labels = np.array(tt[~np.isnan(tt.r)].r)
    tt = pd.merge(tt,prd,on='pid',how='left')
    col = [x for x in tt.columns if tt[x].dtype != 'O' and x not in ['id','pid']]
    tt = tt[col]
    col.remove('r')
    'train'
    train = np.array(tt[~np.isnan(tt.r)][col])
    train[np.isnan(train)]=-2
    'test'
    test = np.array(tt[np.isnan(tt.r)][col])
    test[np.isnan(test)]=-2
    
    #raise Exception("LOADED TRAIN & TEST!!!")
    #==============================================================================
    # xgb
    #==============================================================================
    cnt = 10
    for i in range(cnt):
        param = {
         'max_depth':np.random.randint(7,12),
         'eta':0.01,
         'min_child_weight':10,
         'subsample':np.random.uniform(0.5,0.9),
         'colsample_bytree':np.random.uniform(0.5,0.9),
         'silent':0,
         'objective':'reg:linear',
         'eval_metric':'rmse'
        }
        nround = 5000
        
        x_build,x_valid,y_build,y_valid = train_test_split(train, labels, test_size=0.1, 
                                                           random_state=np.random.randint(0,999))
        xgtrain = xgb.DMatrix(x_build, label=y_build)
        xgval = xgb.DMatrix(x_valid, label=y_valid)
        
        #train using early stopping and predict
        watchlist = [(xgtrain, 'train'),(xgval, 'val')]
        model = xgb.train(param, xgtrain, nround, watchlist, early_stopping_rounds=50,
                          verbose_eval=True)
        if i == 0:
            pred = model.predict(xgb.DMatrix(test))
        else:
            pred += model.predict(xgb.DMatrix(test))
    
    test_id['relevance'] = pred/cnt
    
    if w == words[0]:
        stack = test_id
    else:
        stack = pd.concat([stack,test_id])

sub = pd.merge(sub,stack,on='id',how='left')
sub = sub[sub.relevance>0]


sub.ix[sub.relevance>3,'relevance']=3
sub.ix[sub.relevance<1,'relevance']=1
hd.out(sub,'xgb10_words1-4_328_1')

raise Exception("SUCCESS!!!")































































































































