'''
作者：卢沛安
时间：2023年02月05日
'''
from typing import List , Tuple , Dict , Optional
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error


# 定义树节点
class TreeNode :
    def __init__( self , feature_ix=None , splitted_value=None ,
                  leaf_value=None , left_branch=None , right_branch=None ) :
        self.feature_ix = feature_ix
        self.splitted_value = splitted_value
        self.leaf_value = leaf_value
        self.left_branch = left_branch
        self.right_branch = right_branch


def feature_split( X , feature_i , splitted_value ) :
    split_func = None
    if isinstance( splitted_value , int ) or isinstance( splitted_value , float ) :
        split_func = lambda sample : sample[ feature_i ] <= splitted_value
    else :
        split_func = lambda sample : sample[ feature_i ] == splitted_value
    X_left = np.array( [ sample for sample in X if split_func( sample ) ] )
    X_right = np.array( [ sample for sample in X if not split_func( sample ) ] )

    return np.array( [ X_left , X_right ] )


def calculate_gini( y ) :
    # 将数组转化为列表
    y = y.tolist()
    probs = [ y.count( i ) / len( y ) for i in np.unique( y ) ]
    gini = sum( [ p * (1 - p) for p in probs ] )
    return gini


class BinaryDecisionTree :
    def __init__( self , min_samples_split=3 , mini_gini_impurity=999 ,
                  max_depth=float( "inf" ) , loss=None ) :
        self.root = None
        self.min_samples_split = min_samples_split
        self.mini_gini_impurity = mini_gini_impurity
        self.max_depth = max_depth
        self.loss = loss

        self.gini_impurity_calc = None
        self.leaf_value_calc = None

    def _construct_tree( self , X , y , current_depth=0 ) :
        best_gini_impurity = 999
        # 初始化最优特征索引和阈值
        best_criteria = None
        best_sets = None

        Xy = np.concatenate( (X , y) , axis=1 )
        m , n = X.shape

        if m >= self.min_samples_split and current_depth <= self.max_depth :
            for f_i in range( n ) :
                # f_i : int 代表第几列的特征
                f_values = np.expand_dims( X[ : , f_i ] , axis=1 )
                unique_values = np.unique( f_values )

                for splitted_value in unique_values :
                    Xy1 , Xy2 = feature_split( Xy , f_i , splitted_value )

                    if len( Xy1 ) != 0 and len( Xy2 ) != 0 :
                        # 获取两个自己的标签值
                        #  Xy[: , n ] 则维度只剩下一维 ( m, )
                        #  Xy[: , n : ] 维度为 (m * 1)
                        y1 = Xy1[ : , n : ]
                        y2 = Xy2[ : , n : ]

                        impurity = self.gini_impurity_calc( y , y1 , y2 )
                        if impurity < best_gini_impurity :
                            best_gini_impurity = impurity
                            best_criteria = {"feature_index" : f_i , "splitted_value" : splitted_value}
                            best_subsets = {
                                "leftX" : Xy1[ : , :n ] ,
                                "rightX" : Xy2[ : , :n ] ,
                                "lefty" : Xy1[ : , n : ] ,
                                "righty" : Xy2[ : , n : ]
                            }

        if best_gini_impurity < self.mini_gini_impurity :
            left_branch = self._construct_tree( best_subsets[ 'leftX' ] , best_subsets[ 'lefty' ] , current_depth + 1 )
            right_branch = self._construct_tree( best_subsets[ 'rightX' ] , best_subsets[ 'righty' ] ,
                                                 current_depth + 1 )
            return TreeNode( feature_ix=best_criteria[ 'feature_index' ] ,
                             splitted_value=best_criteria[ 'splitted_value' ] ,
                             left_branch=left_branch , right_branch=right_branch
                             )
        leaf_value = self.leaf_value_calc( y )
        return TreeNode( leaf_value=leaf_value )

    def predict_value( self , x , tree=None ) :
        if tree is None :
            tree = self.root
        if tree.leaf_value is not None :
            return tree.leaf_value

        feature_value = x[ tree.feature_ix ]
        branch = tree.right_branch
        if isinstance( feature_value , int ) or isinstance( feature_value , float ) :
            if feature_value <= tree.splitted_value :
                branch = tree.left_branch
        elif feature_value == tree.splitted_value :
            branch = tree.left_branch

        return self.predict_value( x , branch )

    def predict( self , X ) :
        y_pred = np.array( [ self.predict_value( sample ) for sample in X ] )
        return y_pred

    def fit( self , X , y , loss=None ) :
        self.root = self._construct_tree( X , y )
        self.loss = None


