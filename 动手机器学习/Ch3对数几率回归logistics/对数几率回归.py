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
    y_hat = sigmod( np.dot( X , W ) + b )
    # 交叉损失
    cost = -1 / num_train * np.sum( y * np.log( y_hat ) + (1 - y) * np.log( 1 - y_hat ) )
    # 权重梯度
    dW = np.dot( X.T , (y_hat - y) ) / num_train
    db = np.sum( y_hat - y ) / num_train
    # 压缩LOSS数组维度
    cost = np.squeeze( cost )
    return y_hat , cost , dW , db


def logistic_train( X , y , learning_rate=0.01 , epochs=10 ** 4 ) :
    '''
    :param X:
    :param y:
    :param learning_rate:
    :param epochs:
    :return:
    cost_list , params , grads
    '''
    W , b = initialize_params( X.shape[ 1 ] )
    cost_list = [ ]
    for i in range( epochs ) :
        a , cost , dW , db = logistic( X , y , W , b )
        W += -learning_rate * dW
        b += -learning_rate * db
        if i % 10 ** 2 :
            cost_list.append( cost )
            print( 'epoch : {} , cost : {}'.format( i , cost ) )
        params = {
            'W' : W ,
            'b' : b
        }
        grads = {
            'dW' : dW ,
            'db' : db
        }
    return cost_list , params , grads


def predict( X , params ) :
    y_pred = sigmod( np.dot( X , params[ 'W' ] ) + params[ 'b' ] )
    for i in range( len( y_pred ) ) :
        if y_pred[ i ] > 0.5 :
            y_pred[ i ] = 1
        else :
            y_pred[ i ] = 0
    return y_pred


import matplotlib.pyplot as plt
# 生成模拟二分类数据集并可视化
from sklearn.datasets._samples_generator import make_classification

# 生成 100 * 2 的数据集
X , labels = make_classification(
    n_samples=100 ,
    n_features=2 ,
    n_redundant=0 ,
    n_informative=2 ,
    random_state=1 ,
    n_clusters_per_class=2
)
rng = np.random.RandomState( 2 )
X += 2 * rng.uniform( size=X.shape )
# 标签类别数
unique_labels = set( labels )
# 根据标签类别设置颜色
colors = plt.cm.Spectral( np.linspace( 0 , 1 , len( unique_labels ) ) )
# 绘制模拟的散点图
for k , col in zip( unique_labels , colors ) :
    x_k = X[ labels == k ]
    plt.plot( x_k[ : , 0 ] , x_k[ : , 1 ] , 'o' ,
              markerfacecolor=col ,
              markeredgecolor='k' ,
              markersize=14
              )
plt.title( 'Simulated binary data set' )
plt.show( block=True )

offset = int( X.shape[ 0 ] * 0.8 )
X_train , y_train = X[ :offset ] , labels[ :offset ]
X_test , y_test = X[ offset : ] , labels[ offset : ]
y_train , y_test = y_train.reshape( (-1 , 1) ) , y_test.reshape( (-1 , 1) )

cost_list , params , grads = logistic_train( X_train , y_train )
y_pred = predict( X_test , params )
plt.plot( cost_list )
plt.show( block=True )
# 测试集准确性
from sklearn.metrics import classification_report

print( classification_report( y_test , y_pred ) )


# 绘制决策边界
def plot_decision_boundary( X_train , y_train , params ) :
    n = X_train.shape[ 0 ]
    xcord1 , ycord1 , xcord2 , ycord2 = [ ] , [ ] , [ ] , [ ]
    for i in range( n ) :
        if y_train[ i ] == 1 :
            xcord1.append( X_train[ i ][ 0 ] )
            ycord1.append( X_train[ i ][ 1 ] )
        else :
            xcord2.append( X_train[ i ][ 0 ] )
            ycord2.append( X_train[ i ][ 1 ] )
    fig = plt.figure()
    ax = fig.add_subplot( 111 )
    # 绘制两类散点图， 以不同颜色表示
    ax.scatter( xcord1 , ycord1 , s=32 , c='red' )
    ax.scatter( xcord2 , ycord2 , s=32 , c='green' )
    # 取值范围
    x = np.arange( -1.5 , 3 , 0.05 )
    # 决策边界公式
    y = (-params[ 'b' ] - params[ 'W' ][ 0 ] * x) / params[ 'W' ][ 1 ]
    ax.plot( x , y )
    plt.xlabel( 'X1' )
    plt.ylabel( 'X2' )
    plt.show( block=True )


plot_decision_boundary( X_train , y_train , params )

if __name__ == '__main__' :
    print( "finished!" )
