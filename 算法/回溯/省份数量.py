'''
作者：卢沛安
时间：2022年10月15日
'''
from typing import List , Tuple , Dict , Optional


class Solution :
    def findCircleNum( self , isConnected: List[ List[ int ] ] ) -> int :
        def backtrack( i ):
            for j in range( n ):
                if isConnected[i][j] == 1 and j not in visited:
                    visited.add( j )
                    backtrack( j )

        n = len( isConnected )
        visited = set()
        provinces = 0
        for i in range( n ):
            if i not in visited:
                backtrack( i )
                provinces += 1
                # 从 城市 i 出发的所有相邻的城市都会被添入 visited()。 所以 ' i not in visited' 代表着 这个城市不是之前城市所连接的，进而provinces += 1

        return provinces

if __name__ == '__main__' :
    isConnected = [ [ 1 , 1 , 0 ] , [ 1 , 1 , 0 ] , [ 0 , 0 , 1 ] ]
    s = Solution()
    ans = s.findCircleNum( isConnected )
    print( ans )
    print( "finished!" )
