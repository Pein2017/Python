'''
作者：卢沛安
时间：2022年10月06日
'''
from typing import List , Tuple , Dict , Optional


class Solution :
    def searchRange( self , nums: List[ int ] , target: int ) -> List[ int ] :
        def search( nums: List[ int ] , target: int ) -> int :
            left , right = 0 , len( nums ) - 1
            while left <= right :
                mid = left + (right - left) // 2
                if nums[ mid ] < target :
                    left = mid + 1
                else :
                    right = mid - 1
            return left

        left_index = search( nums , target )
        right_index = search( nums , target + 1 ) - 1

        if left_index == len( nums ) or nums[ left_index ] != target :
            return [ -1 , -1 ]
        else :
            return [ left_index , right_index ]


if __name__ == '__main__' :
    nums = [ 5 , 7 , 7 , 8 , 8 , 10 ]
    target = 8
    nums = [ 2 , 2 ]
    target = 3
    s = Solution()
    print( s.searchRange( nums , target ) )
    print( "finished" )
