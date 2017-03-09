# -*- coding: utf-8 -*-
"""
Created on Wed Mar 08 23:01:52 2017
Financial plots

@author: User
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.finance as mpf

start = (2014, 5, 1)
end = (2014, 6, 30)

'''
Nowadays, a couple of Python libraries provide convenience functions to retrieve data from Yahoo! Finance. Be
aware that, although this is a convenient way to visualize financial data sets, the data quality is not sufficient to
base any important investment decision on it. For example, stock splits, leading to “price drops,” are often not
correctly accounted for in the data provided by Yahoo! Finance. This holds true for a number of other freely
available data sources as well.
'''
quotes = mpf.quotes_historical_yahoo_ochl('^GDAXI', start, end)
quotes[:2]

fig, ax = plt.subplots(figsize=(8, 5))
fig.subplots_adjust(bottom=0.2)
mpf.candlestick_ochl(ax, quotes, width=0.6, colorup='b', colordown='r')
plt.grid(True)
ax.xaxis_date()
# dates on the x-axis
ax.autoscale_view()
plt.setp(plt.gca().get_xticklabels(), rotation=30)

fig, ax = plt.subplots(figsize=(8, 5))
mpf.plot_day_summary2_ochl(ax, quotes, ticksize=4, colorup='k', colordown='r')
plt.grid(True)
ax.xaxis_date()
plt.title('DAX Index')
plt.ylabel('index level')
plt.setp(plt.gca().get_xticklabels(), rotation=30)


quotes = np.array(mpf.quotes_historical_yahoo_ochl('YHOO', start, end))
fig, (ax1, ax2) = plt.subplots(2, sharex=True, figsize=(8, 6))
mpf.candlestick_ochl(ax1, quotes, width=0.6, colorup='b', colordown='r')
ax1.set_title('Yahoo Inc.')
ax1.set_ylabel('index level')
ax1.grid(True)
ax1.xaxis_date()
plt.bar(quotes[:, 0] - 0.25, quotes[:, 5], width=0.5)
ax2.set_ylabel('volume')
ax2.grid(True)
ax2.autoscale_view()
plt.setp(plt.gca().get_xticklabels(), rotation=30)


