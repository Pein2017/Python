'''
作者：卢沛安
时间：2023年02月24日
'''
from typing import List , Tuple , Dict , Optional
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import numpy


def dichotomy(start, end):
    if start > end:
        print(-1)
        return
    index = (start + end) // 2
    if numpy.prod(l[:index]) > numpy.prod(l[index+1:]):
        dichotomy(start, index-1)
    elif numpy.prod(l[:index]) < numpy.prod(l[index+1:]):
        dichotomy(index+1, end)
    else:
        print(index)


while 1:
    try:
        nums = list(map(int, input().split()))
        dichotomy(0, len(nums))
    except Exception as e:
        break



if __name__ == '__main__' :
    print( "finished!" )
