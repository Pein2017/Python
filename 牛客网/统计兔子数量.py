'''
作者：卢沛安
时间：2022年09月24日
'''
from typing import List , Tuple , Dict , Optional

def RabitNumber( n:int ) -> int:
    n1 = 1  # 一个月的兔子
    n2 = 0  # 两个月的兔子
    n3 = 0  # 三个月以及以上的兔子
    for i in range(1,n):
        n3 +=n2
        n2 = n1
        n1 = n3
    res = n1 + n2 + n3
    return res
# while 1:
#     try:
#         n = int( input() )
#         print( RabitNumber(n) )
#     except:
#         break


if __name__ == '__main__' :
    for i in range(1,8):
        print( RabitNumber( i ) )
    print("finished")
