'''
作者：卢沛安
时间：2022年10月18日
'''
from typing import List , Tuple , Dict , Optional

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len( nums )
        max_step , block_range = 0 , 0
        counter = 0
        for i in range( n -1 ):
            max_step = max( max_step , nums[i] + i )
            if i == block_range:
                block_range = max_step
                counter +=1
        return counter

if __name__ == '__main__' :
    nums = [ 2 , 3 , 0 , 1 , 4 ]
    nums = [ 2 , 3 , 1 , 1 , 4 ]
    print( Solution().jump( nums ))
    print( "finished!" )
