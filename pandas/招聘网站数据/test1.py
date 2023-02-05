'''
作者：卢沛安
时间：2022年11月01日
'''
from typing import List , Tuple , Dict , Optional
import numpy as np
import pandas as pd

df = pd.read_csv( 'pandas/招聘网站数据/招聘网站数据.txt' , sep=',' )

'''
['positionName', 'companySize', 'industryField', 'financeStage',
       'companyLabelList', 'firstType', 'secondType', 'thirdType',
       'createTime', 'district', 'salary', 'workYear', 'jobNature',
       'education', 'positionAdvantage', 'imState', 'score', 'matchScore',
       'famousCompany']
'''
# 统计各个district的薪资

df[ df[ 'positionName' ] == '数据分析' ].index
df[ df[ 'positionName' ] == '数据分析' ].loc[ : , [ 'district' , 'salary' ] ].groupby( by='district' ).mean()

df[ [ 'district' , 'salary' ] ].groupby( by='district' ).mean()
df.groupby( 'district' , as_index=False )[ 'salary' ].mean()

# 计算并提取平均薪水最高的区
df[ [ 'district' , 'salary' ] ].groupby( by='district' ).mean().sort_values( 'salary' , ascending=False )

# 计算不同行政区(district)，不同规模公司(companySize)出现的次数

df.groupby( 'district' )[ 'companySize' ].value_counts()
df.groupby( [ 'district' , 'companySize' ] ).size()

# 更改索引名字
t1 = pd.DataFrame( df.groupby( 'district' )[ 'companySize' ].value_counts() ).rename_axis( [ '行政区' , '公司规模' ] )

# 统计上述每个区公司的数量
df.groupby( 'district' )[ 'companySize' ].count()

# 分组查看
df.groupby( [ 'district' , 'salary' ] ).get_group( ('西湖区' , 30000) )

# createTime 列，计算每天不同 行政区 新增的岗位数量
df.groupby( df[ 'createTime' ].apply( lambda x : x.day ) )[ 'district' ].value_counts().rename_axis(
    [ '发布时间' , '行政区' ] )

#
df.groupby( 'district' )[ 'industryField' ].apply( lambda x : x.str.contains( '电商' ).sum() )

df.set_index( 'positionName' ).groupby( len )[ 'salary' ].mean()
# 通过字典分组，将score和matchScore的 和 记为“总分”
df.groupby( {'salary' : '薪资' , 'score' : '总分' , 'matchScore' : '总分'} , axis=1 ).sum()

# 计算不同工作年限和学历之间的平均薪资
df.groupby( [ 'workYear' , 'education' ] )[ 'salary' ].mean()

# 添加新列： 该区域的平均薪资 Transform
df[ '该区平均薪资' ] = df[ [ 'district' , 'salary' ] ].groupby( 'district' ).mean()


def f( nums ) :
    return np.mean( nums[ 'salary' ] ) < 30000


# 分组过滤 Filter
df.groupby( 'district' ).filter( lambda x : x[ 'salary' ].mean() < 30000 )

df.groupby( df.index ).filter( lambda x : x[ '该区平均薪资' ] < 30000 )

# import matplotlib.pyplot as plt
# %config InlineBackend.figure_format = 'retina'
# plt.rcParams['font.sans-serif'] = ['Songti SC']
#
# df.groupby("district")['positionName'].count().plot(
#     kind='bar', figsize=(4, 2), color='#5172F0', fontsize=6)
# plt.ylabel("公司数量",fontsize = 8)
# plt.xlabel("杭州市各区",fontsize = 8)
# plt.show( block = True )

# 聚合统计
## 分组计算不同行政区，薪水的最小值、最大值和平均值
pd.DataFrame( df.groupby( 'district' , as_index=False )[ 'salary' ].agg( [ min , max , np.mean ] ) ,
              columns=[ '最小' , '最大' , '均值' ] )

pd.DataFrame( df.groupby( 'district' , as_index=False )[ 'salary' ].agg( [ min , max , np.mean ] ) ).columns

## 修改名字
df.groupby( 'district' )[ 'salary' ].agg( 最低工资='min' , 平均='mean' ).rename_axis( '行政区' )

# 对不同岗位(positionName)进行分组，并统计其薪水(salary)中位数和得分(score)均值
df.groupby( 'positionName' ).agg( 薪水中位数=('salary' , 'median') , 得分均值=('score' , 'mean') ).sort_values(
    '薪水中位数' , ascending=False )

# 多层统计

df.groupby( 'district' ).agg( {'salary' : [ np.mean , np.median , np.std ] , 'score' : np.mean} )
df.groupby( 'district' ).agg( 均值=('salary' , 'mean') , 中位数=('salary' , 'median') , 分数=('score' , 'mean') )


# 自定义函数
## 在聚合计算时新增一列计算最大值与平均值的差值
def myfunc( x ) :
    return np.max( x ) - np.mean( x )


df.groupby( 'district' ).agg( 薪水中位数=('salary' , 'median') , 得分均值=('score' , 'mean') ,
                              最大值与均值差=('salary' , myfunc) ).rename_axis( '行政区' ).sort_values( '薪水中位数' ,
                                                                                                        ascending=False )

if __name__ == '__main__' :
    print( "finished!" )
