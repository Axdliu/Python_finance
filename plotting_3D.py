# -*- coding: utf-8 -*-
"""
Created on Wed Mar 08 23:35:26 2017
3D Plotting

@author: User
"""

import numpy as np
import matplotlib.pyplot as plt

strike = np.linspace(50, 150, 24)
ttm = np.linspace(0.5, 2.5, 24)
strike, ttm = np.meshgrid(strike, ttm)

# generate fake implied volatilities
iv = (strike - 100) ** 2 / (100 * strike) / ttm

from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure(figsize=(9, 6))
ax = fig.gca(projection='3d')
surf = ax.plot_surface(strike, ttm, iv, rstride=2, cstride=2,
cmap=plt.cm.coolwarm, linewidth=0.5,
antialiased=True)
ax.set_xlabel('strike')
ax.set_ylabel('time-to-maturity')
ax.set_zlabel('implied volatility')
fig.colorbar(surf, shrink=0.5, aspect=5)

