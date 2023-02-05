'''
作者：卢沛安
时间：2022年11月01日
'''
from typing import List , Tuple , Dict , Optional
import numpy as np
import pandas as pd

pd.set_option( 'display.max_colwidth' , 10 )
df = pd.read_excel( 'pandas/TOP250/2020年中国大学排名/2020年中国大学排名.xlsx' )

df.head()
df.size
df.sort_values( by = '总分' , ascending= True).head(10)

# 按照指定列排序
df.nlargest( 10 , '高端人才得分')

index = df.iloc[:,4:].idxmax()
df['学校名称'][index]

# 基本统计量
df.总分.mean()
df.总分.median()
df.总分.mode()

# 统计agg

df.agg(  {
    '总分' : ['min','max','mean'],
    '高端人才得分': [ 'min' ,'max' , 'mean']
}   )

# 计算各省平均值
df.groupby('省市').总分.mean()
df.groupby('省市')['总分'].mean()

# COR
df.corr()

# 频率
df['省市'].value_counts()
from matplotlib import pyplot as plt
import seaborn as sns
plt.figure(figsize = (9,6),dpi=100)
sns.set(font='Songti SC')
sns.distplot(df['总分'])
plt.show( block = True )

if __name__ == '__main__' :
    print( "finished!" )
