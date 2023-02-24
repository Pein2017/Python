'''
作者：卢沛安
时间：2023年02月23日
'''
from typing import List , Tuple , Dict , Optional
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd


def get_permutations( data=None ) :
    if not data :
        return [ "" , "0" , "1" ]

    tmp = [ ]
    for c in data :
        tmp.append( c + "0" )
        tmp.append( c + "1" )
    tmp.extend( data )
    return tmp


while 1 :
    try :
        _mini , _maxi = map( int , input().split() )
        _minb = bin( _mini )[ 2 : ]
        _maxb = bin( _maxi )[ 2 : ]
        sign = "101"
        # 最大值小于5的情况
        if len( _maxb ) < len( sign ) :
            print( _maxi - _mini )
            break
        permutations = [ ]
        # 101可移动的次数
        for i in range( len( _maxb ) - len( sign ) ) :
            permutations = set( get_permutations( permutations ) )


        def _zfill( x ) :
            return (sign + x).zfill( len( _maxb ) )


        # 上面产生的组合 字符串长度是不一致的
        # 如 101  1011 需要对字符串长度补齐，前面补0
        set101 = map( _zfill , permutations )
        set101 = sorted( set101 )
        i = 0
        while int( set101[ i ] , 2 ) < _mini :
            set101.pop( 0 )
        j = len( set101 ) - 1
        while int( set101[ j ] , 2 ) > _maxi :
            set101.pop( j )
            j -= 1

        print( _maxi - _mini - len( set101 ) )
    except Exception as e :
        break

if __name__ == '__main__' :
    print( "finished!" )
