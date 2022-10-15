'''
作者：卢沛安
时间：2022年10月11日
'''
from typing import List , Tuple , Dict , Optional


def solve( st ) :
    if st[ -1 ] == 'T' :
        number = int( st[ :-1 ] )
        ans = [10 ** 6 * number,str(number)+'T']
    elif st[ -1 ] == 'G' :
        number = int( st[ :-1 ] )
        ans = [10 ** 3 * number,str(number)+'G']
    else :
        number = int( st[ :-1 ] )
        ans = [ int( st[ :-1 ] ) , str(number)+'M']
    return ans


import re

base = ("\dM" , "\dG" , "\dT")


def toM( s ) :
    total = 0
    for i , v in enumerate( base ) :
        d = re.search( v , s )
        if d :
            total += int( d.group()[ :-1 ] ) * 1000 ** i
    return total , s


while 1 :
    try :
        n = int( input() )
        my_nums = [ ]
        nums = [ ]
        for _ in range( n ) :
            # 将磁盘容量 M， G， T 全部转换为 M
            data = input()
            nums.append( toM( data ) )
            my_nums.append( solve( data ) )


        nums = sorted( nums , key=lambda x : x[ 0 ] )
        my_nums = sorted( my_nums , key = lambda x: x[0] )
        for d,my_d in zip( nums,my_nums) :
            print( d[1] , my_d[1] )
            print( d[ 1 ] )
            print( d )

    except Exception as e :
        print( e )
        break

if __name__ == '__main__' :
    print( "finished!" )
