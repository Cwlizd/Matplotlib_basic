import numpy as np
import matplotlib.pyplot as plt

data = [20, 20, 10, 50]
labels = ["apple", "guava", "strawberry", "banana"]
explode = [0, 0, 0.2, 0]
plt.pie(data, labels=labels, autopct="%.2f%%", explode=explode, shadow=True)
plt.show()
