'''
作者：卢沛安
时间：2023年02月21日
'''
from typing import List , Tuple , Dict , Optional
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd


class Solution :
    def trap( self , height: List[ int ] ) -> int :
        if not height :
            return 0
        n = len( height )
        left_max = [ height[ 0 ] ] + [ 0 ] * (n - 1)
        # ans = 0
        right_max = [ 0 ] * (n - 1) + [ height[ n - 1 ] ]
        for i in range( 1 , n ) :
            left_max[ i ] = max( height[ i ] , left_max[ i - 1 ] )
        for i in range( n - 2 , -1 , -1 ) :
            right_max[ i ] = max( height[ i ] , right_max[ i + 1 ] )
        # for i in range( 1 , n - 1 ) :
        #     ans += min( left_max[ i ] , right_max[ i ] ) - height[ i ]
        ans = sum( min( left_max[ i ] , right_max[ i ] ) - height[ i ] for i in range( 1 , n - 1 ) )
        return ans


S = Solution()

height = [ 0 , 1 , 0 , 2 , 1 , 0 , 1 , 3 , 2 , 1 , 2 , 1 ]
S.trap( height )
height = [ 4 , 2 , 0 , 3 , 2 , 5 ]
S.trap( height )
if __name__ == '__main__' :
    print( "finished!" )
