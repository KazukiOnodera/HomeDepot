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


raise Exception("SUCCESS!!!")


sub = hd.load_sub()
sub.relevance = pred/cnt
sub.ix[sub.relevance>3,'relevance']=3
sub.ix[sub.relevance<1,'relevance']=1
hd.out(sub,'xgb10_327_2')
#==============================================================================
# 
#==============================================================================
from sklearn.ensemble import RandomForestRegressor
import stacking as st
from sklearn.metrics import mean_squared_error
clf = RandomForestRegressor(n_estimators=np.random.randint(5000,5300),
                            criterion="mse",
                            max_features=0.8,
                            max_depth=np.random.randint(10,12),
                            n_jobs=-1,)
                            
pred = st.predict(train,labels,clf)
print mean_squared_error(labels,pred)





raise


from sklearn.linear_model import LogisticRegression
import stacking as st
from sklearn.metrics import mean_squared_error

clf = LogisticRegression(tol=0.00005)
                            
pred = st.predict(train,labels,clf)

print mean_squared_error(labels,pred)



#==============================================================================
# RF
#==============================================================================
from sklearn.ensemble import RandomForestRegressor
pred_cnt = 2
for i in range(pred_cnt):
    clf = RandomForestRegressor(n_estimators=np.random.randint(2000,2300),
                            criterion="mse",
                            max_features=0.7,
                            max_depth=np.random.randint(9,12),
                            n_jobs=-1,)
    clf.fit(train,labels)
    if i == 0:
        pred = clf.predict(test)
    else:
        pred += clf.predict(test)


raise Exception("END!!!")

sub = hd.load_sub()
sub.relevance = pred/pred_cnt
sub.ix[sub.relevance>3,'relevance']=3
hd.out(sub,'rfr_318_1')
































































































































