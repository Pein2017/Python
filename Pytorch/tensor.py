'''
作者：卢沛安
时间：2022年10月08日
'''
from typing import List , Tuple , Dict , Optional
%matplotlib inline

import torch
x = torch.empty(5, 3)
print(x)

x = torch.zeros(5, 3, dtype=torch.long)
print(x)

x = torch.tensor([5.5, 3])
print(x)
print("创建全是1的矩阵")
x = x.new_ones(5, 3, dtype=torch.double)      # new_* 方法来创建对象
print(x)
print("创建跟x维度相同的tensor")
x = torch.randn_like(x, dtype=torch.float)    # 覆盖 dtype!
print(x)
print("tensor也支持.size()")
print(x.size())


###        加法运算
y = torch.rand(5, 3)
print(x + y)
print(torch.add(x, y))
print("也可以， 提供输出tensor作为参数 ")
result = torch.empty(5, 3)
torch.add(x, y, out=result)
print(result)
print("将y += x ,替换原来的变量")
y.add_(x)
print(y)

'''
pytorch专属：
任何 以``_`` 结尾的操作都会用结果替换原变量. 例如: ``x.copy_(y)``, ``x.t_()``, 都会改变 ``x``.
如, a.add_(1)，则a会自动+1
'''

print( "view 和 numpy.reshape 相似")
x = torch.randn(2, 2)
y = x.view(16)
z = x.view(-1, 8)  #  size -1 从其他维度推断
print(x.size(), y.size(), z.size())
##### Numpy Pytorch转换
'''
Torch Tensor与NumPy数组共享底层内存地址，修改一个会导致另一个的变化。
'''
a = torch.ones(3)
b = a.numpy()
print(a,b)
print("底层共享内存地址！")
a.add_(1)
print(a)
print(b)

import numpy as np
a = np.ones(3)
b = torch.from_numpy( a )
np.add( a , 1 , out = a )
print(a,b)

### CUDA 张量
'''
使用.to 方法 可以将Tensor移动到任何设备中
'''

device = torch.device( "cuda" )  # a CUDA 设备对象
y = torch.ones_like( x , device=device )  # 直接从GPU创建张量
x = x.to( device )  # 或者直接使用``.to("cuda")``将张量移动到cuda中
z = x + y
print( z )
print( z.to( "cpu" , torch.double ) )  # ``.to`` 也会对变量的类型做更改

if __name__ == '__main__' :
    print( "finished" )
