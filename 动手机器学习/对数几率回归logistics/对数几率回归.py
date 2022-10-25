'''
作者：卢沛安
时间：2022年10月25日
'''
from typing import List , Tuple , Dict , Optional
import numpy as np


def sigmod( x ) :
    z = 1 / (1 + np.exp( -x ))
    return z


def initialize_params( dims ) :
    W = np.zeros( (dims , 1) )
    b = 0
    return W , b


def logistic( X , y , W , b ) :
    num_train = X.shape[ 0 ]
    num_feature = X.shape[ 1 ]
    # 对数几率回归模型的输出
    a = sigmod( np.dot( X , W ) + b )
    # 交叉损失
    cost = -1 / num_train * np.sum( y * np.log( a ) + (1 - y) * np.log( 1 - a ) )
    # 权重梯度
    dW = np.dot( X.T , (a - y) ) / num_train
    db = np.sum( a-y  ) / num_train


    if __name__ == '__main__' :
        print( "finished!" )
