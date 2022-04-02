import numpy as np
import matplotlib.pyplot as plt

data = [20, 20, 10, 50]
labels = ["apple", "guava", "strawberry", "banana"]
plt.pie(data, labels=labels, autopct="%.2f%%")
plt.show()
