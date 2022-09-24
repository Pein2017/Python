'''
作者：卢沛安
时间：2022年09月24日
'''
from typing import List , Tuple , Dict , Optional


def min_Sub_Array_Len( s: int , nums: List[ int ] ) -> int :
    if not nums:
        return 0
    l , r , n = 0 , 0 , len(nums) - 1
    temp_sum = nums[ l ]
    res = float( 'inf')
    while r <= n :
        while temp_sum < s :
            r += 1
            if r == n + 1 :
                break
            temp_sum += nums[ r ]
        while temp_sum >= s :
            temp_sum -= nums[ l ]
            res = min( res , r - l + 1 )
            l += 1
    return 0 if res == float('inf') else res
'''
优化
只引入一个while 循环，通过判断sum是否大于target而修改窗口，不然无脑扩充
'''
def min_Sub_Array_Len( s: int , nums: List[ int ] ) -> int :
    if not nums:
        return 0
    l , r , n = 0 , 0 , len(nums) - 1
    temp_sum = 0
    res = float( 'inf')
    while r <=n:
        temp_sum += nums[r]
        while temp_sum >= s:
            res = min( res , r-l+1 )
            temp_sum -= nums[l]
            l+=1
        r +=1

    return 0 if res == float('inf') else res



s = 15
nums = [5,1,3,5,10,7,4,9,2,8]
if __name__ == '__main__' :
    ans = min_Sub_Array_Len(s , nums)
    print( ans )
    print("finished")
