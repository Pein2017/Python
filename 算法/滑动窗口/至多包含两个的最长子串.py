'''
作者：卢沛安
时间：2022年10月30日
'''
from typing import List , Tuple , Dict , Optional
import numpy as np

s = "abaccc"


def lengthOfLongestSubstringTwoDistinct( s: str ) -> int :
    n = len( s )
    if n <= 2 :
        return s
    i = 0
    current_windows = [ ]
    current_set = set()
    ans = [ ]
    while i < n :
        # expand windows
        while len( current_set ) <= 2 and i < n :
            current_set.add( s[ i ] )
            current_windows.append( s[ i ] )
            i += 1
        if len( current_set ) > 2 :
            if len( current_windows ) - 1 > len( ans ) :
                ans = current_windows[ :-1 ]
        else :
            if len( current_windows ) > len( ans ) :
                ans = current_windows
        # print( i , ans )
        # reduce windows
        while len( current_set ) > 2 :
            current_windows.pop(0)
            current_set = set( current_windows )
    return len( ans )

print( lengthOfLongestSubstringTwoDistinct( s ) )
if __name__ == '__main__' :
    print( "finished!" )
