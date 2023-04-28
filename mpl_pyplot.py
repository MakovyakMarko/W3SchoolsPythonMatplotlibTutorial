# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 17:59:40 2023

@author: Marko
"""

import matplotlib.pyplot as plt
import numpy as np
# проведіть лінію на схемі від позиції
# (0,0) до позиції (6,250)
xpoints = np.array([0,6])
ypoints = np.array([0,250])
plt.plot(xpoints, ypoints)
plt.show()
