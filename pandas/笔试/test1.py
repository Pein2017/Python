'''
作者：卢沛安
时间：2022年11月01日
'''
from typing import List , Tuple , Dict , Optional
import numpy as np
import pandas as pd

df = pd.read_csv( 'pandas/笔试/data.csv' )
from sklearn.ensemble import RandomForestRegressor
# 1 数据预处理
  #1.1  # 可知最大窗口为120， 跳过前120条数据
df.isnull().sum()
df.loc[ 120 : , ].isnull().sum()
df = df.drop( labels='feature0' , axis=1 )
    # 均值填充
for column in list(df.columns[df.isnull().sum() > 0]):
    mean_val = df[column].mean()
    df[column].fillna(mean_val, inplace=True)
df.isnull().sum()
df = df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
    # 1.2 熟悉R的操作但Python不熟悉

#  2 拟合部分


from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import Lasso, Ridge, LassoCV,LinearRegression
from sklearn.model_selection import KFold, RepeatedKFold, GridSearchCV, cross_validate, train_test_split

X , y = df.iloc[:,7:-1] , df['label_y']
X = X.replace((np.inf, -np.inf, np.nan), 0).reset_index(drop=True)
Y = y.replace((np.inf, -np.inf, np.nan), 0).reset_index(drop=True)
X_train , X_test , y_train , y_test = train_test_split( X , y , test_size=0.2 , random_state=41 )
y_train, y_test = y_train.values.reshape( (-1,1)) , y_test.values.reshape( (-1,1))
from sklearn import linear_model
# lasso
lasso_alphas = np.linspace(0, 1, 100)
cv = RepeatedKFold(n_splits=10, n_repeats=3, random_state=1)
lasso = LassoCV(alphas=lasso_alphas, cv=cv, n_jobs=-1)
lasso.fit(X_train, y_train)
lasso.score(X_test,y_test)





na_list = [ 'feature26' , 'feature41' ]


for j in na_list :
    df_na = df.loc[ 120 : , j ]
    ytrain = df_na[ df_na.notnull() ]
    ytest = df_na[ df_na.isnull() ]
    xtrain = df.iloc[ 120 : , ytrain.index ]
    xtest = df.iloc[ 120 : , ytest.index ]
    rf = RandomForestRegressor()
    rf.fit( xtrain , ytrain )
    y_pred = rf.predict( xtest )
    df_na[ df_na.isnull() ] = y_pred

if __name__ == '__main__' :
    print( "finished!" )
