'''
作者：卢沛安
时间：2022年10月28日
'''
from typing import List , Tuple , Dict , Optional
import numpy as np
from 动手机器学习.Ch7决策树.ID3 import feature_split
from 动手机器学习.Ch7决策树.ID3 import calculate_gini


class TreeNode :
    def __init__( self , feature_ix=None , threshold=None ,
                  leaf_value=None , left_bracnh=None , right_branch=None ) :
        self.feature_ix = feature_ix
        self.threshold = threshold
        self.leaf_value = leaf_value
        self.left_branch = left_bracnh
        self.right_branch = right_branch


class BinaryDecisionTree :
    def __init__( self , min_samples_split=3 , mini_gini_impurity=999 ,
                  max_depth=float( 'inf' ) , loss=None ) :
        self.root = None
        self.min_samples_split = min_samples_split
        self.min_gini_impurity = mini_gini_impurity
        self.max_depth = max_depth
        # 基尼不纯度计算函数
        self.gini_impurity_calc = None
        # 叶子结点的值预测函数
        self.leaf_value_calc = None
        self.loss = loss

    def fit( self , X , y , loss=None ) :
        self.root = self._construct_tree( X , y )

    def _construct_tree( self , X , y , current_depth=0 ) :
        init_gini_impurity = 9999
        best_criteria = None
        best_sets = None

        # 合并输入和标签
        Xy = np.concatenate( (X , y) , axis=1 )
        # 获取样本数和特征数
        m , n = X.shape

        # 设置决策树构建条件
        # 训练样本量大于结点最小分裂样本数且当前深度小于最大深度
        if m >= self.min_samples_split and current_depth <= self.max_depth :
            # 遍历计算每个特征的gini impurity
            for f_i in range( n ) :
                f_values = np.expand_dims( X[ : , f_i ] , axis=1 )
                unique_values = np.unique( f_values )

                #遍历取值并寻找最优特征分裂阈值
                for threshold in unique_values:
                    Xy1 , Xy2 = feature_split( Xy)


if __name__ == '__main__' :
    print( "finished!" )
