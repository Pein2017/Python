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
        log_list = list(map(int, input().split()))
        # 最大得分
        max_score = 0
        for i in range(len(log_list)):
            # 待上报条数
            log_num = sum(log_list[0:i+1])

            # 扣分项
            deduct = sum([log_list[j]*(i-j) for j in range(i)])
            max_score = max(max_score, log_num-deduct)
            if log_num > 100:
                break
        print(max_score)
    except Exception as e:
        break


if __name__ == '__main__' :
    print( "finished!" )
