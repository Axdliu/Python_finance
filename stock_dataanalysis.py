# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 18:05:08 2017

@author: User
"""

import pandas.io.data as web
import numpy as np
import pandas as pd
import math

DAX = web.DataReader(name='^GDAXI', data_source='yahoo', start='2000-1-1')
print DAX.info()
print DAX.tail()
DAX['Close'].plot(figsize=(8, 5))

DAX['Ret_Loop'] = 0.0
DAX['Return'] = np.log(DAX['Close'] / DAX['Close'].shift(1))
DAX['Return1'] = DAX['Close'] / DAX['Close'].shift(1) - 1
DAX['diff'] = DAX['Return'] - DAX['Return1']
del DAX['Return1']
DAX[['Close', 'Return']].plot(subplots=True, style='b', figsize=(8, 5))

DAX['42d'] = pd.rolling_mean(DAX['Close'], window=42)
DAX['252d'] = pd.rolling_mean(DAX['Close'], window=252)
DAX[['Close', '42d', '252d']].tail()

# moving annual volatility
DAX['Mov_Vol'] = pd.rolling_std(DAX['Return'],\
                    window=252) * math.sqrt(252)
DAX[['Close', 'Mov_Vol', 'Return']].plot(subplots=True, style='b', figsize=(8, 7))
