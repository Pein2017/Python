'''
作者：卢沛安
时间：2022年10月18日
'''
from typing import List , Tuple , Dict , Optional

def lengthOfLongestSubstring( s: str) -> int:
    n = len( s )
    windows = ''
    res = 0
    windows_size = 0
    for i in range( n ):
        adding = s[i]
        if adding not in windows:
            windows += adding
            windows_size +=1
            if windows_size > res:
                res = windows_size
                print( windows )
        else:
            while adding in windows:
                windows = windows[1:]
                print( windows )
                windows_size -= 1
            windows += adding
            windows_size += 1

    return res
s = "abcabcbb"
s = "bbbbb"
s = "pwwkew"
s = 'aab'
print( lengthOfLongestSubstring( s ))

if __name__ == '__main__' :
    print( "finished!" )
