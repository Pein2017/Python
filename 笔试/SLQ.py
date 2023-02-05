'''
作者：卢沛安
时间：2022年10月30日
'''
from typing import List , Tuple , Dict , Optional
import numpy as np
import pandas as pd
from collections import Counter
data = pd.DataFrame
def getMonth( date ):
    month = int( str( date )[-4:-2]  )
    return month
i=0
for day in data['DAY_OPENED']:
    data['DAY_OPENED'].iloc[0] = getMonth( day )
ans = {}
for month in range(1,13):
    ans[month] = Counter( data[ data['DAY_OPENED'] == month] )

record = []
for i in range( data.shape[0] ):
    card_number , date , bill , type = data[i, ['CARD_NBR','INP_DATE' , 'BILL','TRAN_TYPE'] ]
    if getMonth(date) <=6 and type == 'POS消费':
        record.append( [card_number,bill] )







if __name__ == '__main__' :
    print( "finished!" )
