'''
作者：卢沛安
时间：2022年10月17日
'''
from typing import List , Tuple , Dict , Optional


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        if not strs:
            return 0
        if len( strs ) == 1:
            return 1
        def isSimilar( st1: str , st2: str ) -> bool :
            count = 0
            if not st1 :
                return True
            for i in range( len( st1 ) ) :
                if st1[ i ] != st2[ i ] :
                    count += 1
                if count > 2 :
                    return False
            return True

        visited = [ 0 for _ in range( len( strs ) ) ]
        # visited[ 0 ] = 1

        # map[ 0 ] = 0
        groupNumber = 0

        def dfs(  target: int ) :
            if visited[ target ] == 1:
                return
            visited[ target ] = 1
            # map[ target ] = groupNumber
            for i in range( target , len( strs ) ) :
                if i != target and isSimilar( strs[ i ] , strs[ target ] ) :
                    # print( " here " , target , i)
                    dfs( i )

        for i in range( 0 , len( strs ) ):
            if visited[i] == 0:
                dfs( i )
                groupNumber += 1

        return groupNumber

    a = "abcd"
    b = "cdabcdab"

if __name__ == '__main__' :
    strs = [ "tars" , "rats" , "arts" , "star" ]
    strs = ["blw","bwl","wlb"]
    s = Solution()
    ans = s.numSimilarGroups( strs )
    print( ans )
    print( "finished!" )
