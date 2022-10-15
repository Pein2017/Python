'''
作者：卢沛安
时间：2022年10月08日
'''
from typing import List , Tuple , Dict , Optional

import pylab
import matplotlib.pyplot as plt
# %matplotlib inline

'''
训练一个图像分类器
依次按照下列顺序进行：

    1.使用torchvision加载和归一化CIFAR10训练集和测试集
    2.定义一个卷积神经网络
    3.定义损失函数
    4.在训练集上训练网络
    5.在测试集上测试网络
'''
# 使用torchvision可以非常容易地加载CIFAR10
import torch
import torchvision
import torchvision.transforms as transforms

# torchvision的输出是[0,1]的PILImage图像，我们把它转换为归一化范围为[-1, 1]的张量。
transform = transforms.Compose(
    [transforms.ToTensor(),
     transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

trainset = torchvision.datasets.CIFAR10(root='./data', train=True,
                                        download=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=4,
                                          shuffle=True, num_workers=2)

testset = torchvision.datasets.CIFAR10(root='./data', train=False,
                                       download=True, transform=transform)
testloader = torch.utils.data.DataLoader(testset, batch_size=4,
                                         shuffle=False, num_workers=2)

classes = ('plane', 'car', 'bird', 'cat',
           'deer', 'dog', 'frog', 'horse', 'ship', 'truck')

# 展示训练图片
import matplotlib.pyplot as plt
import numpy as np

def imshow(img):
    img = img / 2 + 0.5     # unnormalize
    npimg = img.numpy()
    plt.imshow(np.transpose(npimg, (1, 2, 0)))

# 获取随机数据
dataiter = iter(trainloader)
images, labels = dataiter.next()

# 展示图像
plt.imshow( torchvision.utils.make_grid( images ) )
# 显示图像标签
print(' '.join('%5s' % classes[labels[j]] for j in range(4)))


if __name__ == '__main__' :
    print( "finished!" )
