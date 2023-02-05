'''
作者：卢沛安
时间：2022年10月28日
'''
from typing import List , Tuple , Dict , Optional
import numpy as np
from math import log

import numpy as np


### 定义二叉特征分裂函数
def feature_split( X , feature_i , threshold ) :
    split_func = None
    if isinstance( threshold , int ) or isinstance( threshold , float ) :
        split_func = lambda sample : sample[ feature_i ] >= threshold
    else :
        split_func = lambda sample : sample[ feature_i ] == threshold

    X_left = np.array( [ sample for sample in X if split_func( sample ) ] )
    X_right = np.array( [ sample for sample in X if not split_func( sample ) ] )

    return np.array( [ X_left , X_right ] )


### 计算基尼指数
def calculate_gini( y ) :
    # 将数组转化为列表
    y = y.tolist()
    probs = [ y.count( i ) / len( y ) for i in np.unique( y ) ]
    gini = sum( [ p * (1 - p) for p in probs ] )
    return gini


def entropy( ele ) :
    '''

    :param ele: 包含类别取值的列表
    :return: entropy
    '''
    probs = [ ele.count( i ) / len( ele ) for i in set( ele ) ]
    entro = - sum( [ prob * log( prob , 2 ) for prob in probs ] )
    return entro


import pandas as pd


def gini( nums ) :
    probs = [ nums.count( i ) / len( nums ) for i in set( nums ) ]
    gin = sum( [ p * (1 - p) for p in probs ] )
    return gin


def df_split( df , col ) :
    '''

    :param df:  待划分的训练数据
    :param col: 划分数据的依据特征
    :return: res_dict : 根据特征取值划分后的不同数据集字典
    '''
    unique_col_val = df[ col ].unique()
    res_dict = {elem : pd.DataFrame for elem in unique_col_val}
    for key in res_dict.keys() :
        res_dict[ key ] = df[ : ][ df[ col ] == key ]
    '''
    例如Iris数据 
    第一个特征数据 为 长度 
    res_dict :    { 1.2 : dataset1 , 2.4 : dataset2 , 2.5 : dataset3 }
    '''

    return res_dict


def choose_best_feature( df , label ) :
    '''

    :param df: 待划分的训练数据
    :param label: 训练标签
    :return:
    max_value: 最大信息增益
    best_feature: 最优特征
    max_splited: 根据最优特征划分后的数据字典
    '''
    # 计算训练标签的信息熵
    entropy_D = entropy( df[ label ].tolist() )
    # 特征集
    cols = [ col for col in df.columns if col not in [ label ] ]
    # 初始化最大信息增益值、最有特征和划分后的数据集
    max_value , best_feature = float( '-inf' ) , None
    max_splited = None
    # 遍历特征并划分
    for col in cols :
        splited_set = df_split( df , col )
        # 初始化条件熵
        entropy_DA = 0
        '''
        这里的 subset_col 代表着需要遍历的特征的元素，例如长度，1.2， 2.4， 2.5... 由于没有预测函数，这里只在意这个值其对应的dataset的信息增益
        '''
        # 对划分后的数据集 遍历计算
        for subset_col , subset in splited_set.items() :
            # 计算划分后的数据子集的标签信息熵
            entropy_Di = entropy( subset[ label ].tolist() )
            # 计算当前特征的经验条件熵
            entropy_DA += len( subset ) / len( df ) * entropy_Di
        info_gain = entropy_D - entropy_DA
        # 获取最大的信息增益， 并保存对应的特征和划分结果
        if info_gain > max_value :
            max_value , best_feature = info_gain , col
            max_splited = splited_set
    return max_value , best_feature , max_splited


class ID3Tree :
    class TreeNode :
        def __init__( self , name ) :
            self.name = name
            self.connections = {}

        def connect( self , label , node ) :
            self.connections[ label ] = node

    def __init__( self , df , label ) :
        self.columns = df.columns
        self.df = df
        self.label = label
        self.root = self.TreeNode( "Root" )

    def construct_tree( self ) :
        self.construct( self.root , '' , self.df , self.columns )

    def construct( self , parent_node , parent_label , sub_df , columns ) :
        max_value , best_feature , max_splited = choose_best_feature( sub_df[ columns ] , self.label )
        # 如果找不到最优特征，则构造单节点的树
        if not best_feature :
            node = self.TreeNode( sub_df[ self.label ].iloc[ 0 ] )
            parent_node.connect( parent_label , node )
            return
            # 根据最优特征以及子节点构建树
        node = self.TreeNode( best_feature )
        parent_node.connect( parent_label , node )
        new_columns = [ col for col in columns if col != best_feature ]
        # 递归构造
        for splited_value , splited_data in max_splited.items() :
            self.construct( node , splited_value , splited_data , new_columns )


from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = datasets.load_iris()
X , y = data.data , data.target
y = y.reshape( (-1 , 1) )
X_train , X_test , y_train , y_test = train_test_split( X , y , test_size=0.3 )
test = pd.DataFrame( X )
test[ 'target' ] = y

id3_tree = ID3Tree( df=test , label='target' )
id3_tree.construct_tree()
if __name__ == '__main__' :
    print( "finished!" )
