'''
作者：卢沛安
时间：2022年10月10日
'''
from typing import List , Tuple , Dict , Optional

while 1 :
    try :
        data = input()
        if data :
            while 1 :
                if len( data ) > 8 :
                    print( data[ 0 :8 ] )
                else :
                    print( data.ljust( 8 , '0' ) )
                    break
                data = data[ 8 : ]
        else :
            pass

    except :
        break

if __name__ == '__main__' :
    print( "finished!" )
