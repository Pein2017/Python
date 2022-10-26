'''
作者：卢沛安
时间：2022年10月25日
'''
from typing import List , Tuple , Dict , Optional

import numpy as np


def linear_loss( X: List[ List[ int ] ] , y: List[ int ] , W , b ) :
    '''
    输出:
    y_hat , loss , dW: 权重系数一阶偏导, db: 偏置一阶偏导
    '''
    num_train = X.shape[ 0 ]
    num_feature = X.shape[ 1 ]
    y_hat = np.dot( X , W ) + b
    # 计算LOSS
    loss = np.sum( (y_hat - y) ** 2 ) / num_train
    dW = np.dot( X.T , (y_hat - y) ) / num_train
    db = np.sum( (y_hat - y) ) / num_train
    return y_hat , loss , dW , db


def initialize_params( dims ) :
    '''

    :param dims: 变量维度
    :return:
    W: 初始化权重
    b: 初始化偏置
    '''
    W = np.zeros( (dims , 1) )
    b = 0
    return W , b


def linear_train( X , y , learning_rate=0.01 , epochs=10 ** 4 ) :
    '''

    :return:
    loss_his: 每次迭代的LOSS
    params: 优化后的参数字典
    grads： 优化后的参数梯度字典
    '''
    loss_his = [ ]
    # 初始化
    W , b = initialize_params( X.shape[ 1 ] )
    # training
    for i in range( epochs ) :
        # 计算当前迭代的预测值、LOSS和梯度
        y_hat , loss , dW , db = linear_loss( X , y , W , b )
        W += -learning_rate * dW
        b += -learning_rate * db
        # 计算当前LOSS
        loss_his.append( loss )
        # 每1000次迭代打印当前LOSS:
        if i % 10 ** 3 == 0 :
            print( 'epoch {}: loss {}'.format( i , loss ) )
        params = {
            'W' : W ,
            'b' : b
        }
        grads = {
            'dW' : dW ,
            'db' : db
        }

    return loss_his , params , grads


from sklearn.datasets import load_diabetes
from sklearn.utils import shuffle

# 获取数据
diabetes = load_diabetes()
# 获取输入和标签
data , target = diabetes.data , diabetes.target
# 打乱数据集
X , y = shuffle( data , target , random_state=13 )
# 按照 8:2 划分训练集和测试集
offset = int( X.shape[ 0 ] * 0.8 )
# 训练集、测试集
X_train , y_train = X[ :offset ] , y[ :offset ]
X_test , y_test = X[ offset : ] , y[ offset : ]
# 改为列向量形式
y_train , y_test = y_train.reshape( (-1 , 1) ) , y_test.reshape( (-1 , 1) )

## 训练
loss_his , params , grads = linear_train( X_train , y_train , 0.01 , 2 * 10 ** 4 )


def predict( X , params ) :
    W = params[ 'W' ]
    b = params[ 'b' ]
    y_pred = np.dot( X , W ) + b
    return y_pred


y_pred = predict( X_test , params )


def r2_score( y_test , y_pred ) :
    y_avg = np.mean( y_test )
    ss_tot = np.sum( (y_test - y_avg) ** 2 )
    ss_res = np.sum( (y_test - y_pred) ** 2 )
    r2 = 1 - (ss_res / ss_tot)
    return r2

import matplotlib.pyplot as plt
print(" r2 is {}".format( r2_score( y_test , y_pred ) ) )
plt.plot( loss_his )

if __name__ == '__main__' :
    print( "finished!" )
