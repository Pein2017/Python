'''
作者：卢沛安
时间：2022年10月11日
'''
from typing import List , Tuple , Dict , Optional

import bisect as bis

while 1:
    try:
        n = int(input())

        nums = [list(map(int, input().split())) for _ in range(n)]

        dp = []
        lens = len(nums)

        def dfs(sub, count=1):
            if count >= lens:
                dp.append(len(sub))
            else:
                for i in range(lens):
                    if i not in sub:
                        if nums[i][0] < nums[sub[-1]][0] and nums[i][1] < nums[sub[-1]][1]:
                            dfs(sub+[i], count+1)

        for i in range(lens):
            dfs([i])
        true = max(dp)
        #print( "true is {}".format(true))

        long_sorted_data = sorted( nums , key=lambda x : x[ 0 ] )
        dp = [ 1 ]
        t = [ float( 'inf' ) ] * len( nums )
        t[ 0 ] = long_sorted_data[ 0 ][ 1 ]
        for _ , value in long_sorted_data :
            pos = bis.bisect_left( t , value )
            t[ pos ] = value
            dp.append( pos + 1 )
        my_res = max( dp )
        assert true == my_res

    except Exception as e:
        break


if __name__ == '__main__' :
    print( "finished!" )
    # my part

