'''
作者：卢沛安
时间：2023年02月09日
'''

import numpy as np
import pandas as pd

### 定义二叉特征分裂函数
def feature_split( X , feature_i , threshold ) :
    split_func = None
    if isinstance( threshold , int ) or isinstance( threshold , float ) :
        split_func = lambda sample : sample[ feature_i ] >= threshold
    else :
        split_func = lambda sample : sample[ feature_i ] == threshold

    X_left = np.array( [ sample for sample in X if split_func( sample ) ] )
    X_right = np.array( [ sample for sample in X if not split_func( sample ) ] )
    return np.array( [ X_left , X_right ] )


### 计算基尼指数
def calculate_gini( y ) :
    y = y.tolist()
    probs = [ y.count( i ) / len( y ) for i in np.unique( y ) ]
    gini = sum( [ p * (1 - p) for p in probs ] )
    return gini


### 打乱数据
def data_shuffle( X , y , seed=None ) :
    if seed :
        np.random.seed( seed )
    idx = np.arange( X.shape[ 0 ] )
    np.random.shuffle( idx )
    return X[ idx ] , y[ idx ]


### 类别标签转换
def cat_label_convert( y , n_col=None ) :
    if not n_col :
        n_col = np.amax( y ) + 1
    one_hot = np.zeros( (y.shape[ 0 ] , n_col) )
    one_hot[ np.arange( y.shape[ 0 ] ) , y[ : , 0 ] ] = 1
    return one_hot

class SquareLoss :
    def loss( self , y , y_pred ) :
        return 0.5 * np.power( (y - y_pred) , 2 )

    def gradient( self , y , y_pred ) :
        return - (y - y_pred)

    def hess( self , y , y_pred ):
        return np.ones_like( y )

## 分类损失函数
class Sigmoid :
    def __call__( self , x ) :
        return 1 / (1 + np.exp( -x ))

    def gradient( self , x ) :
        return self.__call__( x ) * (1 - self.__call__( x ))



class LogisticLoss :
    def __init__( self ) :
        sigmoid = Sigmoid()
        self._func = sigmoid
        self._grad = sigmoid.gradient

    def loss( self , y , y_pred ) :
        '''
        Equivalent to but faster than np.minimum(a_max, np.maximum(a, a_min)).
        '''
        y_pred = np.clip( y_pred , 1e-10 , 1 - 1e-10 )
        p = self._func( y_pred )
        return y * np.log( p ) + (1 - y) * np.log( 1 - p )


    def gradient( self , y , y_pred ) :
        p = self._func( y_pred )
        return -(y - p)

    def hess( self , y , y_pred ) :
        p = self._func( y_pred )
        return p * (1 - p)

if __name__ == '__main__' :
    print( "finished!" )
