'''
作者：卢沛安
时间：2022年10月05日
'''
from typing import List , Tuple , Dict , Optional


class Solution :
    def search( self , nums: List[ int ] , target: int ) -> int :
        if not nums :
            return -1
        left , right = 0 , len( nums ) - 1

        while left <= right :
            mid = left + (right - left) // 2
            if nums[ mid ] == target :
                return mid

            if nums[ 0 ] <= nums[ mid ] :
                if nums[ left ] <= target < nums[ mid ] :
                    right = mid - 1
                else :
                    left = mid + 1

            else :
                if nums[ mid ] < target <= nums[ right ] :
                    left = mid + 1
                else :
                    right = mid - 1
        return -1


if __name__ == '__main__' :
    s = Solution()
    nums = [3,1]
    target = 1
    print( s.search( nums , target ) )
    print( "finished" )
