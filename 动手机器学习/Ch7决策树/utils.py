'''
作者：卢沛安
时间：2023年02月09日
'''
from typing import List , Tuple , Dict , Optional
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd


def feature_split( X , feature_i , splitted_value ) :
    split_func = None
    if isinstance( splitted_value , int ) or isinstance( splitted_value , float ) :
        split_func = lambda sample : sample[ feature_i ] < splitted_value
    else :
        split_func = lambda sample : sample[ feature_i ] == splitted_value
    X_left = np.array( [ sample for sample in X if split_func( sample ) ] )
    X_right = np.array( [ sample for sample in X if not split_func( sample ) ] )

    return np.array( [ X_left , X_right ]  )


def calculate_gini( y ) :
    # 将数组转化为列表
    y = y.tolist()
    probs = [ y.count( i ) / len( y ) for i in np.unique( y ) ]
    gini = sum( [ p * (1 - p) for p in probs ] )
    return gini



if __name__ == '__main__' :
    print( "finished!" )
