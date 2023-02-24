'''
作者：卢沛安
时间：2023年02月24日
'''
from typing import List , Tuple , Dict , Optional
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

'''
m , n = 4 , 5
array = 
[['X', 'X', 'X', 'X', 'X'],
 ['O', 'O', 'O', 'O', 'X'],
 ['X', 'O', 'O', 'O', 'X'],
 ['X', 'O', 'X', 'X', 'O']]
'''

'''
m , n = 5 , 5
array = 
[['X', 'X', 'X', 'X', 'X'],
 ['X', 'X', 'O', 'O', 'O'],
 ['X', 'X', 'X', 'X', 'X'],
 ['X', 'X', 'O', 'O', 'O'],
 ['X', 'X', 'X', 'X', 'X']]
'''

while 1 :
    try :
        m , n = map( int , input().split() )

        array = [ input().split() for i in range( m ) ]

        # 字典的 key是入口坐标，value是空闲区域大小
        start_dict = {}
        del_xy = set()

        for i in range( m ) :
            if array[ i ][ 0 ] == "O" :
                start_dict.update( {(i , 0) : [ ]} )
            if array[ i ][ n - 1 ] == "O" :
                start_dict.update( {(i , n - 1) : [ ]} )

        for j in range( n ) :
            if array[ 0 ][ j ] == "O" :
                start_dict.update( {(0 , j) : [ ]} )
            if array[ m - 1 ][ j ] == "O" :
                start_dict.update( {(m - 1 , j) : [ ]} )


        def do_dfs( x , y , stack ) :
            if not (0 <= x < m) \
                    or not (0 <= y < n) \
                    or array[ x ][ y ] == "X" \
                    or (x , y) in stack :
                if (x , y) in stack :
                    print( f'({x},{y}) has checked' )
                return
            if (x , y) in start_dict :
                del_xy.add( (x , y) )
                print( 'del_xy added' , (x , y) )
                return
            print( '------' )
            print( 'checking' , x , y , stack )
            stack.append( (x , y) )
            print( 'finished dfs, the stack is: ' , stack )
            print( '---' )
            do_dfs( x + 1 , y , stack )
            do_dfs( x - 1 , y , stack )
            do_dfs( x , y + 1 , stack )
            do_dfs( x , y - 1 , stack )


        def dfs( x , y ) :
            start_dict[ (x , y) ].append( (x , y) )
            do_dfs( x + 1 , y , start_dict[ (x , y) ] )
            do_dfs( x - 1 , y , start_dict[ (x , y) ] )
            do_dfs( x , y + 1 , start_dict[ (x , y) ] )
            do_dfs( x , y - 1 , start_dict[ (x , y) ] )


        for key in start_dict.keys() :
            dfs( *key )

        # 移除无效的入口
        for key in del_xy :
            start_dict.pop( key )

        if not start_dict :
            print( "NULL" )
        else :
            ret = {}
            for key , value in start_dict.items() :
                lens = len( value )
                if lens not in ret :
                    ret.update( {lens : [ ]} )
                ret[ lens ].append( key )

            _max = max( ret )
            if len( ret[ _max ] ) == 1 :
                print( ret[ _max ][ 0 ][ 0 ] , ret[ _max ][ 0 ][ 1 ] , _max )
            else :
                print( _max )
    except Exception as e :
        break

if __name__ == '__main__' :
    print( "finished!" )
