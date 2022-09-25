'''
作者：卢沛安
时间：2022年09月25日
'''
from typing import List , Tuple , Dict , Optional
#  子序列 ， 不用连续
#  子串，    要连续




def lengthOfLIS( nums: List[ int ] ) -> int :
    if not nums :
        return 0
    dp = [ 1 ] * len( nums )
    for i in range( 1 , len( nums ) ) :
        temp_res = 1
        for j in range( 0 , i ) :
            if nums[ i ] > nums[ j ] :
                temp_res = max( temp_res , dp[ j ] + 1 )
            dp[ i ] = temp_res
    return max( dp )

if __name__ == '__main__' :
    nums = [ 10 , 9 , 2 , 5 , 3 , 7 , 101 , 18 ]
    ans = lengthOfLIS( nums )
    print( ans )

    nums = [ 0 , 1 , 0 , 3 , 2 , 3 ]
    ans = lengthOfLIS( nums )
    print( ans )
    print( "finished" )
