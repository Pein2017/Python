'''
作者：卢沛安
时间：2022年11月03日
'''
from typing import List , Tuple , Dict , Optional
import numpy as np


def numDecodings( s: str ) -> int :
    if len( s ) == 0 :
        return 0
    if len( s ) == 1 :
        return 1 if s[ 0 ] != '0' else 0
    # dp = [ 0 ] * (len( s ) + 1)
    # dp[ 0 ] = 1
    dp = [ 1 ] + [ 0 ] * len( s )
    for i in range( 1 , len( s ) + 1 ) :
        # 自己组成一个解码
        if s[ i - 1 ] != '0' :
            dp[ i ] += dp[ i - 1 ]
        # 和前面一个 s[i-1] 组成一个解码
        if i >= 2 :
            if 9 < int( s[i-2:i]) < 27:
                dp[ i ] += dp[ i - 2 ]
    return dp[ -1 ]


s = "10"

if __name__ == '__main__' :
    print( numDecodings( s ) )
    print( "finished!" )
