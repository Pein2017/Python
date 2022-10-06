'''
作者：卢沛安
时间：2022年10月03日
'''
from typing import List , Tuple , Dict , Optional
import torch

if __name__ == '__main__' :
    x = torch.rand( 5 , 3 )
    print( x )
    a = torch.cuda.is_available()
    print(a)
    print( "finished" )