class ClassificationTree( BinaryDecisionTree ) :
    #  y：所有数据 , y1: 左子树的数据 , y2: 右子树的数据
    def _calculate_gini_impurity( self , y , y1 , y2 ) :
        p = len( y1 ) / len( y )
        gini = calculate_gini( y )
        gini_impurity = p * calculate_gini( y1 ) + (1 - p) * calculate_gini( y2 )
        return gini_impurity

    def _majority_vote( self , y ) :
        most_common = None
        max_count = 0
        for label in np.unique( y ) :
            count = len( y[ y == label ] )
            if count > max_count :
                most_common = label
                max_count = count
        # print( f'majority vote {most_common}' )
        return most_common

    def fit( self , X , y ) :
        self.gini_impurity_calc = self._calculate_gini_impurity
        self.leaf_value_calc = self._majority_vote
        super( ClassificationTree , self ).fit( X , y )


class RegressionTree( BinaryDecisionTree ) :
    # 计算减少方差
    # y：所有数据 , y1: 左子树的数据 , y2: 右子树的数据
    def _calculate_var_reduction( self , y , y1 , y2 ) :
        var_total = np.var( y , axis=0 )
        var_y1 = np.var( y1 , axis=0 )
        var_y2 = np.var( y2 , axis=0 )
        frac_1 = len( y1 ) / len( y )
        frac_2 = len( y2 ) / len( y )
        var_reduction = var_total - (frac_1 * var_y1 + frac_2 * var_y2)
        return sum( var_reduction )

    # 取节点平均
    def _mean_of_y( self , y ) :
        value = np.mean( y , axis=0 )
        return value if len( value ) > 1 else value[ 0 ]

    # 回归树拟合
    def fit( self , X , y ) :
        self.gini_impurity_calc = self._calculate_var_reduction
        self.leaf_value_calc = self._mean_of_y
        super( RegressionTree , self ).fit( X , y )


from sklearn import datasets

data = datasets.load_iris()
X , y = data.data , data.target
X_train , X_test , y_train , y_test = train_test_split( X , y.reshape( -1 , 1 ) , test_size=0.3 )
clf = ClassificationTree()
clf.fit( X_train , y_train )
y_pred = clf.predict( X_test )
acc_own = accuracy_score( y_test , y_pred )

from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier()
clf.fit( X_train , y_train )
y_pred = clf.predict( X_test )
acc_sklearn = accuracy_score( y_test , y_pred )

print( f"accuracy of classification of own is {acc_own}, sklearn is {acc_sklearn}" )

data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv( data_url , sep="\s+" , skiprows=22 , header=None )
data = np.hstack( [ raw_df.values[ : :2 , : ] , raw_df.values[ 1 : :2 , :2 ] ] )
target = raw_df.values[ 1 : :2 , 2 ]
X , y = data , target
y = y.reshape( (-1 , 1) )
X_train , X_test , y_train , y_test = train_test_split( X , y , test_size=0.3 )
reg = RegressionTree()
reg.fit( X_train , y_train )
y_pred = reg.predict( X_test )
mse1 = mean_squared_error( y_test , y_pred )
from sklearn.tree import DecisionTreeRegressor
reg = DecisionTreeRegressor()
reg.fit(X_train, y_train)
y_pred = reg.predict(X_test)
mse2 = mean_squared_error(y_test, y_pred)
print( f"mse of own is {round( mse1 , 2 )}, sklearn is {round( mse2 , 2 )}" )

if __name__ == '__main__' :
    print( "finished!" )
