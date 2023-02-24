'''
作者：卢沛安
时间：2022年09月24日
'''
from typing import List , Tuple , Dict , Optional


def binarySearch( nums: List[ int ] , target: int ) -> int :
    left , right = 0 , len( nums ) - 1

    while left <= right :
        middle = (left + right) // 2
        if nums[ middle ] < target :
            left = middle + 1
        elif nums[ middle ] > target :
            right = middle - 1
        else :
            return middle


import bisect as bis

a = [ 1 , 4 , 12 , 13 , 15 , 15 , 20 ]
print( " ".join( str( i ) for i in nums ) )
# 插入 13， 先查找要插入的地方
position = bis.bisect_left( a , 13 )
# 当有重复值时，默认查询靠后的索引
# bisect_left 可使得返回第一个查找到的索引
print( "position should be {} , current is {}, previous is {}".format( position , a[ position ] , a[ position - 1 ] ) )
a.insert( position , 13 )
print( a )

# 或者，直接使用bisect.insort
bis.insort( a , 13 )

a = [ 10 , 3 , 5 , 61 , 23 , 5 , 7 , 4 , 8 , 9 , 10 , 3 ]
pos = bis.bisect( a , 5 )
if __name__ == '__main__' :
    print( "finished" )
