'''
作者：卢沛安
时间：2022年09月24日
'''
from typing import List , Tuple , Dict , Optional

def sortedSquares( nums: List[ int ] ) -> List[ int ] :
    if len(nums) == 0 :
        return [ ]
    l , r = 0 , len(nums) - 1
    res = [ 0 ] * len(nums)
    k = r
    while l <= r :
        if nums[ l ] ** 2 >= nums[ r ] ** 2 :
            res[ k ] = nums[ l ] ** 2
            l += 1
        else :
            res[ k ] = nums[ r ] ** 2
            r -= 1
        k -= 1
    return res


test1 = [ -3 , 1 , 2 ]
if __name__ == '__main__' :
    ans = sortedSquares(test1)
    print(ans)
    print("finished")
