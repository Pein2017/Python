'''
作者：卢沛安
时间：2022年10月06日
'''
from typing import List , Tuple , Dict , Optional

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

'''
假设你有 n 个版本 [1, 2, ..., n]，你想找出导致之后所有版本出错的第一个错误的版本。

你可以通过调用 bool isBadVersion(version)接口来判断版本号 version 是否在单元测试中出错。实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 API 的次数。

输入：n = 5, bad = 4
输出：4
解释：
调用 isBadVersion(3) -> false 
调用 isBadVersion(5) -> true 
调用 isBadVersion(4) -> true
所以，4 是第一个错误的版本。
'''


def isBadVersion( version: int ) -> bool :
    return 1


class Solution :
    def firstBadVersion( self , n: int ) -> int :
        left = 1
        right = n
        while left != right :
            mid = left + (right - left) // 2
            status = isBadVersion( mid )
            # print( "left {} , mid {}, right {}".format( left , mid , right))
            if status is False :  # 还没到错误的版本，继续前进
                left = mid + 1
            else :  # 到了错误版本，再回退
                right = mid
        return left


if __name__ == '__main__' :
    print( "finished" )
