# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 01:17:30 2017

@author: User
"""

import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt

#  the rand function returns random numbers from the open interval [0,1) 
npr.rand(10)
npr.rand(5, 5)
a = 5.
b = 10.
npr.rand(10) * (b - a) + a
npr.rand(5, 5) * (b - a) + a

sample_size = 500
rn1 = npr.rand(sample_size, 3)
rn2 = npr.randint(0, 10, sample_size)
rn3 = npr.sample(size=sample_size)
a = [0, 25, 50, 75, 100]
rn4 = npr.choice(a, size=sample_size)

