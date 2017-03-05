# -*- coding: utf-8 -*-
"""
Created on Sun Mar 05 10:22:35 2017

However, we have to keep in mind that we completely neglect operational issues (like
trade execution) and relevant market microstructure elements (e.g., transaction costs). For
example, we are working with daily closing values. A question would be when to execute
an exit from the market (from being long to being neutral/in cash): on the same day at the
closing value or the next day at the opening value. Such considerations for sure have an
impact on the performance, but the overall result would probably persist. Also, transaction
costs generally diminish returns, but the trading rule does not generate too many signals.

Whenever it comes to the analysis of financial time series, consider using pandas. Almost any time series-related
problem can be tackled with this powerful library.

@author: User
"""

import numpy as np
import pandas as pd
import pandas.io.data as web

sp500 = web.DataReader('^GSPC', data_source='yahoo', start='1/1/2000', end='4/14/2014')
sp500.info()

sp500.index.values

sp500['Close'].plot(grid=True, figsize=(8, 5))

sp500['42d'] = np.round(pd.rolling_mean(sp500['Close'], window=42), 2)
sp500['252d'] = np.round(pd.rolling_mean(sp500['Close'], window=252), 2)

sp500[['Close', '42d', '252d']].plot(grid=True, figsize=(8, 5))

sp500['42-252'] = sp500['42d'] - sp500['252d']
sp500['42-252'].tail()
sp500[['Close', '42d', '252d', '42-252']].plot(grid=True, figsize=(8, 5))

SD = 50
sp500['Regime'] = np.where(sp500['42-252'] > SD, 1, 0)
sp500['Regime'] = np.where(sp500['42-252'] < -SD, -1, sp500['Regime'])
sp500['Regime'].value_counts()
sp500['Regime_100'] = sp500['Regime']*100

sp500[['Close', '42d', '252d', '42-252','Regime_100']].plot(grid=True, figsize=(12, 8))

sp500['Market'] = np.log(sp500['Close'] / sp500['Close'].shift(1))
sp500['Strategy'] = sp500['Regime'].shift(1) * sp500['Market']
sp500[['Market', 'Strategy']].cumsum().apply(np.exp).plot(grid=True,figsize=(8, 5))