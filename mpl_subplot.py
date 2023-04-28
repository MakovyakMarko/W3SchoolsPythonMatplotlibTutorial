# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 13:13:26 2023

@author: Marko
"""
# за допомогою subplot() функції можна малювати кілька
# графіків на одній фігурі:
import matplotlib.pyplot as plt
import numpy as np

# plot 1
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])
plt.subplot(1,2,1)
plt.plot(x,y)

# plot 2
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])
plt.subplot(1, 2, 2)
plt.plot(x,y)

plt.show()

# функція subplot() приймає три аргументи, які описують компонування фігури
# Макет складається з рядків і стовпців, які представлені першим і другим аргументом
# Третій аргумент представляє індекс поточного графіка
# plt.subplot(1,2,1) 1row, 2 colums, this plot is the first plot

# plot 1
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])
plt.subplot(2,1,1)
plt.plot(x,y)

# plot 2
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])
plt.subplot(2, 1, 2)
plt.plot(x,y)

plt.show()

# можна намалювати скільки завгодно графіків на одній фігурі
# просто опишіть кількість рядків, стовпців та індекс ділянки
# plot 1
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])
plt.subplot(2,3,1)
plt.plot(x,y)

# plot 2
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])
plt.subplot(2, 3, 2)
plt.plot(x,y)

# plot 3
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])
plt.subplot(2,3,3)
plt.plot(x,y)

# plot 4
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])
plt.subplot(2, 3, 4)
plt.plot(x,y)

# plot 5
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])
plt.subplot(2,3,5)
plt.plot(x,y)

# plot 6
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])
plt.subplot(2, 3, 6)
plt.plot(x,y)

plt.show()

# plot 1 title
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])
plt.subplot(1,2,1)
plt.plot(x,y)
plt.title("Sales")

# plot 2 title
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])
plt.subplot(1, 2, 2)
plt.plot(x,y)
plt.title("Income")

plt.show()

# figure suptitle
# plot 1 tille
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])
plt.subplot(1,2,1)
plt.plot(x,y)
plt.title("Sales")

# plot 2 title
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])
plt.subplot(1, 2, 2)
plt.plot(x,y)
plt.title("Income")

plt.suptitle("My Shop")
plt.show()
