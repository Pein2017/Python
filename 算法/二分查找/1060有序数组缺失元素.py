'''
作者：卢沛安
时间：2023年02月15日
'''
from typing import List , Tuple , Dict , Optional
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd


def missing( idx ) :
    ans = nums[ idx ] - nums[ 0 ] - idx
    return ans


def sol1( nums , k ) :
    n = len( nums )
    left , right = 0 , n - 1
    if k > missing( right ) :
        return nums[ right ] + (k - missing( right ))
    while left < right :
        mid = (left + right) // 2
        miss = missing( mid )
        if miss < k :
            left = mid + 1
        else :
            right = mid
    ans = nums[ left - 1 ] + (k - missing( left - 1 ))


def sol2( nums , k ) :
    n = len( nums )
    left , right = 0 , n - 1
    if k > missing( right ) :
        return nums[ right ] + (k - missing( right ))

    def a( left , right , k ) :
        if left == right :
            return nums[ left - 1 ] + (k - missing( left - 1 ))
        mid = (left + right) // 2

        if missing( mid ) < k :
            return a( mid + 1 , right , k )
        else :
            return a( left , mid , k )

    return a( left , right , k )


nums = [ 4 , 7 , 9 , 10 ]
k = 3
print( sol2( nums , k ) )

if __name__ == '__main__' :
    print( "finished!" )
