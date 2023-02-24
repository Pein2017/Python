'''
作者：卢沛安
时间：2023年02月16日
'''
from typing import List , Tuple , Dict , Optional
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

mat = [ [ 7 , 44 , 15 , 31 , 2 , 40 , 36 ] , [ 21 , 40 , 42 , 5 , 41 , 30 , 45 ] , [ 20 , 42 , 27 , 8 , 9 , 3 , 20 ] ,
        [ 32 , 8 , 7 , 16 , 35 , 9 , 25 ] , [ 30 , 24 , 43 , 48 , 45 , 35 , 27 ] , [ 38 , 48 , 47 , 10 , 27 , 42 , 7 ] ,
        [ 32 , 40 , 27 , 18 , 3 , 45 , 24 ] , [ 14 , 29 , 16 , 24 , 7 , 44 , 35 ] ]

mat = [ [ 1 , 2 , 6 ] , [ 3 , 4 , 5 ] ]

mat =[[1,2,3,4,5,6,7,8],[2,3,4,5,6,7,8,9],[3,4,5,6,7,8,9,10],[4,5,6,7,8,9,10,11]]


def findPeakGrid( mat ) :
    # mat = np.array( mat )
    m , n = len( mat ) , len( mat[ 0 ] )
    # getmax = lambda x : (x.argmax() , x.max())
    def getmax( col ) :
        max_value , max_row = mat[ 0 ][ col ] , 0
        for row in range( 1 , m ) :
            if mat[ row ][ col ] > max_value :
                max_value , max_row = mat[ row ][ col ] , row
        return max_row , max_value
    left , right = 0 , n - 1
    while left <= right :
        mid = (left + right) // 2
        max_row , max_value = getmax( mid )
        if mid != left :
            mid_left , mid_right = mat[ max_row ][ mid - 1 ] , mat[ max_row ][ mid + 1 ]
            if max_value > mid_left and max_value > mid_right :
                return [ max_row , mid ]
            elif mid_left < max_value and max_value < mid_right :
                left = mid + 1
            else :
                right = mid - 1
        else :
            a , b = mat[ max_row ][ left ] , mat[ max_row ][ right ]
            if a < b :
                left = right
            break
    max_row , max_value = getmax( left )
    return [ max_row , left ]


findPeakGrid( mat )

if __name__ == '__main__' :
    print( "finished!" )
