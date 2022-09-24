'''
作者：卢沛安
时间：2022年09月24日
'''
from typing import List , Tuple , Dict , Optional

def removeElement( nums: List[ int ] , val: int ) -> int :

    if num is None or len(nums) == 0 :
        return 0
    left , right = 0 , len(nums) - 1
    while left < right :
        while left < right and nums[ left ] != val :
            left += 1
        while left < right and nums[ right ] == val :
            right -= 1
        nums[ left ] , nums[ right ] = nums[ right ] , nums[ left ]
        print(nums)

        if nums[ left ] == val :
            return left
        else :
            return left + 1


if __name__ == '__main__' :
    print("finished")
