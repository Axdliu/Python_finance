# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 00:23:41 2017
Wtiting and Reading Numpy Arrays

@author: User
"""

import numpy as np

dtimes = np.arange('2015-01-01 10:00:00', '2021-12-31 22:00:00',\
                   dtype='datetime64[m]') # minute intervals

dty = np.dtype([('Date', 'datetime64[m]'), ('No1', 'f'), ('No2', 'f')])
data = np.zeros(len(dtimes), dtype=dty) 
data['Date'] = dtimes                  
a = np.random.standard_normal((len(dtimes), 2)).round(5)
data['No1’] = a[:, 0]
data['No2’] = a[:, 1]