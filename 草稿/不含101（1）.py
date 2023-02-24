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
        return [ "0" , "1" ]

    tmp = [ ]
    for c in data :
        tmp.append( c + "0" )
        tmp.append( c + "1" )
    return tmp


while 1 :
    try :
        _mini , _maxi = map( int , input().split() )
        _minb = bin( _mini )[ 2 : ]
        _maxb = bin( _maxi )[ 2 : ]
        lens = max( len( _minb ) , len( _maxb ) )

        sign = "101"
        # 最大值小于5的情况
        if lens < len( sign ) :
            print( _maxi - _mini )
            break

        set101 = set()
        permutations = None
        # 101可移动的次数
        for i in range( lens - len( sign ) ) :
            permutations = get_permutations( permutations )
            for c in permutations :
                if int( sign + c , 2 ) > _maxi :
                    break
                set101.add( sign + c )

        print( _maxi - _mini - len( set101 ) )
    except Exception as e :
        break

if __name__ == '__main__' :
    print( "finished!" )
