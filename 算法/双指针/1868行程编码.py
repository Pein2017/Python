'''
作者：卢沛安
时间：2023年02月21日
'''
from typing import List , Tuple , Dict , Optional
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd


class Solution :
    def findRLEArray( self , encoded1: List[ List[ int ] ] , encoded2: List[ List[ int ] ] ) -> List[ List[ int ] ] :
        n1 , n2 = len( encoded1 ) , len( encoded2 )
        i , j = 0 , 0
        res = [ ]
        while i < n1 and j < n2 :
            # case 1  元素频率相同，直接乘
            array1 , array2 = encoded1[ i ] , encoded2[ j ]
            if array1[ 1 ] == array2 :
                prod = array1[ 0 ] * array2[ 0 ]
                freq = array1[ 1 ]
            else :
                # case 2  合并元素频率小的那个
                prod = array1[ 0 ] * array2[ 0 ]
                if array1[ 1 ] < array2[ 1 ] :
                    freq = array1[ 1 ]
                    encoded2[ j ][ 1 ] -= freq
                    i += 1
                    if encoded2[ j ][ 1 ] == 0 :
                        j += 1
                else :
                    freq = array2[ 1 ]
                    encoded1[ i ][ 1 ] -= freq
                    j += 1
                    if encoded1[ i ][ 1 ] == 0 :
                        i += 1
            temp_ans = [ prod , freq ]
            if len( res ) >= 1 :
                if res[ -1 ][ 0 ] == prod :
                    res[ -1 ][ 1 ] += freq
                else :
                    res.append( temp_ans )
            else :
                res.append( temp_ans )
        return res


encoded1 =  [[1,3],[2,3]]  #[ [ 1 , 3 ] , [ 2 , 1 ] , [ 3 , 2 ] ]
encoded2 =  [[6,3],[3,3]]  # [ [ 2 , 3 ] , [ 3 , 3 ] ]
s = Solution()
s.findRLEArray( encoded1 , encoded2 )



if __name__ == '__main__' :
    print( "finished!" )
