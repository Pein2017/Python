'''
作者：卢沛安
时间：2022年09月26日
'''
from typing import List , Tuple , Dict , Optional


'''
只有 1,0 的字符，每次操作选择相邻的两个同时替换成0或者1,
最少多少次操作，全部字符相同
'''


class Solution :

    def minOperations( self , str: str ) -> int :
        def count( str ) :
            zero_count = 0
            for value in str :
                if value == "0" :
                    zero_count += 1
            return zero_count

        n = len( str )
        str = list(str)
        zero_count = count( str )
        one_count = n - zero_count
        if zero_count > one_count :
            # 0多，将所有1换位0
            target = '1'
            replace_to = '0'
        else :
            # 1多，将所有1换位0
            target = '0'
            replace_to = '1'
        res = 0
        for i in range( n ) :
            value = str[i]
            if value == target:
                str[i] = replace_to
                res += 1
                if i < n-1:
                    str[i+1] = replace_to

        return res






s = "1001101"
ans = Solution()
print( ans.minOperations( s ))


def count( str ) :
    zero_count = 0
    for value in str :
        if value == "0" :
            zero_count += 1
    return zero_count

def minOP( str ):
    n = len( str )
    str = list( str )
    zero_count = count( str )
    one_count = n - zero_count
    if zero_count > one_count :
        # 0多，将所有1换位0
        target = '1'
        replace_to = '0'
    else :
        # 1多，将所有1换位0
        target = '0'
        replace_to = '1'
    res = 0
    for i in range( n ) :
        value = str[ i ]
        res += 1
        if value == target :
            str[ i ] = replace_to
            if i < n - 1 :
                str[ i + 1 ] = replace_to
            print(str)

    return res

if __name__ == '__main__' :
    print( "finished" )
