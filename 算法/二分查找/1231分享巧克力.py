'''
作者：卢沛安
时间：2023年02月16日
'''
from typing import List , Tuple , Dict , Optional
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

sweetness = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 ]
k = 5

sweetness = [ 1 , 2 , 2 , 1 , 2 , 2 , 1 , 2 , 2 ]
k = 2

sweetness = [ 52832 , 63820 , 96186 , 1623 , 88717 ]
k = 3


class Solution :
    def maximizeSweetness( self , sweetness: List[ int ] , k: int ) -> int :
        def getPieces( min_sweet ) :
            count , sweet_sum = 0 , 0
            for sweet in sweetness :
                sweet_sum += sweet
                if sweet_sum >= min_sweet :
                    count += 1
                    sweet_sum = 0
            return count

        K = k + 1
        left , right = min( sweetness ) , sum( sweetness ) // K + 1
        while 1 :
            mid = left + (right - left) // 2
            if left == mid :
                if getPieces( right ) == K :
                    left = right
                break
            count = getPieces( mid )
            if count < K :
                right = mid - 1
            else :
                left = mid
            print( left , right , count )

        return left


if __name__ == '__main__' :
    print( "finished!" )
