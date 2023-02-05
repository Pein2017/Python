'''
作者：卢沛安
时间：2022年11月07日
'''
from typing import List , Tuple , Dict , Optional
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import random as rd
import numba as nb

N = 1e7
count = 0
p = 0.49
n = 400


@nb.jit( nopython=True )
def simulation( N , p=0.6 , n=100  ) :
    print( N , p ,n )
    count = 0
    thres = int( 0.55 * n)
    for _ in range( int( N ) ) :
        samples = np.random.binomial( n , p )
        if samples >= thres :
            count += 1
    return count / N


ans = simulation( N = N  , p = p , n = n)
print( "P is {}".format( ans ) )

if __name__ == '__main__' :
    print( "finished!" )
