'''
作者：卢沛安
时间：2022年10月18日
'''
from typing import List , Tuple , Dict , Optional
import bisect as bis


def findRadius( houses: List[ int ] , heaters: List[ int ] ) -> int :
    res = 0
    heaters.sort()
    houses.sort()
    heaters.insert( 0 , float( '-inf' ) )
    heaters.append( float( "inf" ) )
    for house in houses :
        pos = bis.bisect_left( heaters , house )
        temp_radius = min( heaters[ pos ] - house , abs( heaters[ pos - 1 ] - house ) )
        if temp_radius > 161834419:
            break
        res = max( res , temp_radius )
    return res


houses = [ 1 , 2 , 3 , 4 ]
heaters = [ 1 , 4 ]
houses = [ 282475249 , 622650073 , 984943658 , 144108930 , 470211272 , 101027544 , 457850878 , 458777923 ]
heaters = [ 823564440 , 115438165 , 784484492 , 74243042 , 114807987 , 137522503 , 441282327 , 16531729 , 823378840 , 143542612 ]
bis.bisect_left( heaters , 0 )
if __name__ == '__main__' :
    print( findRadius( houses , heaters ) )
    print( "finished!" )
