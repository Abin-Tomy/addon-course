import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#plot
# x = np.linspace(0, 10, 100)
# y = np.sin(x)
# plt.plot(x, y, color='blue', linestyle='--', marker='o')
# plt.title("Line Plot")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.show()

#scaterplot
# x = np.random.rand(50)
# y = np.random.rand(50)
# plt.scatter(x, y, color='red', marker='*')
# plt.title("Scatter Plot")
# plt.show()

#bar chart
# categories = ['A', 'B', 'C']
# values = [3, 7, 5]
# plt.bar(categories, values, color=['red','green','blue'])
# plt.title("Bar Chart")
# plt.show()

#bar chart
# categories = ['A', 'B', 'C']
# values = [3, 7, 5]
# plt.barh(categories, values, color=['red','green','blue'])
# plt.title("horizontal Bar Chart")
# plt.show()

#histogram
# data = np.random.randn(1000)
# plt.hist(data, bins=30, color='blue', edgecolor='black')
# plt.title("Histogram")
# plt.show()

#pie chart
# sizes = [15, 30, 45, 10]
# labels = ['A', 'B', 'C', 'D']
# plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
# plt.title("Pie Chart")  
# plt.show()

#advanced Plotting Functions
# days = [1,2,3,4,5]
# sleeping = [7,8,6,11,7]
# eating = [2,3,4,3,2]
# working = [7,8,7,2,2]
# playing = [8,5,7,8,13]
# plt.stackplot(days, sleeping, eating, working, playing, labels=['sleep','eat','work','play'])
# plt.legend(loc='upper left')
# plt.title("Stack Plot")
# plt.show()

#box plot
data = np.random.normal(100, 20, 200)
plt.boxplot(data)
plt.title("Box Plot")   
plt.show()

