# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 12:07:55 2023

@author: Marko
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,290,300,310,320,330])

plt.plot(x,y)
# підписати осі
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
# створити заголовок для графіку
plt.title("Sports Watch Data")
plt.show()

# встановлення шрифту для заголовка та міток

font1 = {'family' : 'serif', 'color' : 'blue', 'size' : 20}
font2 = {'family' : 'serif', 'color' : 'darkred', 'size' : 15}

plt.title("Sports Watch Data", fontdict = font1)
plt.xlabel("Average Pulse", fontdict = font2)
plt.ylabel("Calorie Burnage", fontdict = font2)

plt.plot(x,y)
plt.show()

# loc параметр для розміщення заголовка (right,left,center(def))

plt.title("Sports Watch Data", loc = 'left')
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x,y)
plt.show()
