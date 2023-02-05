'''
作者：卢沛安
时间：2022年11月04日
'''
from typing import List , Tuple , Dict , Optional
import numpy as np
import pandas as pd

pd.Timestamp( 'now' )

# 生成指定时间范围
pd.date_range( '1/1/2021' , '9/11/2021' )
# 生成指定间隔时间
pd.date_range( '1/1/2021' , '9/11/2021' , periods=10 )
# 生成指定频率时间
pd.date_range( "2021-01-01" , periods=7 , freq="W" )
# 生成 工作日 时间
pd.bdate_range( start='1/1/2021' , end='9/1/2021' , freq='D' )
# 计算时间差
(pd.Timestamp( 'now' ) - pd.to_datetime( '2021-10-31' )).days
# 小时
(pd.Timestamp( 'now' ) - pd.to_datetime( '2021-10-31' )) / np.timedelta64( 1 , 'h' )

# 将现在的时间减去一天，并格式化
(pd.Timestamp( 'now' ) - pd.to_timedelta( '1 day' ))
(pd.Timestamp( 'now' ) - pd.to_timedelta( '1 day' )).strftime( '%Y年%M月%D日 - %H时%M分%S秒' )


weight = np.array( [15,60,15,15,15,15,30,15] )
weight = weight / np.sum( weight )

values = np.array( [ 0.5 , 0.72 , 0.85,0.82,0.77,0.77,0.95,0.54])
weight.T.dot( values )

even_weight =np.array([1] * len(weight) )
even_weight = even_weight / np.sum( even_weight)
even_weight.T.dot( values )


if __name__ == '__main__' :
    print( "finished!" )
