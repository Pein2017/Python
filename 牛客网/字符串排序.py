'''
作者：卢沛安
时间：2022年10月09日
'''
from typing import List , Tuple , Dict , Optional

class Solution:
    def solve( self,  sentence: str ) -> str:
        a = ''
        for i in sentence:
            if i.isalpha():
                a +=i
        b = sorted( a , key = str.upper )    # key = str.upper   / lower
        index = 0
        res = ''
        for word in sentence:
            if word.isalpha():
                res += b[index]
                index +=1
            else:
                res += word
        return res
sol = Solution()

while 1:
    try:
        s = input()
        ans = sol.solve( s )
        print(ans)
    except:
        break


if __name__ == '__main__' :
    print( "finished!" )
