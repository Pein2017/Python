'''
作者：卢沛安
时间：2023年02月22日
'''
from typing import List , Tuple , Dict , Optional
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

import collections

nums = [ 1 , 3 , -1 , -3 , 5 , 3 , 6 , 7 ]
k = 3

nums = [ 7 , 2 , 4 ]
k = 2


class Solution :
    def maxSlidingWindow( self , nums: List[ int ] , k: int ) -> List[ int ] :
        n = len( nums )
        q = [ ]
        for i in range( k ) :
            while q and nums[ i ] >= nums[ q[ -1 ] ] :
                q.pop( -1 )
            q.append( i )

        ans = [ nums[ q[ 0 ] ] ]
        for i in range( k , n ) :
            while q and nums[ i ] >= nums[ q[ -1 ] ] :
                q.pop( -1 )
            q.append( i )
            while q[ 0 ] <= i - k :
                q.pop( 0 )
            ans.append( nums[ q[ 0 ] ] )

        return ans


class Solution :
    def maxSlidingWindow( self , nums: List[ int ] , k: int ) -> List[ int ] :
        n = len( nums )
        if n <= k :
            return [ max( nums ) ]
        if k == 1 :
            return nums

        # 初始化窗口
        windows = [ ]
        res = [ ]
        left , right = 0 , 0
        while right < k :
            if not windows :
                windows.append( right )
            else :
                if nums[ windows[ -1 ] ] > nums[ right ] :
                    windows.append( right )
                else :
                    while nums[ windows[ -1 ] ] < nums[ right ] :
                        windows.pop( -1 )
                        if not windows :
                            break
                    windows.append( right )
            right += 1
        res.append( nums[ windows[ 0 ] ] )
        if windows[ 0 ] == left :
            windows.pop( 0 )
        left += 1
        while right < n :
            # print( windows )

            if nums[ windows[ -1 ] ] > nums[ right ] :
                windows.append( right )
            else :
                while nums[ windows[ -1 ] ] < nums[ right ] :
                    windows.pop( -1 )
                    if not windows :
                        break
                windows.append( right )
            res.append( nums[ windows[ 0 ] ] )
            if windows[ 0 ] == left :
                windows.pop( 0 )

            left += 1
            right += 1
        return res


S = Solution()
print( S.maxSlidingWindow( nums , k ) )

if __name__ == '__main__' :
    print( "finished!" )
