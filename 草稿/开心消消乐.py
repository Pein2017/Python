'''
作者：卢沛安
时间：2023年02月23日
'''
from typing import List , Tuple , Dict , Optional
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd


def dfs( ni , mj ) :
    # 点击点是0，或者已经查看过，不是有效的集合
    if (ni , mj) in cache \
            or mapping[ ni ][ mj ] == "0" :
        return False

    # 如果这个点是1，查看所有相邻的点，如果是1继续向下查
    def do_dfs( x , y ) :
        if (x , y) in cache \
                or x < 0 or x >= n \
                or y < 0 or y >= m :
            return

        cache.append( (x , y) )
        if mapping[ x ][ y ] == "1" :
            do_dfs( x , y + 1 )
            do_dfs( x , y - 1 )
            do_dfs( x - 1 , y )
            do_dfs( x + 1 , y )
            do_dfs( x - 1 , y - 1 )
            do_dfs( x - 1 , y + 1 )
            do_dfs( x + 1 , y - 1 )
            do_dfs( x + 1 , y + 1 )

    do_dfs( ni , mj )
    # 已经找到了一个全是1的集合，返回计数
    return True


while 1 :
    try :
        n , m = map( int , input().split() )
        mapping = [ input().split() for i in range( n ) ]
        cache = [ ]
        count = 0
        for i in range( n ) :
            for j in range( m ) :
                count += dfs( i , j )
        print( count )
    except Exception as e :
        break

if __name__ == '__main__' :
    print( "finished!" )
