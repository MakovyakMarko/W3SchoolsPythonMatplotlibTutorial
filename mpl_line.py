# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 11:18:00 2023

@author: Marko
"""

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3,8,1,10])

plt.plot(ypoints, linestyle = 'dotted')
plt.show()

plt.plot(ypoints, linestyle = 'dashed')
plt.show()

plt.plot(ypoints, linestyle = 'solid')
plt.show()

plt.plot(ypoints, linestyle = 'dashdot')
plt.show()

plt.plot(ypoints, linestyle = 'None')
plt.show()

# color = c
plt.plot(ypoints, color = 'r')
plt.show()
#linewidth = lw, значення з плаваючим числом у пунктах
plt.plot(ypoints, linewidth = '20.5')
plt.show()
# ви можете накреслити скільки завгодно ліній просто
# додавши більше plt.plot() функцій
y1 = np.array([3,8,1,10])
y2 = np.array([6,2,7,11])

plt.plot(y1)
plt.plot(y2)

plt.show()
# також можна намалювати багато ліній додавши точки х і у 
# для кожної лінії на одній plt.plot() функції
x1 = np.array([0,1,2,3])
y1 = np.array([3,8,1,10])
x2 = np.array([0,1,2,3])
y2 = np.array([6,2,7,11])

plt.plot(x1, y1, x2, y2)
plt.show()