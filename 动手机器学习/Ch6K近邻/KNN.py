'''
作者：卢沛安
时间：2022年10月27日
'''
from typing import List , Tuple , Dict , Optional
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split

iris = datasets.load_iris()
X , y = iris.data , iris.target
X_train ,  X_test , y_train , y_test = train_test_split( X , y , test_size=0.3 , random_state=13 )
y_train , y_test = y_train.reshape( (-1 , 1) ) , y_test.reshape( (-1 , 1) )


def compute_distances(  X , X_train ) :
    '''
    :param X:  测试样本
    :param X_train: 训练样本
    :return:
    dist: 欧氏距离
    '''
    num_test = X.shape[ 0 ]
    num_train = X_train.shape[ 0 ]
    dists = np.zeros_like( (num_test , num_train) )
    M = np.dot( X , X_train.T )
    te = np.square( X ).sum( axis=1 )
    tr = np.square( X_train ).sum( axis=1 )
    #
    dists = np.sqrt( -2 * M + tr + np.matrix( te ).T )
    return dists

def predict_labels(  y_train , dists , k=1 ) :
    nums_test = dists.shape[ 0 ]
    y_pred = np.zeros( nums_test )
    for i in range( nums_test ) :
        closest_y = [ ]
        '''
        按照欧氏距离矩阵排序后取索引， 并用训练集标签按排序后的索引取值
        最后展平列表
        '''
        labels = y_train[ np.argsort( dists[ i , : ] ) ].flatten()
        closest_y = labels[ 0 :k ]
        # 对最近的k个值进行统计
        c = Counter( closest_y )
        y_pred[ i ] = c.most_common( 1 )[ 0 ][ 0 ]
    return y_pred

dists = compute_distances( X_test , X_train )

y_test_pred = predict_labels( y_train , dists ,k = 1 ).reshape( (-1 , 1) )
# 找出正确实例
num_correct = np.sum( y_test_pred == y_test )
acc = float( num_correct ) / X_test.shape[ 0 ]
print( 'KNN accuracy is {}'.format( acc ) )


num_folds = 5
k_choices = [ 1 , 3 , 5 , 8 , 10 , 12 , 15 , 20 ]
X_train_folds = [ ]
y_train_folds = [ ]
X_train_folds = np.array_split( X_train , num_folds )
y_train_folds = np.array_split( y_train , num_folds )
k_to_acc = {}
for k in k_choices :
    for fold in range( num_folds ) :
        validation_X_test = X_train_folds[ fold ]
        validation_y_test = y_train_folds[ fold ]
        temp_X_train = np.concatenate( X_train_folds[ :fold ] + X_train_folds[ fold + 1 : ] )
        temp_y_train = np.concatenate( y_train_folds[ :fold ] + y_train_folds[ fold + 1 : ] )
        # 计算距离
        temp_dists = compute_distances( validation_X_test , temp_X_train )
        temp_y_test_pred = predict_labels( temp_y_train , temp_dists , k=k ).reshape( (-1 , 1) )
        # 查看准确率
        num_correct = np.sum( temp_y_test_pred == validation_y_test )
        num_test = validation_X_test.shape[ 0 ]
        acc = float( num_correct ) / num_test
        # get.( key , value)
        # 如果无这个key, 返回设定的value
        k_to_acc[ k ] = k_to_acc.get( k , [ ] ) + [ acc ]
        k_to_acc = k_to_acc
        k_choices = [ 1 , 3 , 5 , 8 , 10 , 12 , 15 , 20 ]
for k in sorted( k_to_acc ) :
    for acc in k_to_acc[ k ] :
        print( 'k = {}, acc = {}'.format( k , acc ) )


for k in k_choices :
    acc = k_to_acc[ k ]
    plt.scatter( [ k ] * len( acc ) , acc )
acc_mean = np.array( [ np.mean( v ) for k , v in sorted( k_to_acc.items() ) ] )
acc_std = np.array( [ np.std( v ) for k , v in sorted( k_to_acc.items() ) ] )
plt.errorbar( k_choices , acc_mean , yerr = acc_std)
plt.title( 'CV on k')
plt.xlabel('k')
plt.ylabel('acc')
plt.show( block = True )





if __name__ == '__main__' :
    print( "finished!" )
