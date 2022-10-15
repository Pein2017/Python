'''
作者：卢沛安
时间：2022年10月14日
'''
from typing import List , Tuple , Dict , Optional


class NestedInteger :
    def __init__( self , value=None ) :
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """

    def isInteger( self ) :
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """


nestedList = [ [ 1 , 1 ] , 2 , [ 1 , 1 ] ]
nestedList = [1,[4,[6]]]

def depthSum( nestedList: List[ int ] ) -> int :
    def backtrack( array: List[ int ] , depth: int ) -> int :
        ans = 0
        if isinstance( array , int ) :
            print( "int , depth is", array , depth )
            return array * depth
        for nested_elements in array :
            temp = backtrack( nested_elements , depth + 1 )
            ans += temp
        return ans
    ans = backtrack( nestedList , 0 )
    return ans

res = depthSum( nestedList )
print( res )

if __name__ == '__main__' :
    print( "finished!" )
