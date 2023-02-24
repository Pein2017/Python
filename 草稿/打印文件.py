'''
作者：卢沛安
时间：2023年02月24日
'''
from typing import List , Tuple , Dict , Optional
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

while 1 :
    try :
        n = int( input() )
        # 声明5个打印队列
        stack_list = [ [ ] for i in range( 5 ) ]
        count = 1
        ret = [ ]
        for i in range( n ) :
            line = input().split()
            if "IN" in line :
                opt , p , post = line
                stack_list[ int( p ) ].append( (int( post ) , count) )
                count += 1
            else :
                opt , p = line
                if stack_list[ int( p ) ] :
                    # 对队列进行排序
                    stack_list[ int( p ) ] = sorted( stack_list[ int( p ) ] , key=lambda x : (x[ 0 ] , -x[ 1 ]) )
                    ret.append( stack_list[ int( p ) ].pop()[ 1 ] )
                else :
                    ret.append( "NULL" )
        for out in ret :
            print( out )
    except Exception as e :
        break

if __name__ == '__main__' :
    print( "finished!" )
