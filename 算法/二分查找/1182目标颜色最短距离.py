'''
作者：卢沛安
时间：2023年02月16日
'''
from typing import List , Tuple , Dict , Optional
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from bisect import bisect_left

class Solution :
    def shortestDistanceColor( self , colors: List[ int ] , queries: List[ List[ int ] ] ) -> List[ int ] :
        record = {1 : [ ] , 2 : [ ] , 3 : [ ]}
        for index , col in enumerate( colors ) :
            record[ col ].append( index )
        res = [ ]
        for start , target_color in queries :
            array = record.get( target_color )
            if len( array ) == 0 :
                res.append( -1 )
                continue
            shortest = bisect_left( array , start )
            if shortest == 0 :
                res.append( array[ shortest ] - start )
            elif shortest == len( array ) :
                res.append( start - array[ shortest - 1 ] )
            else :
                ans = min( array[ shortest ] - start , start - array[ shortest - 1 ]  )
                res.append( ans )
        return res


if __name__ == '__main__' :
    print( "finished!" )
