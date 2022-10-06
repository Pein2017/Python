'''
作者：卢沛安
时间：2022年10月04日
'''
from typing import List , Tuple , Dict , Optional


class Solution :
    def corpFlightBookings( self , bookings: List[ List[ int ] ] , n: int ) -> List[ int ] :
        if not bookings:
            return []
        ans = [ 0 ] * n
        for book in bookings:
            index1 = book[0]
            ans[ index1 -1 ] += book[2]
            index2 = book[1]
            if index2 < n:
                ans[index2] -= book[2]


        for i in range(1,n):
            ans[i] += ans[i-1]

        return  ans


if __name__ == '__main__' :
    bookings = [[1,2,10],[2,2,15]]
    n = 2
    sol = Solution()
    print( sol.corpFlightBookings( bookings , n ) )
    print( "finished" )
