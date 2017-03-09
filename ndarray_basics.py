# -*- coding: utf-8 -*-
"""
Created on Sun Mar 05 23:05:46 2017

@author: User
"""

from copy import deepcopy

v = [0.5, 0.75, 1.0, 1.5, 2.0]
m = [v, v, v]
n = 3 * [deepcopy(v), ]
print m
print n

v[0] = 'Python'
print m
print n

import numpy as np

a = np.array([0, 0.5, 1.0, 1.5, 2.0])
type(a)

print a[:2]
print a.sum()
print a.std()
print a.cumsum()
print a*2
b = np.array([a, a*2])
print b
print b.sum()
print b.sum(axis=0)
print b.sum(axis=1)
c = np.zeros((2,3,4))
print c


import random
I = 5000
%time mat = [[random.gauss(0, 1) for j in range(I)] for i in range(I)]
%time reduce(lambda x, y: x + y, \
     [reduce(lambda x, y: x + y, row) \
              for row in mat])

%time mat = np.random.standard_normal((I, I))
%time mat.sum()

dt = np.dtype([('Name', 'S10'), ('Age', 'i4'), \
               ('Height', 'f'), ('Children/Pets', 'i4', 2)])
s = np.array([('Smith', 45, 1.83, (0, 1)), \
              ('Jones', 53, 1.72, (2, 2))], dtype=dt)
print s


x = np.random.standard_normal((5, 10000000))
y = 2 * x + 3 # linear equation y = a * x + b
C = np.array((x, y), order='C')
F = np.array((x, y), order='F')
x = 0.0; y = 0.0 # memory cleanup
