'''
作者：卢沛安
时间：2023年02月24日
'''
from typing import List , Tuple , Dict , Optional
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

while 1 :
    try :
        s = input()


        def is_perfect( data , blens=0 ) :
            ac = data.count( "A" )
            dc = data.count( "D" )
            sc = data.count( "S" )
            wc = data.count( "W" )
            return abs( ac - dc ) + abs( sc - wc ) == blens


        def get_lens() :
            for i in range( max( abs( s.count( "A" ) - s.count( "D" ) ) ,
                                 abs( s.count( "S" ) - s.count( "W" ) ) ) // 2 ,
                            len( s ) ) :
                for j in range( i , len( s ) ) :
                    if is_perfect( s[ :j - i ] + s[ j : ] , i ) :
                        return i


        if is_perfect( s ) :
            print( 0 )
        else :
            print( get_lens() )
    except Exception as e :
        break

if __name__ == '__main__' :
    print( "finished!" )
