'''
作者：卢沛安
时间：2022年10月08日
'''
from typing import List , Tuple , Dict , Optional


'''
如果设置 .requires_grad 为 True，那么将会追踪所有对于该张量的操作。 
当完成计算后通过调用 .backward()，自动计算所有的梯度， 这个张量的所有梯度将会自动积累到 .grad 属性。
'''

import torch

x = torch.tensor(1.).requires_grad_() # 第一种

x = torch.tensor(1., requires_grad=True) # 第二种

x = torch.ones( 2 , 2 , requires_grad=True )

x = torch.tensor(2.).requires_grad_()
y = torch.tensor(3.).requires_grad_()

z = x * x * y

z.backward()

print( x.grad , y.grad)

grad_x = torch.autograd.grad(outputs=z, inputs=x , create_graph= True)
grad_y = torch.autograd.grad(outputs=z, inputs=y)
grad_xx = torch.autograd.grad( outputs= grad_x  , inputs = x ) #  d_gradX / d_x , 相当于二阶导
# 也可以用多次grad.backward()
z.backward(create_graph=True)
x.grad.nums.zero_()
x.grad.backward()


print(grad_x[0], grad_y[0])

y = x + 2
print( y )
print( y.grad_fn )

y = torch.tensor( [ 1 , 2 , 3 , 4 ] , dtype=torch.float )
y = y.view( 2 , 2 )

z = y * y * 3
out = z.mean()
print( z , out )

# Gradient
'''
O = 1/4 * \sum_{1}^{4} 3*(x_i + 2)^2 
dO/dx_i = 3/2 (x_i + 2)
则, dO/dx_i | x_i = 1  = 9/2 = 4.5  
'''

x = torch.ones( 2 , 2 , dtype=torch.float , requires_grad=True )
y = x + 2
print( y )
print( y.grad_fn )
z = y * y * 3
out = z.mean()
print( z , out )
out.backward()
print( x.grad )

############# Vector-Jacobian Product 当Y不是标量时

x = torch.randn( 3 , requires_grad=True )
y = x * 2
while y.data.norm() < 1000 :
    y = y * 2

print( y )
# 需要将向量作为参数传入 backward()

gradients = torch.tensor( [ 0.1 , 1.0 , 0.0001 ] , dtype=torch.float )
y.backward( gradients )

print( x.grad )

if __name__ == '__main__' :
    print( "finished!" )
