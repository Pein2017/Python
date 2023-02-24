'''
作者：卢沛安
时间：2023年02月21日
'''
from typing import List , Tuple , Dict , Optional
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from collections import defaultdict

class Solution :
    def lengthOfLongestSubstringKDistinct( self , s: str , k: int ) -> int :
        n = len( s )
        if n <= k :
            return n
        current_window = defaultdict()
        end = 0
        ans = 0
        start = 0
        while end < n :
            # keep adding
            if len( current_window ) <= k :
                element = s[ end ]
                current_window[ element ] = end
                end += 1
            if len( current_window ) > k :
                # remove the left most
                left_idx = min( current_window.values() )
                # del current_window[ s[ left_idx ] ]
                current_window.pop( s[ left_idx ] )
                start = left_idx + 1
            ans = max( ans , end - start )
        return ans


S = Solution()
s = "eceba"
k = 2
S.lengthOfLongestSubstringKDistinct( s , k )
s = "aa"
k = 1
S.lengthOfLongestSubstringKDistinct( s , k )

if __name__ == '__main__' :
    print( "finished!" )
