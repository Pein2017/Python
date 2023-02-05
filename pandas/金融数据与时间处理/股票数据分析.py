'''
作者：卢沛安
时间：2022年11月04日
'''
from typing import List , Tuple , Dict , Optional
import numpy as np
import pandas as pd

df1 = pd.read_csv( "pandas/金融数据与时间处理/1day.txt" )
# ['日期', '开盘', '收盘', '最高', '最低', '成交量', '成交额', '振幅', '涨跌幅', '涨跌额', '换手率']

df2 = pd.read_csv( "pandas/金融数据与时间处理/5mins.txt" )
# ['时间', '开盘', '收盘', '最高', '最低', '涨跌幅', '涨跌额', '成交量', '成交额', '振幅', '换手率']

#
df1[ '日期' ] = pd.to_datetime( df1[ '日期' ] )
df2[ '时间' ] = pd.to_datetime( df2[ '时间' ] )

# 按区间筛选
## 2021-08-03 09:35:00 与 2021-08-04 15:00:00
df2[ (df2[ '时间' ] > pd.to_datetime( '2021-08-03 09:35:00 ' )) & (df2[ '时间' ] < pd.to_datetime(
    '2021-08-04 15:00:00' )) ]

## 按指定时间筛选  2021-08-03
df2.set_index( '时间' ).truncate( after=pd.Timestamp( '2021-08-04' ) )
df2[ df2[ '时间' ].dt.date == pd.to_datetime( '2021-08-03' ) ]  # dt.year, dt.month, dt.day, dt.time, dt.hour

# 计算涨跌
df1[ '涨跌' ] = df1.收盘.diff()

# 涨跌变化率
df1[ '涨跌变化率' ] = (df1.收盘.pct_change()).round( 2 )  # .apply(lambda x: format(x, '.2%'))

# 移动均值 计算收盘价的5日移动均线
df1.收盘.rolling( window=5 ).mean()
df1.收盘.rolling( window=5 ).mean().plot(  )
#df1.set_index("日期")['收盘'].rolling(20).mean().plot()

# 指数移动平均值（EMA）
df1['EMA20'] = df1['收盘'].ewm(span=20,min_periods=0,adjust=False,ignore_na=False).mean()

# MACD
exp1 = df1['收盘'].ewm(span=12, adjust=False).mean()
exp2 = df1['收盘'].ewm(span=26, adjust=False).mean()
df1['MACD'] = exp1 - exp2
df1['Signal line'] = df1['MACD'].ewm(span=9, adjust=False).mean()

# 绘制布林指标
df1['former 30 days rolling Close mean'] = df1['收盘'].rolling(20).mean()
df1['upper bound'] = df1['former 30 days rolling Close mean'] + \
    2*df1['收盘'].rolling(20).std()  # 在这里我们取20天内的标准差
df1['lower bound'] = df1['former 30 days rolling Close mean'] - \
    2*df1['收盘'].rolling(20).std()

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Songti SC'] #设置中文，如果本句代码导致失效，可以点击https://mp.weixin.qq.com/s/WKOGvQP-6QUAP00ZXjhweg

df1.set_index("日期")[['收盘', 'former 30 days rolling Close mean','upper bound','lower bound' ]].plot(figsize=(16, 6))

plt.show( block = True)
if __name__ == '__main__' :
    print( "finished!" )
