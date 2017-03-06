# -*- coding: utf-8 -*-
"""
Created on Sun Mar 05 18:40:11 2017

@author: User
"""

t = 1, 2.5, 'data'
l = list(t)
l.append([4, 3])
l.extend([1.0, 1.5, 2.0])
l.insert(1, 'insert')
l.remove('data')
p = l.pop(3)
print l, p

# selected operations and methods of dict objects
dict_1 = {1:1, 2:2, 3:3}
print dict_1
del dict_1[2]
print dict_1
print dict_1.has_key(2)
print dict_1.has_key(1)
content = dict_1.items()
print content
dict_1.popitem()

# set
s = set(['u', 'd', 'ud', 'du', 'd', 'du'])
t = set(['d', 'dd', 'uu', 'u'])
print s.union(t)
print s.intersection(t)
print s.difference(t) 
print t.difference(s)
print s.symmetric_difference(t)

from random import randint
l = [randint(0, 10) for i in range(1000)]
print set(l)
