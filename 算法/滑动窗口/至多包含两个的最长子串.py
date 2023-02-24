'''
作者：卢沛安
时间：2022年10月30日
'''
from typing import List , Tuple , Dict , Optional
import numpy as np
from collections import defaultdict

s = "abaccc"


class Solution :
    def lengthOfLongestSubstringTwoDistinct( self , s: str ) -> int :
        k = 3
        n = len( s )
        if n < k  :
            return n
        current_window = defaultdict()
        end = 0
        ans = 0
        start = 0
        while end < n :
            # keep adding
            if len( current_window ) < k  :
                element = s[ end ]
                current_window[ element ] = end
                end += 1
            if len( current_window ) == k  :
                # remove the left most
                left_idx = min( current_window.values() )
                # del current_window[ s[ left_idx ] ]
                current_window.pop( s[ left_idx ] )
                start = left_idx + 1
            ans = max( ans , end - start  )
        return ans


S = Solution()
s = "ccaabbb"
S.lengthOfLongestSubstringTwoDistinct( s )
s = "eceba"
S.lengthOfLongestSubstringTwoDistinct( s )
if __name__ == '__main__' :
    print( "finished!" )
