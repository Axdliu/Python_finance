# -*- coding: utf-8 -*-
"""
Created on Sun Mar 05 16:42:59 2017

test some useful string functions

@author: User
"""

t = 'this is a string object'

print t.capitalize()
print t.split()
print t.find('string')
print t[t.find('string')]
print t.replace(' ', '|')       

print 'http://www.python.org'.strip('htp:/')
print t.count('s')

