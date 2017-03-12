# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 18:03:41 2017
Regression Analysis
@author: User
"""

import pandas as pd
from urllib import urlretrieve
import datetime as dt
import numpy as np
import matplotlib as mlp
import matplotlib.pyplot as plt

es_url = 'http://www.stoxx.com/download/historical_values/hbrbcpe.txt'
vs_url = 'http://www.stoxx.com/download/historical_values/h_vstoxx.txt'
urlretrieve(es_url, './data/es.txt')
urlretrieve(vs_url, './data/vs.txt')

lines = open('./data/es.txt', 'r').readlines()
lines = [line.replace(' ', '') for line in lines]

'''
From December 27, there suddenly appears an additional 
semicolon at the end of each data row:
    322.55;272.18;5360.52;370.94
    322.69;272.95;5360.52;370.94
    327.57;277.68;5479.59;378.69;
    329.94;278.87;5585.35;386.99;
to fix it, we will do the following:
1. Generate a new text file.
2. Delete unneeded header lines.
3. Write an appropriate new header line to the new file.
4. Add a helper column, DEL (to catch the trailing semicolons).
5. Write all data rows to the new file.
'''

new_file = open('./data/es50.txt', 'w')
# opens a new file
new_file.writelines('date' + lines[3][:-1] \
                    + ';DEL' + lines[3][-1])
# writes the corrected third line of the original file
# as first line of new file
new_file.writelines(lines[4:])
# writes the remaining lines of the orignial file
new_file.close()

new_lines = open('./data/es50.txt', 'r').readlines()
es1 = pd.read_csv('./data/es50.txt', index_col=0, \
                 parse_dates=True, sep=';', dayfirst=True)
del es1['DEL']

# An alternative way of reading data
cols = ['SX5P', 'SX5E', 'SXXP', 'SXXE', 'SXXF', 'SXXA', 'DK5F', 'DKXF']
es = pd.read_csv(es_url, index_col=0, parse_dates=True, \
                 sep=';', dayfirst=True, header=None, skiprows=4, names=cols)

vs = pd.read_csv('./data/vs.txt', index_col=0, header=2, \
                 parse_dates=True, sep=',', dayfirst=True)

data = pd.DataFrame({'EUROSTOXX' :
                    es['SX5E'][es.index > dt.datetime(1999, 1, 1)]})
data = data.join(pd.DataFrame({'VSTOXX' :
                    vs['V2TX'][vs.index > dt.datetime(1999, 1, 1)]}))

data['EUROSTOXX'].loc['2016-03-28'] = None
data['EUROSTOXX'].loc['2016-03-25'] = None
data = data.fillna(method='ffill')
data.plot(subplots=True, grid=True, style='b', figsize=(8, 6))

rets = np.log(data / data.shift(1))
print rets.head()

xdat = rets['EUROSTOXX']
ydat = rets['VSTOXX']
model = pd.ols(y=ydat, x=xdat)
print model.beta

plt.plot(xdat, ydat, 'r.')
ax = plt.axis() # grab axis values
x = np.linspace(ax[0], ax[1] + 0.01)
plt.plot(x, model.beta[1] + model.beta[0] * x, 'b', lw=2)
plt.grid(True)
plt.axis('tight')
plt.xlabel('EURO STOXX 50 returns')
plt.ylabel('VSTOXX returns')

pd.rolling_corr(rets['EUROSTOXX'], rets['VSTOXX'], \
                window=252).plot(grid=True, style='b')
