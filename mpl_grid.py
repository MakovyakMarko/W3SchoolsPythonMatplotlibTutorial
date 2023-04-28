# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 12:32:49 2023

@author: Marko
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,290,300,310,320,330])


font1 = {'family':'serif', 'color':"blue", 'size': 20}
font2 = {'family':'serif', 'color':'darkred', 'size': 15}

plt.title("Sports Watch Data", fontdict = font1)
plt.xlabel("Average Pulse", fontdict = font2)
plt.ylabel("Calorie Burnage", fontdict = font2)

plt.plot(x,y, linestyle = 'dotted', marker = "*", ms = 15, mec ='y', mfc = 'b')

plt.grid()

plt.show()
# укажіть як лінії сітки відображати axis (x або у)
font1 = {'family':'serif', 'color':"blue", 'size': 20}
font2 = {'family':'serif', 'color':'darkred', 'size': 15}

plt.title("Sports Watch Data", fontdict = font1)
plt.xlabel("Average Pulse", fontdict = font2)
plt.ylabel("Calorie Burnage", fontdict = font2)

plt.plot(x,y, linestyle = 'dotted', marker = "*", ms = 15, mec ='b', mfc = 'y')

plt.grid(axis= 'x')

plt.show()
# axis = 'y'
font1 = {'family':'serif', 'color':"blue", 'size': 20}
font2 = {'family':'serif', 'color':'darkred', 'size': 15}

plt.title("Sports Watch Data", fontdict = font1)
plt.xlabel("Average Pulse", fontdict = font2)
plt.ylabel("Calorie Burnage", fontdict = font2)

plt.plot(x,y, linestyle = 'dotted', marker = "*", ms = 15, mec ='y', mfc = 'b')

plt.grid(axis= 'y')

plt.show()
# встановіть властивості сітки {color='color',linestyle='--', linewidth=0.5}
font1 = {'family':'serif', 'color':"blue", 'size': 20}
font2 = {'family':'serif', 'color':'darkred', 'size': 15}

plt.title("Sports Watch Data", fontdict = font1)
plt.xlabel("Average Pulse", fontdict = font2)
plt.ylabel("Calorie Burnage", fontdict = font2)

plt.plot(x,y, linestyle = 'dotted', marker = "*", ms = 15, mec ='y', mfc = 'b')

plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)

plt.show()
