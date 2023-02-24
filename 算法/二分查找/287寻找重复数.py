'''
作者：卢沛安
时间：2023年02月20日
'''
from typing import List , Tuple , Dict , Optional
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd


class Solution :
    def findDuplicate( self , nums: List[ int ] ) -> int :
        n = len( nums )
        slow , fast = 0 , 0
        p1 = nums[ slow ]
        p2 = nums[ p1 ]
        while p1 != p2 :
            p1 = nums[ p1 ]
            p2 = nums[ nums[ p2 ] ]
        p1 = 0
        while p1 != p2:
            p1 = nums[p1]
            p2 = nums[p2]
        return p1




class Solution :
    def findDuplicate( self , nums: List[ int ] ) -> int :
        n = len( nums )
        left , right = 1 , n - 1

        def counting( target ) :
            res = 0
            for num in nums :
                if num <= target :
                    res += 1
            return res

        while left < right :
            mid = left + (right - left) // 2
            if counting( mid ) > mid :
                right = mid
            else :
                left = mid + 1
        return right


nums = [ 4 , 3 , 1 , 4 , 2 ]
s = Solution()
s.findDuplicate( nums )

nums = [ 3 , 1 , 3 , 4 , 2 ]

if __name__ == '__main__' :
    print( "finished!" )
