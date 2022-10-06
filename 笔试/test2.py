'''
作者：卢沛安
时间：2022年09月26日
'''
from typing import List , Tuple , Dict , Optional


class Solution :
    def getProduct( self , path , x , golden ) :
        if golden :
            print( self.path )
            return True
        ans = 1
        for value in path :
            ans *= value
        ans = str( ans )
        if ans[ : :-1 ][ :2 ] == '00' :
            print( self.path )
            return True
        else :
            return False
        ans = "20"

    def getSubarrayNum( self , a: List[ int ] , x: int ) -> int :
        # for test
        x = 2
        a = [ 5 , 2 , 3 , 50 , 4 ]

        res = 0
        n = len( a )
        dp = [ [ 0 , 0 ] ] * n
        fives = [ ]
        twos = [ ]
        for i in range( n ) :
            if a[ i ] % 5 == 0 :
                dp[ i ] = [ 5 , a[ i ] / 5 ]
                fives.append( i )
            elif a[ i ] % 2 == 0 :
                dp[ i ] = [ 2 , a[ i ] / 2 ]
                twos.append( i )
        targets = [ ]

        for i , j in targets :
            cumProduct = 1
            cumProduct *= dp[ i ][ 1 ] * dp[ j ][ 1 ] * 10
            print( "product is {}".format( cumProduct ) )
            start_index = j
            while start_index < n - 1 and cumProduct < 10 ** x :
                start_index += 1
                cumProduct *= a[ start_index ]

            print( start_index , cumProduct )
            res += (n - start_index)

        # TODO( get Product 函数： 输入 一个数组，计算数组由第一个开始的满足结尾有x个0的乘积)
        def getProductExpand( a: List[ int ] , x: int ) -> int :
    # a = [5,2,3,50,4]

    # self.path = []
    # self.result = 0
    # self.golden = False
    #
    # def backtrack( a , start , array_length , x ) :
    #
    #     if self.golden:
    #         pass
    #     else:
    #         self.golden = self.getProduct( self.path , x ,self.golden )
    #     if self.golden:
    #         self.result += 1
    #
    #     if start == array_length:
    #         self.golden = False
    #         return
    #
    #     for i in range( start , array_length ) :
    #         self.path.append( a[ i ] )
    #         backtrack( a , i + 1 , array_length , x )
    #         self.path.pop()
    #     return
    #
    # backtrack( a , 0 , len(a) , x )
    # return self.result % ( 1e9 + 7)


if __name__ == '__main__' :
    a = [ 5 , 2 , 3 , 50 , 4 ]
    x = 2
    ans = Solution()
    p = ans.getSubarrayNum( a , x )
    print( p )
    print( "finished" )
