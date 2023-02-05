'''
作者：卢沛安
时间：2022年12月03日
'''
from typing import List , Tuple , Dict , Optional
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd


def parking_cars( K ) :
    def check( path,K ):
        for i in range( K ):
            if path[i] == i:
                return False
        return True
    def get_rest( path , K ):
        res = []
        for i in range(K):
            if i not in path:
                res.append(i)
        return res
    cars = [ ]
    path = [ ]
    def backtrack(  ):
        nonlocal path
        nonlocal cars
        if len( path ) == K :
            if check( path , K ) :
                # print( 'yes' )
                cars.append( path[ : ] )
            return
        rest = get_rest( path , K )
        for item in rest:
            if item == len( path ):

                continue
            path.append( item )
            backtrack( )
            path.pop( )
        return
    backtrack( )
    prod = 1
    for j in range( 2 , K+1 ):
        prod*=j
    return cars , len( cars ) / prod



for K in range( 2 , 9):
    ans = parking_cars(K)
    print( K , ans[1] )


if __name__ == '__main__' :
    print( "finished!" )
