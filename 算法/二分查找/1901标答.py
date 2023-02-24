'''
作者：卢沛安
时间：2023年02月16日
'''
from typing import List , Tuple , Dict , Optional
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd


class Solution :
    def findPeakGrid( self , mat: List[ List[ int ] ] ) -> List[ int ] :

        m , n = len( mat ) , len( mat[ 0 ] )

        # 找到单列中最大值和其索引
        def getColMax( i: int ) -> (int , int) :
            value , index = mat[ 0 ][ i ] , 0
            for row in range( 1 , m ) :
                if mat[ row ][ i ] > value :
                    value , index = mat[ row ][ i ] , row
            return value , index

        # 二分法切片
        left , right = 0 , n - 1
        while left < right :
            mid = left + int( (right - left) / 2 )
            max_val , max_idx = getColMax( mid )
            if mid == 0 :  # left = 0, right = 1
                if max_val > mat[ max_idx ][ 1 ] :
                    return [ max_idx , 0 ]
                else :
                    left = 1
            else :
                if mat[ max_idx ][ mid - 1 ] < max_val and mat[ max_idx ][ mid + 1 ] < max_val :
                    return [ max_idx , mid ]
                elif mat[ max_idx ][ mid - 1 ] < max_val < mat[ max_idx ][ mid + 1 ] :
                    left = mid + 1
                else :
                    right = mid - 1

        # 对于最后剩下的一列，其最大值一定是极大值
        _ , idx = getColMax( left )
        return [ idx , left ]


if __name__ == '__main__' :
    print( "finished!" )
