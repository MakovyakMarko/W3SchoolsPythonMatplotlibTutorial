# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 16:25:17 2023

@author: Marko
"""

# за допомогою pyplot ви можете використовувати bar() функцію для малювання гістрограм
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A","B","C","D"])
y = np.array([3,8,1,10])

plt.bar(x,y)
plt.show()

# якщо ви хочете, щоб смужки відображалися горизонтально, скористайтесь функцією barh()

plt.barh(x, y)
plt.show()

# bar() i barh() приймає ключове слово color, щоб встановити колір смуг

plt.bar(x,y,color = "red")
plt.show()

# для встановлення ширини смужок bar() приймає аргумент width
plt.bar(x,y, width=0.3)
plt.show()

# для горизонтальних смуг використовуйте height замість width
plt.barh(x,y,height=0.3)
plt.show()

# стандартна ширина 0.8, стандартна висота 0.8