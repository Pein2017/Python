'''
作者：卢沛安
时间：2022年10月31日
'''
from typing import List , Tuple , Dict , Optional
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# 导入sklearn模拟二分类数据生成模块
from sklearn.datasets._samples_generator import make_blobs

# 生成模拟二分类数据集
X , y = make_blobs( n_samples=150 , n_features=2 , centers=2 , cluster_std=1.2 , random_state=40 )
# 设置颜色参数
colors = {0 : 'r' , 1 : 'g'}
# 绘制二分类数据集的散点图
plt.scatter( X[ : , 0 ] , X[ : , 1 ] , marker='o' , c=pd.Series( y ).map( colors ) )
plt.show( block=True )
# 将标签转换为1/-1
y_ = y.copy()
y_[ y_ == 0 ] = -1
y_ = y_.astype( float )

from sklearn.model_selection import train_test_split

X_train , X_test , y_train , y_test = train_test_split( X , y_ , test_size=0.3 , random_state=43 )
print( X_train.shape , y_train.shape , X_test.shape , y_test.shape )

from cvxopt import matrix , solvers


class Hard_Margin_SVM :
    def fit( self , X , y ) :
        m , n = X.shape
        # 初始化二次规划变量: P / q / G / h
        self.P = matrix( np.identity( n + 1 , dtype=float ) )
        self.q = matrix( np.zeros( (n + 1) , dtype=float ) )
        self.G = matrix( np.zeros( (m , n + 1) , dtype=float ) )
        self.h = -matrix( np.ones( m , dtype=float ) )

        # 将数据转换为变量：
        self.P[ 0 , 0 ] = 0
        for i in range( m ) :
            self.G[ i , 0 ] = -y[ i ]
            self.G[ i , 1 : ] = -X[ i , : ] * y[ i ]
        sol = solvers.qp( self.P , self.q , self.G , self.h )
        print( "ravel " , np.ravel( sol[ 'x' ] ) )
        # 对 w 和 b 寻优
        self.w = np.zeros( n , )
        self.b = sol[ 'x' ][ 0 ]
        for i in range( 1 , n + 1 ) :
            self.w[ i - 1 ] = sol[ 'x' ][ i ]
        return self.w , self.b

    def predict( self , X ) :
        return np.sign( np.dot( self.w , X.T ) + self.b )


hard_SVM = Hard_Margin_SVM()
hard_SVM.fit( X_train , y_train )
# 模型预测
y_pred = hard_SVM.predict( X_test )
from sklearn.metrics import accuracy_score

# 计算测试集准确率
print( accuracy_score( y_test , y_pred ) )

mean1 , mean2 = np.array( [ 0 , 2 ] ) , np.array( [ 2 , 0 ] )
covar = np.array( [ [ 1.5 , 1.0 ] , [ 1.0 , 1.5 ] ] )
X1 = np.random.multivariate_normal( mean1 , covar , 100 )
y1 = np.ones( X1.shape[ 0 ] )
X2 = np.random.multivariate_normal( mean2 , covar , 100 )
y2 = -1 * np.ones( X2.shape[ 0 ] )
X_train = np.vstack( (X1[ :80 ] , X2[ :80 ]) )
y_train = np.hstack( (y1[ :80 ] , y2[ :80 ]) )
X_test = np.vstack( (X1[ 80 : ] , X2[ 80 : ]) )
y_test = np.hstack( (y1[ 80 : ] , y2[ 80 : ]) )
print( X_train.shape , y_train.shape , X_test.shape , y_test.shape )
# 设置颜色参数
colors = {1 : 'r' , -1 : 'g'}
# 绘制二分类数据集的散点图
plt.scatter( X_train[ : , 0 ] , X_train[ : , 1 ] , marker='o' , c=pd.Series( y_train ).map( colors ) )
plt.show( block=True )


def linear_kernel( x1 , x2 ) :
    return np.dot( x1 , x2 )


class soft_margin_SVM :
    def __init__( self , kernel=linear_kernel , C=None ) :
        self.kernel = kernel
        self.C = C
        if self.C is not None :
            self.C = float( self.C )

    def _gram_matrix( self , X ) :
        m , n = X.shape
        K = np.zeros( (m , m) )
        for i in range( m ) :
            for j in range( m ) :
                K[ i , j ] = self.kernel( X[ i ] , X[ j ] )
        return K

    def fit( self , X , y ) :
        m , n = X.shape
        # 基于线性核计算Gram矩阵
        K = self._gram_matrix( X )
        # 初始化二次规划
        P = matrix( np.outer( y , y ) * K )
        q = matrix( np.ones( m ) * -1 )
        A = matrix( y , (1 , m) )
        b = matrix( 0.0 )

        if self.C is None :
            G = matrix( np.diag( np.ones( m ) * -1 ) )
            h = matrix( np.zeros( m ) )
        else :
            tmp1 = np.diag( np.ones( m ) * -1 )
            tmp2 = np.identity( m )
            G = matrix( np.vstack( (tmp1 , tmp2) ) )
            tmp1 = np.zeros( m )
            tmp2 = np.ones( m ) * self.C
            h = matrix( np.hstack( (tmp1 , tmp2) ) )
        sol = solvers.qp( P , q , G , h , A , b )
        # 拉格朗日乘子
        a = np.ravel( sol[ 'x' ] )
        # 寻找支持向量
        spv = a > 1e-5
        ix = np.arange( len( a ) )[ spv ]
        self.a = a[ spv ]
        self.spv = X[ spv ]
        self.spv_y = y[ spv ]
        print( "{} support vectors out of {} points".format( len( self.a ) , m ) )

        self.b = 0
        for i in range( len( self.a ) ) :
            self.b += self.spv_y[ i ]
            self.b -= np.sum( self.a * self.spv_y * K[ ix[ i ] , spv ] )
        self.b /= len( self.a )

        self.w = np.zeros( n , )
        for i in range( len( self.a ) ) :
            self.w += self.a[ i ] * self.spv_y[ i ] * self.spv[ i ]

    def project( self , X ) :
        if self.w is not None :
            return np.dot( X , self.w ) + self.b

    def predict( self , X ) :
        return np.sign( np.dot( self.w , X.T ) + self.b )


soft_svm = soft_margin_SVM( C=0.1 )
soft_svm.fit( X_train , y_train )
y_pred = soft_svm.predict( X_test )
print( "acc is {}".format( accuracy_score( y_test , y_pred ) ) )

if __name__ == '__main__' :
    print( "finished!" )
