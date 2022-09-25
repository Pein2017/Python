'''
作者：卢沛安
时间：2022年09月25日
'''
from typing import List , Tuple , Dict , Optional
import collections

def getMinCount( str: str ) -> int :
    n = len( str )
    dic = collections.Counter( str )
    ans = 0
    # 记录去除原始字符串中的重复元素的操作次数
    for value in dic.values() :
        ans += value // 2
    # 剩下的字符串如果超过26个字母，则每多一个就需要一次操作
    ans += max( 0 , n - ans - 26 )
    return ans

str = 'ababc'
ans = getMinCount( s )
print( ans )


if __name__ == '__main__' :
    print( "finished" )
