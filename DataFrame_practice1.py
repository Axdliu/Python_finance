# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 00:50:54 2017
DataFrame Class practice

@author: User
"""

import numpy as np
import pandas as pd
import matplotlib as mpl
import pandas.io.data as web

a = (np.random.standard_normal((9, 4))).round(6)
df = pd.DataFrame(a)
df.columns = [['No1', 'No2', 'No3', 'No4']]
print df['No2'][3]
# the options of freq are B, C, D, W, M, BM, MS, BMS, Q, 
# BQ, QS, BQS, A, BA, AS, BAS, H, T, S, L, U
dates = pd.date_range('2015-1-1', periods=9, freq='M')
df.index = dates
print df.sum()
print df.mean()
print df.cumsum()
# statistic descriptions
print df.describe()
print np.sqrt(df)
print np.sqrt(df).sum()
df.cumsum().plot(lw=2.0)
df['Quarter'] = ['Q1', 'Q1', 'Q1', 'Q2', 'Q2', 'Q2', 'Q3', 'Q3', 'Q3']
groups = df.groupby('Quarter')
print groups.mean()
print groups.max()
print groups.size()
df['Odd_Even'] = ['Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even',\
                    'Odd', 'Even', 'Odd']
groups = df.groupby(['Quarter', 'Odd_Even'])
print groups.size()
print groups.mean()

DAX = web.DataReader(name='^AAPL', data_source='yahoo',\
                     start='2000-1-1')

