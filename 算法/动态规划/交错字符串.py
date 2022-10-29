'''
作者：卢沛安
时间：2022年10月29日
'''
from typing import List , Tuple , Dict , Optional
import numpy as np


def isInterleave( s1: str , s2: str , s3: str ) -> bool :
    n1 , n2 , n3 = len( s1 ) , len( s2 ) , len( s3 )
    if n1 + n2 != n3 :
        return False
    dp = [ [ False for _ in range( n2 + 1 ) ] for _ in range( n1 + 1 ) ]
    dp[ 0 ][ 0 ] = True

    for i in range( 1 , n1 + 1 ) :
        dp[ i ][ 0 ] = (dp[ i - 1 ][ 0 ] and s1[ :i ] == s3[ :i ])
    for j in range( 1 , n2 + 1 ) :
        dp[ 0 ][ j ] = (dp[ 0 ][ j - 1 ] and s2[ :j ] == s3[ :j ])

    for i in range( 1 , n1 +1 ) :
        for j in range( 1 , n2 +1 ) :
            temp = False
            if dp[ i ][ j - 1 ] :
                if s2[ j - 1 ] == s3[ i + j - 1 ] :
                    temp = True
            if dp[ i - 1 ][ j ] :
                if s1[ i - 1 ] == s3[ i + j - 1 ] :
                    temp = True
            dp[ i ][ j ] = temp

    return dp[ -1 ][ -1 ]


s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"

if __name__ == '__main__' :
    print( "finished!" )
