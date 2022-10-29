'''
作者：卢沛安
时间：2022年10月27日
'''
from typing import List , Tuple , Dict , Optional
import numpy as np


class LDA :
    def __int__( self ) :
        self.w = None

    def calculate_cov( self , X  , Y=None ) :
        m = X.shape[ 0 ]
        # 数据标准化
        X = (X - np.mean( X , axis=0 )) / np.std( X , axis=0 )
        Y = X if Y == None else (Y - np.mean( Y , axis=0 )) / np.std( Y , axis=0 )
        return 1 / m * np.matmul( X.T , Y )

    def fit( self , X , y ) :
        # (1)按组分类
        X0 = X[ y == 0 ]
        X1 = X[ y == 1 ]
        # (2)计算协方差
        sigma0 = self.calculate_cov( X0 )
        sigma1 = self.calculate_cov( X1 )
        # (3)类内散度 Sw
        Sw = sigma0 + sigma1
        # (4) 两类数据的均值和均值差
        u0 , u1 = np.mean( X0 , axis=0 ) , np.mean( X1 , axis=0 )
        mean_diff = np.atleast_1d( u0 - u1 )  # 转换成至少是1维的数组 [ X ]   at_least_2d 则是 [ [X] ]
        # (5) 奇异值分解
        U , S , V = np.linalg.svd( Sw )
        # (6) 求逆
        Sw_inverse = np.dot( np.dot( V.T , np.linalg.pinv( np.diag( S ) ) ) , U.T )  # pinv 求伪逆矩阵
        # (7) 计算W
        # print( Sw_inverse.shape  )
        # print(  mean_diff.shape)
        self.w = Sw_inverse.dot( mean_diff )

    def project( self , X , y ) :
        self.fit( X , y )
        X_projection = X.dot( self.w )
        return X_projection

    def predict( self , X: List[ List[ float ] ] ) :
        y_pred = [ ]
        for x_i in X :
            h = x_i.dot( self.w )
            y = 1 * (h < 0)
            y_pred.append( y )
        return y_pred


from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = datasets.load_iris()
X , y = data.data , data.target
# 取标签不为2的数据
X = X[ y != 2 ]
y = y[ y != 2 ]
X_train , X_test , y_train , y_test = train_test_split( X , y , test_size=0.2 , random_state=41 )
lda = LDA()
lda.fit( X_train , y_train )
y_pred = lda.predict( X_test )
acc = accuracy_score( y_test , y_pred )
print( 'Accuracy is {}'.format( acc ) )

# sklearn module
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
clf = LinearDiscriminantAnalysis()
clf.fit( X_train,y_train)
y_pred = clf.predict( X_test)
acc = accuracy_score( y_test , y_pred )
print( 'Accuracy is {} on sklearn module '.format( acc ) )
if __name__ == '__main__' :
    print( "finished!" )
