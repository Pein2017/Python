'''
作者：卢沛安
时间：2023年02月23日
'''
from typing import List , Tuple , Dict , Optional
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

while 1:
    try:
        s1 = input()
        s2 = input()
        width = len(s1) + int(input())

        mapping = {}
        for c in s1:
            if c not in mapping:
                mapping[c] = 0
            mapping[c] += 1

        for i in range(len(s2)):
            # 剩余子串长度不满足
            if len(s2[i:]) < width:
                print(-1)
                break
            for k, v in mapping.items():
                # 当前子串有不满足的字符，直接跳出进入下一个子串的判断
                if s2[i:i+width].count(k) < v:
                    break
            else:
                # 所有字符都满足要求，没有跳出的情况，输出最左侧下标
                print(i)
                break
    except Exception as e:
        break


if __name__ == '__main__' :
    print( "finished!" )
