'''
作者：卢沛安
时间：2022年11月07日
'''
from typing import List , Tuple , Dict , Optional
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

class DecisionStump :
    def __init__( self ) :
        # 基于划分阈值决定样本分类为 1 还是 -1
        self.label = 1
        # 特征索引
        self.feature_index = None
        # 特征划分阈值
        self.threshold = None
        # 指示分类准确率 的值
        self.alpha = None


class Adaboost :
    # 弱分类器
    def __init__( self ,  n_estimators) :
        self.n_estimators = n_estimators

    def fit( self , X: np.array , y: np.array ) :
        m , n = X.shape
        # 初始化权重分布 为 1 / N
        w = np.full( m , (1 / m) )
        w = w.reshape( (-1 ,1 ))
        # 初始化基分类器 列表
        self.estimators = [ ]
        print( "n_estimator is {}".format( self.n_estimators ))
        for _ in range( self.n_estimators ) :
            # 训练一个弱分类器： 决策树桩
            estimator = DecisionStump()
            # 设定一个最小化误差率
            min_error = float( 'inf' )
            # 遍历数据特征，根据最小分类误差选择特征

            for i in range( n ) :
                # 获得特征值
                values = np.expand_dims( X[ : , i ] , axis=1 )
                # 去重
                unique_values = np.unique( values )
                # 尝试将每一个特征值 作为 分类阈值
                for threshold in unique_values :
                    p = 1
                    # 初始化所有预测值为 1
                    pred = np.ones( np.shape( y ) )

                    pred[ X[ :,i ] < threshold ] = - 1

                    # 计算误差率
                    error = sum( w[ y != pred ] )
                    # 如果误差率大于0.5，则进行政府预测的翻转
                    if error > 0.5 :
                        error = 1 - error
                        p = -1

                    # 一旦获得了最小误差率，则保存相关参数
                    if error < min_error :
                        estimator.label = p
                        estimator.threshold = threshold
                        estimator.feature_index = i
                        min_error = error

            # 计算基分类器的权重
            estimator.alpha = 0.5 * np.log( (1.0 - min_error) / (min_error + 1e-9) )
            # 初始化所有预测值为1
            preds = np.ones( np.shape( y ) )
            # 获取所有 小于阈值 的 负类索引
            negative_idx = (estimator.label * X[ : , estimator.feature_index ] < estimator.label * estimator.threshold)
            # 将 负类设为 "-1"
            preds[ negative_idx ] = -1

            w *= np.exp( -estimator.alpha * y * preds )
            w /= np.sum( w )

            self.estimators.append( estimator )

    def predict( self , X ) :
        m = len( X )
        y_pred = np.zeros( (m , 1) )
        for estimator in self.estimators :
            predictions = np.ones( np.shape( y_pred ) )
            negative_idx = (estimator.label * X[ : , estimator.feature_index ] < estimator.label * estimator.threshold)
            # 将负类设为 '-1'
            predictions[ negative_idx ] = -1
            # 对分类器的 预测结果 加权
            y_pred += estimator.alpha * predictions
        y_pred = np.sign( y_pred ).flatten()
        return y_pred


from sklearn.model_selection import train_test_split
# 导入sklearn模拟二分类数据生成模块
from sklearn.datasets import make_blobs

# 生成模拟二分类数据集
X , y = make_blobs( n_samples=500 , n_features=10 , centers=2,
                    cluster_std=3 , random_state=13 )
# 将标签转换为1/-1
y_ = y.copy()
y_[ y_ == 0 ] = -1
y_ = y_.astype( float )
# 训练/测试数据集划分
X_train , X_test , y_train , y_test = train_test_split( X , y_ ,
                                                        test_size=0.3 , random_state=43 )
y_train , y_test = y_train.reshape( (-1 , 1) ) , y_test.reshape( (-1 , 1) )
# 设置颜色参数
colors = {0 : 'r' , 1 : 'g'}
# 绘制二分类数据集的散点图
# plt.scatter( X[ : , 0 ] , X[ : , 1 ] , marker='o' , c=pd.Series( y ).map( colors ) )
# plt.show( block=True );

from sklearn.metrics import accuracy_score

# 创建Adaboost模型实例
clf = Adaboost( n_estimators= 5 )
# 模型拟合
clf.fit( X_train , y_train )
# 模型预测
y_pred = clf.predict( X_test )
# 计算模型预测准确率
accuracy = accuracy_score( y_test , y_pred )
print( "Accuracy of AdaBoost by numpy:" , accuracy )


if __name__ == '__main__' :
    print( "finished!" )
