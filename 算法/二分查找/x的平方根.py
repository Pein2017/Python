'''
作者：卢沛安
时间：2022年10月05日
'''
from typing import List , Tuple , Dict , Optional


class Solution :
    def mySqrt( self , x: int ) -> int :
        if x < 1 :
            return 0
        if x == 2 or x == 3 :
            return 1
        left , right = 1 , x // 2 + 1
        while left <= right :
            mid = int( left + (right - left) / 2 )
            print( "{},{},{}".format( left , mid , right ) )
            if mid * mid <= x :
                ans = mid
                left = mid + 1
            else :
                right = mid - 1

        return ans


if __name__ == '__main__' :
    s = Solution()
    x = 8
    print( s.mySqrt( x ) )
    print( "finished" )
