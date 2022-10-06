'''
作者：卢沛安
时间：2022年09月26日
'''
from typing import List , Tuple , Dict , Optional

# 问题描述： 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
def combine( n: int , k: int ) -> List[ List[ int ] ] :

    path , result = [ ] , [ ]

    def backtrack( n: int , k: int , start: int ) -> None :
        if len( path ) == k :
            result.append( path[ : ] )
            return
        for i in range( start , n - k + len( path ) + 2 ) :
            path.append( i )
            backtrack( n , k , i + 1 )
            path.pop()

    backtrack( n , k , 1 )
    return result


if __name__ == '__main__' :
    print( combine( 4,3) )
    print( "finished" )
