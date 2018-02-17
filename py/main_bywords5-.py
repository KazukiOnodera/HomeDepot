# -*- coding: utf-8 -*-
"""
Created on Mon Feb 29 13:13:41 2016

@author: onodera
"""

import pandas as pd
import numpy as np
import time
import homedepot as hd
reload(hd)

#seed = 1457665531 # fix
seed = int(time.time())
np.random.seed(seed)

tt,prd = hd.load_all(mod=4)

if len(tt) == 240760:
    test_id = tt[np.isnan(tt.r)][tt.s_len>4]['id']
    test_id = test_id.to_frame().id.tolist()
else:
    raise Exception("SUCCESS!!!")

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
import xgboost as xgb
from sklearn.cross_validation import train_test_split
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


sub = hd.load_sub()
sub.relevance = pred/cnt

sub = sub[sub.id.isin(test_id)]

sub.ix[sub.relevance>3,'relevance']=3
sub.ix[sub.relevance<1,'relevance']=1
hd.out(sub,'xgb10_words5-_328_1')

raise Exception("SUCCESS!!!")

#==============================================================================
# merge
#==============================================================================

pred = pd.concat([pd.read_csv(hd.path_sub+'xgb10_words1-4_328_1.csv'),
                  pd.read_csv(hd.path_sub+'xgb10_words5-_328_1.csv')])
pred.sort_values(by='id',inplace=True)

#sub = hd.load_sub()
#sub.relevance = pred
#sub.ix[sub.relevance>3,'relevance']=3
#sub.ix[sub.relevance<1,'relevance']=1
hd.out(pred,'xgb10_bywords_328_1')





















































































































