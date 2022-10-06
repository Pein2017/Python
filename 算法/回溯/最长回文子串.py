'''
作者：卢沛安
时间：2022年09月26日
'''
from typing import List , Tuple , Dict , Optional


def expandCenter( s: str , left: int , right: int ) :
    while left >= 0 and right < len( s ) and s[ left ] == s[ right ] :
        left -= 1
        right += 1
    return left + 1 , right - 1


def longestPalindrome( s: str ) -> str :
    start , end = 0 , 0
    for i in range( len( s ) ) :
        left1 , right1 = expandCenter( s , i , i )  # 以 s[i]为中心的
        left2 , right2 = expandCenter( s , i , i + 1 )  # 以s[i]和s[i+1]为中心的
        if right1 - left1 > right2 - left2 :
            start , end = left1 , right2
        else :
            start , end = left2 , right2
    return s[ start : end + 1 ]


if __name__ == '__main__' :
    print( "finished" )
