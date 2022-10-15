'''
作者：卢沛安
时间：2022年10月12日
'''
from typing import List , Tuple , Dict , Optional

'''
输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36
'''

n = 10


class Solution :
    def cuttingRope( self , n: int ) -> int :
        dp = [ 0 , 0 , 1 ]
        # if n == 2:
        #     return 1
        for i in range( 3 , n + 1 ) :
            ans = -1
            for j in range( 1 , i ) :
                ans = max( ans , max( j * (i - j) , dp[ j ] * (i - j) ) )
                # print( i , j , ans )
            dp.append( ans )
        return dp[ -1 ]


if __name__ == '__main__' :
    print( "finished!" )
