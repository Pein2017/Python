'''
作者：卢沛安
时间：2022年10月09日
'''
from typing import List , Tuple , Dict , Optional
from collections import  Counter

# goal = 'abc'
class Solution :
    def solve( self , words: List[ str ] , goal : str , order : int )  -> List[str] :
        target = sorted( goal )
        division = Counter( target )
        res = []
        for word in words:
            if word != goal:
                temp = Counter( sorted(word) )
                if temp == division:
                    res += [word]
            else:
                continue
        res = sorted( res )
        ans = []
        n = len( res )
        ans.append( n )
        if order <= n:
            ans.append( res[order-1])
        else:
            ans.append(False)
        return ans
sol = Solution()

while 1:
    try:
        data = input( ).split()
        number = int( data[0] )
        order = int( data[-1] )
        words = []
        for i in range(1,1+number):
            words.append( data[i] )
        goal = data[-2]
        output = sol.solve( words , goal, order )
        o1 = output[0]
        o2 = output[1]
        print( o1 )
        if o2 !=False:
            print(o2)

    except:
        break



if __name__ == '__main__' :
    print( "finished!" )
