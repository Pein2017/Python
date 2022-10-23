'''
作者：卢沛安
时间：2022年10月16日
'''
from typing import List , Tuple , Dict , Optional


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return [ i for i in range( numCourses ) ]

        edges = dict()
        for info in prerequisites :
            if edges.get( info[ 1 ] ) :
                value = edges.get( info[ 1 ] )
                value.append( info[ 0 ] )
                edges[ info[ 1 ] ] = value
            else :
                edges[ info[ 1 ] ] = [ info[ 0 ] ]

        valid = True
        visited = [ 0 ] * numCourses
        result = [ ]

        def dfs( u: int ) :
            nonlocal valid
            visited[ u ] = 1
            if edges.get( u ):
                for list_V in edges[ u ] :
                    if isinstance( list_V , int ):
                        v = list_V
                        if visited[ v ] == 0 :
                            dfs( v )
                            if not valid :
                                return
                        elif visited[ v ] == 1 :
                            valid = False
                            return
                    else:
                        for v in list_V:
                            if visited[ v ] == 0 :
                                dfs( v )
                                if not valid :
                                    return
                            elif visited[ v ] == 1 :
                                valid = False
                                return

            visited[ u ] = 2
            result.append( u )

        for i in range( numCourses ) :
            if valid and not visited[ i ] :
                dfs( i )

        if not valid :
            return [ ]
        else :
            return result[ : :-1 ]


if __name__ == '__main__' :
    numCourses = 4
    prerequisites = [ [ 1 , 0 ] , [ 2 , 0 ] , [ 3 , 1 ] , [ 3 , 2 ] ]
    ans = findOrder( numCourses , prerequisites )
    print( ans )

    print( "finished!" )
