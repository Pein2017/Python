'''
作者：卢沛安
时间：2022年10月25日
'''
from typing import List , Tuple , Dict , Optional
import numpy as np


def sign( x ) :
    if x > 0 :
        return 1
    elif x < 0 :
        return -1
    else :
        return 0


vec_sign = np.vectorize( sign )


def l1_loss( X , y , w , b , alpha = 0.1 ) :
    num_train = X.shape[ 0 ]
    num_feature = X.shape[ 1 ]
    y_hat = np.dot( X , w ) + b
    loss = np.sum( (y_hat - y) ** 2 ) / num_train + np.sum( alpha * abs( w ) )
    dW = np.dot( X.T , (y_hat - y) ) / num_train + alpha * vec_sign( w )
    db = np.sum( y_hat - y ) / num_train
    return y_hat , loss , dW , db

def initialize_params( dims ):
    W = np.zeros( (dims , 1 ))
    b = 0
    return W,b
def lasso_train( X, y ,learning_rate = 0.01, epochs = 10**4):
    loss_his = []
    W,b = initialize_params( X.shape[1])
    for i in range( epochs ):
        y_hat , loss , dW , db = l1_loss( X, y , W ,b , 0.1)
        W += -learning_rate * dW
        b += -learning_rate * db
        loss_his.append( loss )
        if i % 10**3 == 0 :
            print('epoch : {}, loss : {}'.format(i,loss))
        params = {
            'W':W,
            'b':b
        }
        grads = {
            'dW':dW,
            'db':db
        }
    return loss_his,params , grads

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

lasso_loss_his , params , grads = lasso_train( X_train , y_train )




def l2_loss( X , y , w , b , alpha = 0.1 ) :
    num_train = X.shape[ 0 ]
    num_feature = X.shape[ 1 ]
    y_hat = np.dot( X , w ) + b
    loss = np.sum( (y_hat - y) ** 2 ) / num_train + alpha * ( np.sum( np.square(w) ) )
    dW = np.dot( X.T , (y_hat - y) ) / num_train + 2*alpha*w
    db = np.sum( y_hat - y ) / num_train
    return y_hat , loss , dW , db
def ridge_train( X, y ,learning_rate = 0.01, epochs = 10**4):
    loss_his = []
    W,b = initialize_params( X.shape[1])
    for i in range( epochs ):
        y_hat , loss , dW , db = l2_loss( X, y , W ,b , 0.1)
        W += -learning_rate * dW
        b += -learning_rate * db
        loss_his.append( loss )
        if i % 10**3 == 0 :
            print('epoch : {}, loss : {}'.format(i,loss))
        params = {
            'W':W,
            'b':b
        }
        grads = {
            'dW':dW,
            'db':db
        }
    return loss_his,params , grads

ridge_loss_his , params , grads = ridge_train( X_train , y_train )

print('lasso final loss is {}'.format( lasso_loss_his[-1]))
print('ridge final loss is {}'.format( ridge_loss_his[-1]))

if __name__ == '__main__' :
    print( "finished!" )
