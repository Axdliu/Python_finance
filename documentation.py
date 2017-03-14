# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 22:44:21 2017

@author: User
"""

import numpy as np
from random import gauss
import matplotlib.pyplot as plt
import pandas as pd
import pickle


'''
documentation with pickle
'''

path = 'D:\\github\\finance\\Python_finance\\pickle\\'

a = [gauss(1.5, 2) for i in range(1000000)]

pkl_file = open(path + 'data.pkl', 'w')
pickle.dump(a, pkl_file)
print pkl_file
pkl_file.close()

pkl_file = open(path + 'data.pkl', 'r') # open file for reading
b = pickle.load(pkl_file)

# check if the two variables are exact the same
print np.allclose(np.array(a), np.array(b))
print np.sum(np.array(a)-np.array(b))

pkl_file = open(path + 'data.pkl', 'w') # open file for writing
pickle.dump(np.array(a), pkl_file)
pickle.dump(np.array(a) ** 2, pkl_file)
pkl_file.close()

pkl_file = open(path + 'data.pkl', 'r') # open file for reading
x = pickle.load(pkl_file)
y = pickle.load(pkl_file)

pkl_file = open(path + 'data.pkl', 'w')
pickle.dump({'x' : x, 'y' : y}, pkl_file)
pkl_file.close()

pkl_file = open(path + 'data.pkl', 'r') 
data = pickle.load(pkl_file)
pkl_file.close()
for key in data.keys():
    print key, data[key][:4]


'''
documentation with csv files
'''

rows = 5000
a = np.random.standard_normal((rows, 5))
a.round(4)
t = pd.date_range(start='2014/1/1', periods=rows, freq='H')
csv_file = open(path + 'data.csv', 'w') # open file for writing
header = 'date,no1,no2,no3,no4,no5\n'
csv_file.write(header)
for t_, (no1, no2, no3, no4, no5) in zip(t, a):
    s = '%s,%f,%f,%f,%f,%f\n' % (t_, no1, no2, no3, no4, no5)
    csv_file.write(s)
csv_file.close()

csv_file = open(path + 'data.csv', 'r') # open file for reading
for i in range(5):
    print csv_file.readline(),
csv_file.close()


'''
SQL Databases
'''

import sqlite3 as sq3
import datetime as dt

query = 'CREATE TABLE numbs (Date date, No1 real, No2 real)'
con = sq3.connect(path + 'numbs.db')
con.execute(query)
con.commit()

con.execute('INSERT INTO numbs VALUES(?, ?, ?)', \
            (dt.datetime.now(), 0.12, 7.3))
data = np.random.standard_normal((10000, 2)).round(5)

for row in data:
    con.execute('INSERT INTO numbs VALUES(?, ?, ?)', \
                (dt.datetime.now(), row[0], row[1]))
con.commit()
con.execute('SELECT * FROM numbs').fetchmany(10)

pointer = con.execute('SELECT * FROM numbs')
for i in range(3):
    print pointer.fetchone()
con.close()






