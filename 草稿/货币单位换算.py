'''
作者：卢沛安
时间：2023年02月23日
'''
from typing import List , Tuple , Dict , Optional
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

mapping = {"fen": 1,
           "CNY": 100,
           "sen": 100/1825,
           "JPY": 10000/1825,
           "cents": 100/123,
           "HKD": 10000/123,
           "eurocents": 100/14,
           "EUR": 10000/14,
           "pence": 100/12,
           "GBP": 10000/12}


def toFen(data):
    _total = 0
    val = ""
    unit = ""
    for c in data:
        if "0" <= c <= "9":
            if unit: # 元与分组合
                _total += mapping[unit] * int(val)
                val = ""
                unit = ""
            val += c
        else:
            unit += c
    else:
        _total += mapping[unit] * int(val)
    return _total


while 1:
    try:
        n = int(input())

        total = 0
        for _ in range(n):
            total += toFen(input())
        print(str(total).split('.')[0])
    except Exception as e:
        break


if __name__ == '__main__' :
    print( "finished!" )
