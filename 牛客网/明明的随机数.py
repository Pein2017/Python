'''
作者：卢沛安
时间：2022年10月10日
'''
from typing import List , Tuple , Dict , Optional


while 1 :
    try :
        N = int( input() )
        data = set()
        for i in range( N ) :
            number = int( input( ) )
            if number not in data:
                data.add( number )
        data = sorted( data )
        for num in data:
            print( num )
    except :
        break

a = 'abc'
a.rjust(4,'0')
if __name__ == '__main__' :
    print( "finished!" )
