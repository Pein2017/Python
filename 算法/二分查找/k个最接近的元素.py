'''
作者：卢沛安
时间：2022年10月06日
'''
from typing import List , Tuple , Dict , Optional

'''
给定一个 排序好 的数组arr ，两个整数 k 和 x ，从数组中找到最靠近 x（两数之差最小）的 k 个数。返回的结果必须要是按升序排好的。

整数 a 比整数 b 更接近 x 需要满足：

|a - x| < |b - x| 或者
|a - x| == |b - x| 且 a < b

'''

import bisect as bis
class Solution :
    '''
    def findClosestElements( self , arr: List[ int ] , k: int , x: int ) -> List[ int ] :
        arr.sort( key=lambda v : abs( v - x ) )
        return sorted( arr[ :k ] )
    '''
    def findClosestElements( self , arr: List[ int ] , k: int , x: int ) -> List[ int ] :
        right = bis.bisect_left( arr , x )
        left = right - 1
        ans = [ ]
        counter = 0
        while counter < k and left >= 0 and right < len( arr ) :
            if abs( arr[ left ] - x ) <= abs( arr[ right ] - x ) :
                ans.insert( 0 , arr[ left ] )
                left -= 1
                counter += 1
            else :
                ans.append( arr[ right ] )
                right += 1
                counter += 1
            # print( ans )
        if counter == k :
            return ans
        else :
            if left == -1 :
                for _ in range( k - counter  ) :
                    ans.append( arr[ right ] )
                    right += 1
            elif right == len( arr ) :
                for _ in range( k - counter  ) :
                    ans.insert( 0 , arr[ left ] )
                    left -= 1
        return ans

if __name__ == '__main__' :
    arr = [-2,-1,1,2,3,4,5]
    k = 7
    x = 3
    sol = Solution()
    print( sol.findClosestElements( arr , k , x ) )

    print( "finished" )
