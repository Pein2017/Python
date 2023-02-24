'''
作者：卢沛安
时间：2023年02月06日
'''
from typing import List , Tuple , Dict , Optional
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

from Ch7决策树.CART_Final import TreeNode , feature_split , calculate_gini , RegressionTree , \
    ClassificationTree
from Ch11GBDT.utilis import *
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import accuracy_score


class GBDT( object ) :
    def __init__( self , n_estimators , learning_rate , min_samples_split ,
                  min_gini_impurity , max_depth , regression ) :
        self.n_estimators = n_estimators
        self.learning_rate = learning_rate
        self.min_samples_split = min_samples_split
        self.min_gini_impurity = min_gini_impurity
        self.max_depth = max_depth
        self.regression = regression

        self.loss = SquareLoss()
        # 如果是分类树，则需要定义分类树的损失函数
        if not self.regression :
            self.loss = LogisticLoss()
        self.estimators = [ ]
        for i in range( self.n_estimators ) :
            model_tree = RegressionTree( min_samples_split=self.min_samples_split ,
                                         min_gini_impurity=self.min_gini_impurity ,
                                         max_depth=self.max_depth )
            self.estimators.append(
                model_tree
            )

    def transform_pred( self , y_pred ) :
        temp_pred = np.exp( y_pred ) / np.expand_dims( np.sum( np.exp( y_pred ) , axis=1 ) , axis=1 )
        # 转化为预测标签
        return temp_pred

    def fit( self , X , y ) :
        if not self.regression :
            original_y = y
            y = cat_label_convert( y )
            # y_pred = np.zeros( np.shape( y ) )
        self.estimators[ 0 ].fit( X , y )
        # 第一棵树的预测结果
        y_pred = self.transform_pred( self.estimators[ 0 ].predict( X ) )
        # 前向分步迭代训练
        for i in range( 1 , self.n_estimators ) :
            gradient = self.loss.gradient( y , y_pred )
            self.estimators[ i ].fit( X ,gradient  )
            y_pred -= np.multiply( self.learning_rate , self.transform_pred( self.estimators[ i ].predict( X ) ) )
            if self.regression :
                mse = mean_squared_error( y , y_pred )
                print( f'{i + 1} th round mse is: {round( mse , 4 )}' )
            else :
                # 将预测值转化为概率
                temp_pred = np.exp( y_pred ) / np.expand_dims( np.sum( np.exp( y_pred ) , axis=1 ) , axis=1 )
                # 转化为预测标签
                temp_pred = np.argmax( y_pred , axis=1 )
                acc = accuracy_score( original_y , temp_pred )
                print( f'{i + 1} th round accuracy  is: {round( acc , 4 )}' )

    def predict( self , X ) :
        # 回归树预测
        y_pred = self.estimators[ 0 ].predict( X )
        for i in range( 1 , self.n_estimators ) :
            y_pred -= np.multiply( self.learning_rate , self.estimators[ i ].predict( X ) )
        # 分类树预测
        if not self.regression :
            # 将预测值转化为概率
            y_pred = np.exp( y_pred ) / np.expand_dims( np.sum( np.exp( y_pred ) , axis=1 ) , axis=1 )
            # 转化为预测标签
            y_pred = np.argmax( y_pred , axis=1 )
        return y_pred


class GDBTClassifier( GBDT ) :
    def __init__( self , n_estimators=5 , learning_rate=0.3 , min_samples_split=3 , min_gini_impurity=999 ,
                  max_depth=3 ) :
        super( GDBTClassifier , self ).__init__( n_estimators=n_estimators , learning_rate=learning_rate ,
                                                 min_samples_split=min_samples_split ,
                                                 min_gini_impurity=min_gini_impurity , max_depth=max_depth ,
                                                 regression=False )

    def fit( self , X , y ) :
        # self.leaf_value_calc = self.leaf_weight
        super( GDBTClassifier , self ).fit( X , y )


# 导入鸢尾花数据集
data = datasets.load_iris()
# 获取输入输出
X , y = data.data , data.target
# 数据集划分
X_train , X_test , y_train , y_test = train_test_split( X , y.reshape( (-1 , 1) ) , test_size=0.2 , random_state=43 )
# 创建GDBT分类器
clf = GDBTClassifier( n_estimators=20 , learning_rate=0.2 , min_samples_split=3 )
# 模型拟合
print( y_train.shape )
clf.fit( X_train , y_train )
# 模型预测
y_pred = clf.predict( X_test )
# 准确率评估
accuracy = accuracy_score( y_test , y_pred )
print( "Accuracy: " , accuracy )


class GDBTRegressor( GBDT ) :
    def __init__( self , n_estimators=5 , learning_rate=0.3 , min_samples_split=3 , min_var_reduction=999 ,
                  max_depth=3 ) :
        super( GDBTRegressor , self ).__init__( n_estimators=n_estimators , learning_rate=learning_rate ,
                                                min_samples_split=min_samples_split ,
                                                min_gini_impurity=min_var_reduction , max_depth=max_depth ,
                                                regression=True )


# data_url = "http://lib.stat.cmu.edu/datasets/boston"
# raw_df = pd.read_csv( data_url , sep="\s+" , skiprows=22 , header=None )
# data = np.hstack( [ raw_df.values[ : :2 , : ] , raw_df.values[ 1 : :2 , :2 ] ] )
# target = raw_df.values[ 1 : :2 , 2 ]
# # X , y = data , target
# X , y = data_shuffle( data , target )
# y = y.reshape( (-1 , 1) )
# X_train , X_test , y_train , y_test = train_test_split( X , y , test_size=0.3 )
#
# model = GDBTRegressor( n_estimators=10 , learning_rate=0.1 )
# model.fit( X_train , y_train )
# pred = model.predict( X_train )
# mse = mean_squared_error( y_train , pred )
# print( f'mse of own is {round( mse , 4 )}' )

if __name__ == '__main__' :
    pass
    # from sklearn.ensemble import GradientBoostingRegressor
    #
    # # 创建模型实例
    # reg = GradientBoostingRegressor( n_estimators=3 , learning_rate=0.4 ,
    #                                  max_depth=3 , random_state=0 )
    # # 模型拟合
    # reg.fit( X_train , y_train )
    # # 模型预测
    # y_pred = reg.predict( X_test )
    # # 计算模型预测的均方误差
    # mse = mean_squared_error( y_test , y_pred )
    # print( f'mse of sklearn is {round( mse )}' )
    # print( "finished!" )
