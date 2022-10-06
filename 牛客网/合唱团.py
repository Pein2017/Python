'''
作者：卢沛安
时间：2022年09月26日
'''
from typing import List , Tuple , Dict , Optional
import bisect as bis


class Solution :
    def minNumber( self , array: List[ int ] , n: int ) -> int :
        def increase( nums: List[ int ] ) -> List[ int ] :
            # TODO( 构造递增子序列函数，为了计算该数左边的最长递增子序列 )
            n = len( nums )
            if n == 1 :
                return 1
            dp = [ 1 ]
            queue = [ float( 'inf' ) ] * n
            queue[ 0 ] = nums[ 0 ]
            for i in range( 1 , n ) :
                pos = bis.bisect_left( queue , nums[ i ] )
                queue[ pos ] = nums[ i ]
                dp.append( pos + 1 )
            return dp

        leftMax = increase( array )
        rightMax = increase( array[ : :-1 ] )[ : :-1 ]
        L = 0
        for i in range( n ) :
            L = max( L , leftMax[ i ] + rightMax[ i ] )
        L -= 1
        return n - L


S = Solution()
while 1 :
    try :
        n = int( input() )
        nums = list( map( int , input().split() ) )
        res = S.minNumber( nums , n )
        print( str( res ) )
    except :
        break

#
# if __name__ == '__main__' :
#     # nums = [ 10 , 9 , 2 , 5 , 3 , 7 , 101 , 18 ]
#     # ans = increase( nums )
#     nums = [8,20,12,15,10,9]
#     nums = [186 ,186 ,150 ,200 ,160 ,130, 197 ,200]
#     S = Solution()
#     print( S.minNumber( nums , len(nums )) )
#     print( "finished" )
