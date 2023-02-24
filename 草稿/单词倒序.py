'''
作者：卢沛安
时间：2023年02月24日
'''
from typing import List , Tuple , Dict , Optional
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd


while 1:
    try:
        lines = input()
        ret = []
        w = ""
        for c in lines:
            if c in " ,.?":
                ret.append(w[::-1])
                w = ""
                ret.append(c)
            else:
                w += c
        print("".join(ret))
    except Exception as e:
        break


if __name__ == '__main__' :
    print( "finished!" )
