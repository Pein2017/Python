'''
作者：卢沛安
时间：2022年10月29日
'''
from typing import List , Tuple , Dict , Optional
import numpy as np

num1 , num2 = '123' , '45'

digit = 0
num1 = '2'
num2 = '3'


def multiply( num1: str , num2: str ) -> str :
    def cal( digit , num1 , num2 ) :
        # digit: 0 is 个位数 , 1 is 百位数
        # num2 is single digit  let's say : 4
        # num1 is a full number let's say : 123
        level = 1
        num2 = int( num2 )
        ans = 0
        for i in num1[ : : -1 ] :
            ans += ( num2 * int( i) ) * level
            level *= 10
        return ( 10 ** digit * ans )

    if len( num1 ) < len( num2 ):
        num1 , num2 = num2 , num1

    n1 , n2 = len( num1 ) , len( num2 )
    ans = 0
    digit = 0
    for j in num2[::-1]:
        ans += cal( digit , num1 , j )
        digit += 1

    return str( ans )

print( multiply( num1 , num2 ))

if __name__ == '__main__' :
    print( "finished!" )
