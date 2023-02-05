'''
作者：卢沛安
时间：2022年11月01日
'''
from typing import List , Tuple , Dict , Optional
import numpy as np
import pandas as pd

df = pd.read_csv( 'pandas/冬奥奖牌/东京奖牌.txt' , sep=',' )
d_name = list( df.columns )
d_name[ 2 :5 ] = [ '金牌数' , '银牌数' , '铜牌数' ]
df.columns = d_name

# 设置索引
df.set_index( '排名' , inplace=True )
# 修改索引名字
df.rename_axis( '金牌排名' , inplace=True )

df.iloc[ 4 , 0 ] = '俄奥委会'

# 替换
df[ '金牌数' ].replace( 0 , '无' , inplace=True )
df.replace( [ '无' , 0 ] , [ np.nan , 'None' ] , inplace=True )
# 修改变脸类型
df[ '金牌数' ] = df[ '金牌数' ].fillna( '0' ).astype( int )

# 新增一列
df[ '比赛地点' ] = '东京'

df[ '银牌数' ] = df[ '银牌数' ].replace( 'None' , np.nan ).fillna( '0' ).astype( int )
df[ '金银牌总数' ] = df[ '金牌数' ] + df[ '银牌数' ]


def getMax( array ) :
    return max( array )


df[ '铜牌数' ] = df[ '铜牌数' ].replace( 'None' , np.nan ).fillna( '0' ).astype( int )
df[ '最多奖牌数量' ] = df[ [ '金牌数' , '银牌数' , '铜牌数' ] ].apply( getMax , axis=1 )
df = df.drop( labels='最多奖牌数量' , axis=1 )

df[ '金牌大于30' ] = np.where( df[ '金牌数' ] >= 30 , '是' , '否' )

df = df.drop( df.columns[ 9 ] , axis=1 )

gold_sum = df[ '金牌数' ].sum()
df[ '金牌占比' ] = df[ '金牌数' ] / gold_sum

# 新增一行
new_row = pd.DataFrame( [ [ i for i in range( df.shape[ 1 ] ) ] ] , columns=df.columns )
df = pd.concat( [ df , new_row ] )

# 指定位置新增一行
df1 = df.iloc[ :1 , : ]
df2 = df.iloc[ 2 : , : ]
new_row = pd.DataFrame( [ [ i for i in range( df.shape[ 1 ] ) ] ] , columns=df.columns )
df = pd.concat( [ df1 , new_row , df2 ] )
df = df.reset_index( drop = True)
# 删除
    # 删除第一行
df =df.drop( df.columns[0:1] ,axis = 1)
df = df.drop( 30 , axis = 0 ).reset_index( drop = True)

df = df.drop( df[df['金牌数'] < 20].index , axis = 0)
if __name__ == '__main__' :
    print( "finished!" )
