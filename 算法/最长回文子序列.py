'''
作者：卢沛安
时间：2022年09月26日
'''
from typing import List , Tuple , Dict , Optional


# 子序列： 不用连续
'''
 dp[i][j]：  下标范围[i,j]内的最长回文子序列的长度！
 
    1. dp[i][i] = 1
    2. for i in range(n):
        for j in range(i+1 , n):
        if s[i] == s[j]:
            先找到 dp[i-1][j-1] 即 [i+1,j-1]范围内的最长回稳子序列，然后再在其首尾添加s[i],s[j]。
            dp[i][j] = dp[i+1][j-1] + 2
        else:
            即s[i][j]不能同时作为回文子序列的头尾，寻找最大的
            dp[i][j] = max( dp[i][j-1] , dp[i+1][j] )
'''
class Solution :
    def longestPalindromeSubseq( self , s: str ) -> int :
        n = len( s )
        dp = [ [ 0 ] * n for _ in range( n ) ]
        for i in range( n - 1 , -1 , -1 ) :
            dp[ i ][ i ] = 1
            for j in range( i + 1 , n ) :
                if s[ i ] == s[ j ] :
                    dp[ i ][ j ] = dp[ i + 1 ][ j - 1 ] + 2
                else :
                    dp[ i ][ j ] = max( dp[ i + 1 ][ j ] , dp[ i ][ j - 1 ] )
        return dp[ 0 ][ n - 1 ]


if __name__ == '__main__' :
    print( "finished" )
