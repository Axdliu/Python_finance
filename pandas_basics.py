# -*- coding: utf-8 -*-
"""
Created on Wed Mar 08 23:39:26 2017

@author: User
"""

import numpy as np
import pandas as pd

df = pd.DataFrame([10, 20, 30, 40], columns=['numbers'],\
                  index=['a', 'b', 'c', 'd'])
print df.index
print df.columns
print df.ix['c']
print df.ix[['a','d']]
print df.ix[df.index[1:3]]
print df.sum()
print df.apply(lambda x: x ** 2)
df['floats'] = (1.5, 2.5, 3.5, 4.5)
df['names'] = pd.DataFrame(['Yves', 'Guido', 'Felix', 'Francesc'],\
                            index=['d', 'a', 'b', 'c'])
df = df.append(pd.DataFrame({'numbers': 100, 'floats': 5.75,\
                             'names': 'Henry'}, index=['z',]))
df.join(pd.DataFrame([1, 4, 9, 16, 25], \
                     index=['a', 'b', 'c', 'd', 'y'], \
                        columns=['squares',]))
df = df.join(pd.DataFrame([1, 4, 9, 16, 25],\
                          index=['a', 'b', 'c', 'd', 'y'],\
                            columns=['squares',]),\
                            how='outer')
print df
print df[['numbers', 'squares']].mean()
print df[['numbers', 'squares']].std()
