'''
作者：卢沛安
时间：2023年02月21日
'''
from typing import List , Tuple , Dict , Optional
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd


class Solution :
    def trap( self , height: List[ int ] ) -> int :
        if not height :
            return 0
        n = len( height )
        res = 0
        left , right = 0 , n - 1
        left_max , right_max = -1 , -1
        while left < right:
            if height[ left ] < height[ right ] :
                # from left to right
                if height[ left ] >= left_max :
                    left_max = height[ left ]
                else :
                    res += left_max - height[ left ]
                left += 1
            else :
                if height[ right ] >= right_max :
                    right_max = height[ right ]
                else :
                    res += right_max - height[ right ]
                right -= 1
        return res


S = Solution()

height = [ 0 , 1 , 0 , 2 , 1 , 0 , 1 , 3 , 2 , 1 , 2 , 1 ]
S.trap( height )
height =[2,0,2]
S.trap( height )
if __name__ == '__main__' :
    print( "finished!" )
