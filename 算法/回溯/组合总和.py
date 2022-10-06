'''
作者：卢沛安
时间：2022年09月26日
'''
from typing import List , Tuple , Dict , Optional

'''
找出所有相加之和为 n 的 k 个数的组合，且满足下列条件：
    只使用数字1到9
    每个数字 最多使用一次 
    
输入: k = 3, n = 9
输出: [[1,2,6], [1,3,5], [2,3,4]]
'''


def combinationSum3( k: int , n: int ) -> List[ List[ int ] ] :
    path , result = [ ] , [ ]

    def backtrack( target_Sum: int , start: int , k: int ) -> None :
        if sum( path ) > target_Sum :
            return
        if len( path ) == k :
            if sum( path ) == target_Sum :
                result.append( path[ : ] )
            return
        for i in range( start ,
                        10 - (k - len( path )) + 1 ) :  # 如果构不成k个组合时，就没必要了。如 [1] 和 k = 3，没必要遍历到9， 因为 [1,9]后面构不成 k=3
            path.append( i )
            backtrack( target_Sum , i + 1 , k )
            path.pop()

    backtrack( n , 1 , k )
    return result


if __name__ == '__main__' :
    print( combinationSum3( 3 , 9 ) )
    print( "finished" )
