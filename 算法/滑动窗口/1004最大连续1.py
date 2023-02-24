'''
作者：卢沛安
时间：2023年02月22日
'''
from typing import List , Tuple , Dict , Optional
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd


class Solution :
    def longestOnes( self , nums: List[ int ] , k: int ) -> int :

        n = len( nums )
        if n <= k :
            return n
        left , right = 0 , 0
        res = 0
        zero_count = 0
        while right < n :

            # 进窗口
            if not nums[ right ] :
                zero_count += 1
            while zero_count > k :
                if nums[ left ] :
                    pass
                else :
                    zero_count -= 1
                left += 1
            res = max( res , right - left + 1 )
            right += 1
        return res


S = Solution()

nums = [ 1 , 1 , 1 , 0 , 0 , 0 , 1 , 1 , 1 , 1 , 0 ]
K = 2
S.longestOnes( nums , K )
nums = [ 0 , 0 , 1 , 1 , 0 , 0 , 1 , 1 , 1 , 0 , 1 , 1 , 0 , 0 , 0 , 1 , 1 , 1 , 1 ]
K = 3
S.longestOnes( nums , K )
if __name__ == '__main__' :
    print( "finished!" )
