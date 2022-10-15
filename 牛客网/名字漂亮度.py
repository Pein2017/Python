'''
作者：卢沛安
时间：2022年10月09日
'''
from typing import List , Tuple , Dict , Optional

word = 'lisi'


class Solution() :
    def solve( self , word: str ) -> int :
        letters = set( word )
        freq = dict()
        for j in letters :
            freq[ j ] = word.count( j )
        sorted_freq = sorted( freq.items() , key=lambda x : x[ 1 ] , reverse=True )
        res = 0
        weights = 26
        for letter , count in sorted_freq :
            res += weights * count
            weights -= 1
        print( res )

sol = Solution()
while 1 :
    try :
        n = int( input() )
        data = [ ]
        for _ in range( n ) :
            word = input()
            sol.solve( word )
    except :
        break

if __name__ == '__main__' :
    print( "finished!" )
