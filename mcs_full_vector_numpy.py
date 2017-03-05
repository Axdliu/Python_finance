# -*- coding: utf-8 -*-
"""
Created on Sun Mar 05 10:11:09 2017

@author: User
"""

#
#Monte Carlo valuation of European call options with NumPy (log version)
# mcs_full_vector_numpy.py
#

import math
from numpy import *
from time import time
import matplotlib.pyplot as plt

# star import for shorter code
random.seed(20000)
t0 = time()
# Parameters
S0 = 100.; K = 105.; T = 1.0; r = 0.05; sigma = 0.2
M = 50; dt = T / M; I = 250000

# Simulating I paths with M time steps
S = S0 * exp(cumsum((r - 0.5 * sigma ** 2) * dt
+ sigma * math.sqrt(dt)
* random.standard_normal((M + 1, I)), axis=0))

# sum instead of cumsum would also do
# if only the final values are of interest
S[0] = S0
# Calculating the Monte Carlo estimator
C0 = math.exp(-r * T) * sum(maximum(S[-1] - K, 0)) / I
# Results output
tnp2 = time() - t0
print 'European Option Value %7.3f' % C0
print 'Duration in Seconds %7.3f' % tnp2

plt.plot(S[:, :10])
plt.grid(True)
plt.xlabel('time step')
plt.ylabel('index level')

plt.hist(S[-1], bins=200)
plt.grid(True)
plt.xlim(0,200)
plt.xlabel('index level')
plt.ylabel('frequency')

plt.hist(np.maximum(S[-1] - K, 0), bins=200)
plt.grid(True)
plt.xlabel('option inner value')
plt.xlim(0,100)
plt.ylabel('requency')
plt.ylim(0, 50000)

print sum(S[-1] < K)