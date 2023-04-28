# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 17:27:49 2023

@author: Marko
"""

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35,25,25,15])
plt.pie(y)
plt.show()
# за замовчуванням креслення першого клину починається 
# від осі x і рухається проти годинникової стрілки
# додайте мітки до секторної діаграми з label параметром
# параметр label має бути масивом з однією міткою для кожного клина
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
plt.pie(y, labels = mylabels)
plt.show()
# за допомогою startangle можна змінити початковий кут
plt.pie(y, labels = mylabels, startangle = 90)
plt.show()
# explode виділяє клин. Параметр explode, якщо вказано, має
# бути масивом з одним значенням для кожного клина. Кожне
# значення відображає, наскільки далеко від центру відображається кожен клин
myexplode = [0.2,0,0,0]
plt.pie(y, labels = mylabels, explode = myexplode)
plt.show()
# доадйте тінь до кругової діаграми, встановивши shadow = True
plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)
plt.show()
# ви можете встановити кольори для кожного клина за допомогою
# сolors параметра. Параметр має бути масивом, з одним значенням 
# для кожного елемента клина
mycolors = ["k", "b", "red", "#4caf50"]
plt.pie(y, labels = mylabels, colors = mycolors)
plt.show()
# щоб додати список пояснень для кожного клина
# скористайтесь функцією legend()
plt.pie(y, labels = mylabels)
plt.legend()
plt.show()
# щоб доадти до пояснення заголовок додайте title параметр до legend
plt.pie(y, labels = mylabels)
plt.legend(title = "Four Fruits:")
plt.show()
