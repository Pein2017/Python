'''
作者：卢沛安
时间：2022年10月06日
'''
from typing import List , Tuple , Dict , Optional


class Solution :
    def findMin( self , nums: List[ int ] ) -> int :
        if len( nums ) == 1 :
            return nums[ 0 ]
        n = len( nums )
        left , right = 0 , n - 1
        while left != right :
            mid = left + (right - left) // 2
            print( "left {} , mid {}, right {}".format( left , mid , right))
            if nums[mid] > nums[ right ]:
                left = mid + 1
            elif nums[ mid ] < nums[right]:
                right = mid

        return nums[left]
if __name__ == '__main__' :
    nums = [5,1,2,3,4]
    s = Solution()
    print( s.findMin( nums ) )

    print( "finished" )
