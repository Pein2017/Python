'''
作者：卢沛安
时间：2022年10月09日
'''
from typing import List , Tuple , Dict , Optional




while 1 :
    try :
        n = int( input() )
        flag = int( input() )  # 0 是高到低
        data = [ ]
        for _ in range( n ) :
            data.append( input( ).split() )
        if flag == 0:
            res = sorted( data , key = lambda x: int(x[1]) , reverse=True)
        else:
            res = sorted( data , key=lambda x : int(x[1]) , reverse=False )
        for j in res:
            print(" ".join(j))
    except :
        break

if __name__ == '__main__' :
    print( "finished!" )
