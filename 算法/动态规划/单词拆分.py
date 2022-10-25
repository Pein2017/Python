'''
作者：卢沛安
时间：2022年10月23日
'''
from typing import List , Tuple , Dict , Optional


from timer_func import timer

def wordBreak( s: str , wordDict: List[ str ] ) -> bool :
    n = len( s )
    dp = [ False ] * (n + 1)
    wordDict = set( wordDict )
    dp[ 0 ] = True
    for i in range( 1 , n + 1 ) :
        for j in range( i ) :
            if dp[ j ] and s[ j :i ] in wordDict :
                dp[ i ] = True
    return dp[ -1 ]


def wordBreak2( s: str , wordDict: List[ str ] ) -> bool :
    n = len( s )
    dp = [ False ] * (n + 1)
    # wordDict = set( wordDict )
    dp[ 0 ] = True
    for i in range( 1 , n + 1 ) :
        for j in range( i ) :
            if dp[ j ] and s[ j :i ] in wordDict :
                dp[ i ] = True
    return dp[ -1 ]


def wordBreak3( s: str , wordDict: List[ str ] ) -> bool :
    n = len( s )
    dp = [ False ] * (n + 1)
    wordDict = dict.fromkeys( wordDict , 1 )
    dp[ 0 ] = True
    for i in range( 1 , n + 1 ) :
        for j in range( i ) :
            if dp[ j ] and wordDict.get( s[ j :i ] ) :
                dp[ i ] = True
    return dp[ -1 ]


b= [ 1,2,3,4,5]

@timer
def test1( n=500 ) :
    for i in range( n ) :
        wordBreak( s , wordDict )


@timer
def test2( n=500 ) :
    for i in range( n ) :
        wordBreak2( s , wordDict )


@timer
def test3( n=500 ) :
    for i in range( n ) :
        wordBreak3( s , wordDict )


if __name__ == '__main__' :
    s = "leetcodeleetleetleetleetleetleetleetleetleetleetleetleetleetleetleetcodecodecodecodecodecodecodecode"
    wordDict = [ "leet" , "code" , "a" , "b" , "c" , "d" , 'E' , "f" ]
    n = 10000
    test1( n )
    test2( n )
    test3( n )

    print( "finished!" )
