'''
作者：卢沛安
时间：2022年11月04日
'''
from typing import List , Tuple , Dict , Optional
import numpy as np
import pandas as pd

df = pd.read_csv( 'pandas/超市数据/超市销售.txt' , thousands=',' )
# 数据透视

# 制作各省「平均销售额」的数据透视表
pd.pivot_table( df , values='销售额' , index='省/自治区' )
df.groupby( "省/自治区" )[ '销售额' ].mean()

# 指定维度
## 制作各省「销售总额」的数据透视表
pd.pivot_table( df , values='销售额' , index='省/自治区' , aggfunc=sum )
## 制作各省「销售总额」与「平均销售额」的数据透视表
pd.pivot_table( df , values='销售额' , index='省/自治区' , aggfunc=[ sum , np.mean ] )

# 组合多列
## 制作各类别「销售总额」、「利润总额」与 [数量综合] 的数据透视表
pd.pivot_table( df , values=[ '销售额' , '利润' , '数量' ] , index='类别' , aggfunc=sum )

## 制作「各省市」与「不同类别」产品「销售总额」的数据透视表
pd.pivot_table( df , values = ['销售额'] ,  index= ['省/自治区' , '类别']  , aggfunc= sum)

# 多层透视
## 制作各省市「不同类别」产品的「销售总额」透视表
pd.pivot_table( df , values = ['销售额'] ,  index= ['省/自治区'] ,columns='类别' , aggfunc= sum)

# 综合使用
## 制作「各省市」、「不同类别」产品「销售量与销售额」的「均值与总和」的数据透视表，并在最后追加一行『合计』
t1 = pd.pivot_table( df , values = ['销售额','数量'] ,  index= ['省/自治区','类别']  , aggfunc= [np.mean,sum] , margins = True)
print(t1)

##  在上一题的基础上，查询 「类别」 等于 「办公用品」 的详情
t1.query( '类别 == "办公用品" ')

# 逆透视
t2 = pd.pivot_table(df,values = ['销售额','利润','数量'],index = '类别',aggfunc = sum)
t2.melt( id_vars= '数量' , var_name='分裂' , value_name = '金额')
if __name__ == '__main__' :
    print( "finished!" )
