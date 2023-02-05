'''
作者：卢沛安
时间：2022年11月01日
'''
from typing import List , Tuple , Dict , Optional
import numpy as np
import pandas as pd

pd.set_option( 'display.max_colwidth' , 10 )

data = pd.DataFrame( [ 1 , 2 , 3 , 4 ] , columns=[ 'a' ] )
d = {"one" : [ 1 , 2 , 3 ] , 'two' : [ 4 , 5 , 6 ]}
data = pd.DataFrame( d , index=[ 'a' , 'b' , 'c' ] )
data.columns = [ 'test1' , 'test2' ]

df = pd.read_excel( "pandas/TOP250/TOP250.xlsx" )
df.sample()
df.info()
df.describe().round( 2 ).T

# 查看缺失值
# 查看全部缺失值
df.isna().sum()
df.isna().sum().sum()
# 查看列的缺失值
df.isnull().sum()

# 定位缺失值
df[ df.isnull().T.any() == True ]
df[ df.isnull().T.any() == True ].style.highlight_null( null_color='skyblue' ).set_table_attributes(
    'style="font-size: 10px"' )

# 删除缺失值的  行 row
df = df.dropna()
# 填补缺失值
df = df.fillna( '*' )

# 向上填充补全
df[ '评分' ] = df[ '评分' ].fillna( axis=0 , method='ffill' )
df[ '评价人数' ].isna().sum()
df[ '评价人数' ] = df[ '评价人数' ].fillna( df[ '评价人数' ].mean() )
# 使用缺失值位置的上下均值进行填充
df[ '评价人数' ].isna().sum()
df[ '评价人数' ] = df[ '评价人数' ].fillna( df[ '评价人数' ].interpolate() )

# 现在填充 “语言” 列的缺失值，要求根据 “国家/地区” 列的值进行填充
# bfill 向前填充， 默认按列填充
df[ '语言' ] = df.groupby( [ '国家/地区' , '上映年份' ] ).语言.bfill()
# 查看groupby 后
df.groupby( [ '国家/地区' , '上映年份' ] ).groups
# get_group
df.groupby( [ '国家/地区' , '上映年份' ] ).get_group( ('中国' , 2000) )

# 查找全部重复值
# 将重复值所在 行 row 选出
df[ df.duplicated() ]
# 上面是所有列完全重复的情况，但有时我们只需要根据某列查找缺失值

df[ df.duplicated( [ '片名' ] ) ]
# 删除全部的重复值
df = pd.read_excel( "pandas/TOP250/TOP250.xlsx" )
df = df.drop_duplicates( )
# 删除全部的重复值，但保留最后一次出现的行
df = df.drop_duplicates( keep = 'last')
if __name__ == '__main__' :
    print( "finished!" )
