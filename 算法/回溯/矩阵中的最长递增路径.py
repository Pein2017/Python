'''
作者：卢沛安
时间：2022年10月15日
'''
from typing import List , Tuple , Dict , Optional




class Solution :
    dirs = [ [ -1 , 0 ] , [ 1 , 0 ] , [ 0 , 1 ] , [ 0 , -1 ] ]

    def longestIncreasingPath( self , matrix: List[ List[ int ] ] ) -> int :
        if not matrix :
            return 0
        len_row = len( matrix )
        len_col = len( matrix[ 0 ] )
        memo = [ [ False ] * len_col for _ in range( len_row ) ]
        ans = 0
        for i in range( len_row ) :
            for j in range( len_col ) :
                ans = max( ans , self.backtrack( matrix , i , j , memo ) )

        return ans

    def backtrack( self , matrix , current_row , current_col , memo ) -> int :

        if memo[current_row][current_col] :
            return memo[ current_row ][ current_col ]
        len_row = len( matrix )
        len_col = len( matrix[ 0 ] )
        longest = 1
        for dir_x , dir_y in self.dirs :
            new_x , new_y = current_row + dir_x , current_col + dir_y
            if new_x >= 0 and new_x < len_row \
                    and new_y >= 0 and new_y < len_col \
                    and matrix[ current_row ][ current_col ] < matrix[ new_x ][ new_y ] :
                longest = max( longest , self.backtrack( matrix , new_x , new_y , memo ) + 1 )
        memo[current_row][current_col] = longest
        return longest


if __name__ == '__main__' :
    s = Solution()
    matrix = [ [ 9 , 9 , 4 ] , [ 6 , 6 , 8 ] , [ 2 , 1 , 1 ] ]
    ans = s.longestIncreasingPath( matrix )
    print( ans )
    print( "finished!" )
