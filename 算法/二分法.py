'''
作者：卢沛安
时间：2022年09月24日
'''
from typing import List , Tuple , Dict , Optional

def binarySearch( nums: List[ int ] , target: int ) -> int :
    left , right = 0 , len(nums) - 1

    while left <= right :
        middle = (left + right) // 2

        if nums[ middle ] < target :
            left = middle + 1
        elif nums[ middle ] > target :
            right = middle - 1
        else :
            return middle


if __name__ == '__main__' :
    print("finished")
