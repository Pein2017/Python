'''
作者：卢沛安
时间：2022年10月11日
'''
from typing import List , Tuple , Dict , Optional

'''
IN:
AB-ABC-cABd-Cb@
2
OUT:
AB-AB-CC-AB-dc-b@

'''
head , tail = input().split( '-' , 1 )
k = int( input() )
tail = tail.replace( '-' , '')
temp = ''
for index in range(0 , len(tail) , 3 ):
    line = tail[ index : index + 3 ]
    lower_count , upper_count = 0 , 0
    for letter in line:
        if 'A' <= letter <= 'Z':
            upper_count +=1
        elif 'a' <= letter <= 'z':
            lower_count +=1
        else:
            pass
    if upper_count == lower_count:
        temp += line
    elif upper_count > lower_count:
        temp += line.upper()
    else:
        temp += line.lower()

ans = [ head ]

for index in range( 0,len( temp ) , k ):
    ans.append( temp[index : index + k ] )

print( "-".join( i for i in ans))
print( "-".join( ans ))






if __name__ == '__main__' :
    print( "finished!" )
