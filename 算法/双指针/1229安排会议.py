'''
作者：卢沛安
时间：2023年02月18日
'''
from typing import List , Tuple , Dict , Optional
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

slots1 = [ [ 10 , 50 ] , [ 60 , 120 ] , [ 140 , 210 ] ]
slots2 = [ [ 0 , 15 ] , [ 60 , 70 ] ]
duration = 8

slots1 = [ [ 10 , 60 ] ]
slots2 = [ [ 12 , 17 ] , [ 21 , 50 ] ]


class Solution :
    def minAvailableDuration( self , slots1: List[ List[ int ] ] , slots2: List[ List[ int ] ] , duration: int ) -> \
            List[ int ] :

        def intersect( s1 , s2 ) :
            start_time = max( s1[ 0 ] , s2[ 0 ] )
            end_time = min( s1[ 1 ] , s2[ 1 ] )
            return end_time - start_time , start_time

        slots1 , slots2 = sorted( slots1 ) , sorted( slots2 )
        p1 , p2 = 0 , 0
        n1 , n2 = len( slots1 ) , len( slots2 )
        while p1 < n1 and p2 < n2 :
            s1 = slots1[ p1 ]
            s2 = slots2[ p2 ]
            time , start_time = intersect( s1 , s2 )
            if time < duration :
                if s1[ 1 ] < s2[ 1 ] :
                    p1 += 1
                else :
                    p2 += 1
            else :
                return [ start_time , (duration + start_time) ]
        return [ ]


sol = Solution()
print( sol.minAvailableDuration( slots1 , slots2 , duration=8 ) )

if __name__ == '__main__' :
    print( "finished!" )
