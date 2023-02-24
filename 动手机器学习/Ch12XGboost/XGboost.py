'''
作者：卢沛安
时间：2023年02月09日
'''
from typing import List , Tuple , Dict , Optional
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from Ch7决策树.CART_Final import BinaryDecisionTree
from Ch12XGboost.utilis import *
from sklearn.metrics import accuracy_score , mean_squared_error
from sklearn import datasets
from sklearn.model_selection import train_test_split


class XGBoost_Single_Tree( BinaryDecisionTree ) :
    def __init__( self , min_samples_split , min_gini_impurity ,
                  max_depth , loss , regression=False ) :
        super().__init__( min_samples_split , min_gini_impurity ,
                          max_depth , loss )
        self.regression = regression

    # 结点分裂
    def node_split( self , y ) :
        '''

        :param y: np.concatenate( ( y , y_pred ) , axis = 1 )
        :return: y_true , y_pred
        '''
        feature = int( np.shape( y )[ 1 ] / 2 )
        y_true , y_pred = y[ : , : feature ] , y[ : , feature : ]

        return y_true , y_pred

    def gain( self , y , y_pred ) :
        gradient = np.power( (y * self.loss.gradient( y , y_pred )).sum() , 2 )
        hessian = self.loss.hess( y , y_pred ).sum()
        return 0.5 * (gradient / hessian)

    def gain_xgb( self , y , y1 , y2 ) :
        # 结点分裂
        y_true , y_pred = self.node_split( y )
        y1 , y1_pred = self.node_split( y1 )
        y2 , y2_pred = self.node_split( y2 )
        left_gain = self.gain( y1 , y1_pred )
        right_gain = self.gain( y2 , y2_pred )
        gain = self.gain( y_true , y_pred )
        # print( "gain_xgb shape test" , left_gain.shape , right_gain.shape , gain.shape )
        return left_gain + right_gain - gain

    # 计算叶子结点最优权重
    def leaf_weight( self , y ) :
        y_true , y_pred = self.node_split( y )
        # 梯度计算
        if not self.regression :
            gradient = np.sum( y_true * self.loss.gradient( y_true , y_pred ) , axis=0 )
        else :
            gradient = np.sum( self.loss.gradient( y_true , y_pred ) , axis=0 )
        # hessian矩阵计算
        hessian = np.sum( self.loss.hess( y_true , y_pred ) , axis=0 )
        # 叶子结点得分
        leaf_weight = gradient / hessian
        return leaf_weight

    def fit( self , X , y ) :
        self.gini_impurity_calc = self.gain_xgb
        self.leaf_value_calc = self.leaf_weight
        super( XGBoost_Single_Tree , self ).fit( X , y )


class XGboost :
    def __init__( self , n_estimators=5 , learning_rate=0.2 , min_samples_split=2 ,
                  min_gini_impurity=999 , max_depth=2 , regression=False ) :
        self.n_estimators = n_estimators
        self.learning_rate = learning_rate
        self.min_samples_split = min_samples_split
        self.min_gini_impurity = min_gini_impurity
        self.max_depth = max_depth
        self.regression = regression
        if regression :
            self.loss = SquareLoss()
        else :
            self.loss = LogisticLoss()
        self.estimators = [ ]
        for _ in range( n_estimators ) :
            tree = XGBoost_Single_Tree(
                min_samples_split=self.min_samples_split ,
                min_gini_impurity=self.min_gini_impurity ,
                max_depth=self.max_depth ,
                loss=self.loss ,
                regression=self.regression
            )
            self.estimators.append( tree )

    def fit( self , X , y ) :
        if not self.regression :
            y_true_copy = y
            y = cat_label_convert( y )
        y_pred = np.zeros_like( y )
        # 拟合每一棵树后将结果累加
        for i in range( self.n_estimators ) :
            estimator = self.estimators[ i ]
            y_true_pred = np.concatenate( (y , y_pred) , 1 )
            estimator.fit( X , y_true_pred )
            iter_pred = estimator.predict( X )
            y_pred -= np.multiply( self.learning_rate , iter_pred )
            if self.regression :
                mse = mean_squared_error( y , y_pred )
                print( f"at round {i + 1} mse is {round( mse , 2 )}" )
            else :
                y_pred_copy = np.exp( y_pred ) / np.sum( np.exp( y_pred ) , axis=1 , keepdims=True )
                y_pred_copy = np.argmax( y_pred_copy , axis=1 )
                acc = accuracy_score( y_true_copy , y_pred_copy )
                print( f"at round {i + 1} acc is {round( acc , 3 )}" )

    def predict( self , X ) :
        y_pred = None
        for estimator in self.estimators :
            iter_pred = estimator.predict( X )
            if y_pred is None :
                y_pred = np.zeros_like( iter_pred )
            y_pred -= np.multiply( self.learning_rate , iter_pred )
        if not self.regression :
            y_pred = np.exp( y_pred ) / np.sum( np.exp( y_pred ) , axis=1 , keepdims=True )
            y_pred = np.argmax( y_pred , axis=1 )
        return y_pred


## 回归任务
data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv( data_url , sep="\s+" , skiprows=22 , header=None )
data = np.hstack( [ raw_df.values[ : :2 , : ] , raw_df.values[ 1 : :2 , :2 ] ] )
target = raw_df.values[ 1 : :2 , 2 ]
# X , y = data , target
X , y = data_shuffle( data , target )
y = y.reshape( (-1 , 1) )
X_train , X_test , y_train , y_test = train_test_split( X , y , test_size=0.5 )
model = XGboost( n_estimators=3 , learning_rate=0.4 , regression=True )
model.fit( X_train , y_train )
pred = model.predict( X_train )
mse = mean_squared_error( y_train , pred )
print( f'mse of own is {round( mse , 4 )}' )



# 导入鸢尾花数据集
data = datasets.load_iris()
# 获取输入输出
X , y = data.data , data.target
# 数据集划分
X_train , X_test , y_train , y_test = train_test_split( X , y.reshape( (-1 , 1) ) , test_size=0.2 , random_state=43 )

# 创建xgboost分类器

clf = XGboost( n_estimators=6 , learning_rate=0.2 )
# 模型拟合
clf.fit( X_train , y_train )
# 模型预测
y_pred = clf.predict( X_test )
# 准确率评估
accuracy = accuracy_score( y_test , y_pred )
print( "Accuracy: " , accuracy )

if __name__ == '__main__' :
    print( "finished!" )
