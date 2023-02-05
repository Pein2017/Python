'''
作者：卢沛安
时间：2022年12月10日
'''
from typing import List , Tuple , Dict , Optional
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

nums1 = [1,2,3,1]
nums2 = [1,2,3,4]
nums3 = [1,1,1,3,3,4,3,2,4,2]
def solve( array ):
    curr = set()
    for element in array:
        if element in curr:
            return True
        else:
            curr.add( element )
    return False

print( solve( nums1) )

print( solve( nums2) )

print( solve( nums3) )







if __name__ == '__main__' :
    print( "finished!" )
