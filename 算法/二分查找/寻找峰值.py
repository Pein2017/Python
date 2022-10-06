'''
作者：卢沛安
时间：2022年10月06日
'''
from typing import List , Tuple , Dict , Optional


class Solution :
    def findPeakElement( self , nums: List[ int ] ) -> int :
        if len( nums ) == 1 :
            return 0
        n = len( nums )
        left , right = 0 , n - 1
        while left != right :
            mid = left + (right - left) // 2

            if nums[ mid ] < nums[ mid + 1 ] :
                left = mid + 1
            else :
                right = mid
        return left


if __name__ == '__main__' :
    nums = [ 1 , 2 , 3 , 1 ]
    print( Solution().findPeakElement( nums ) )
    print( "" )
    print( "finished!" )
