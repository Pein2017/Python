'''
作者：卢沛安
时间：2022年11月12日
'''
from typing import List , Tuple , Dict , Optional
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd


A = [1,2,3,4,5,6,7,8]
p = []
for a in A:
    for b in A:
        if a != b:
            p += [ a+b ]
p = np.array( p )
sum(  p <= 7 )


res = get( 100 )
print( res )
if __name__ == '__main__' :
    print( "finished!" )
