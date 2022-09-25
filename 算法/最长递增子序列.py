'''
作者：卢沛安
时间：2022年09月25日
'''
from typing import List , Tuple , Dict , Optional
#  子序列 ， 不用连续
#  子串，    要连续

#最快
def lengthOfLIS( nums: List[ int ] ) -> int :
    import bisect as bis
    if not nums :
        return 0
    # dp 为包括自己在内，从左开始到自己的最长自增子序列
    dp = [1]
    # t 为需要维护的数组： 每次都更新数组，使得这个t数组非正无穷的数字严格递增，且递增得最慢!
    # t1 = [ 2 5 7]
    # t2 = [ 2 5 6]
    # 则将 t1 替换成 t2， t[pos] = nums[check] （6）

    t = [ float('inf') for _ in range(n) ]
    t[0]=nums[0]
    n = len( nums )
    for i in range( 1 , n ):
        pos = bis.bisect_left( t , nums[i] )
        print( t , pos )
        t[pos] = nums[i] # 在t中，找到合适位置插入nums[i]维持秩序
        # 如果 pos ==0 ， 则没有数字比当前的nums[i]小,
        dp += [pos+1]
    return max(dp)

#动态规划
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



nums = [ 186 , 186 , 150 ,200 , 160 , 130 , 197, 200]


if __name__ == '__main__' :
    nums = [ 10 , 9 , 2 , 5 , 3 , 7 , 101 , 18 ]
    ans = lengthOfLIS( nums )
    print( ans )

    nums = [ 0 , 1 , 0 , 3 , 2 , 3 ]
    ans = lengthOfLIS( nums )
    print( ans )
    print( "finished" )
