import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 11)
x1 = ["Taiwan", "Japan", "France", "Australia",
      "Hongkong", "American", "Canada", "Mexico", "Brazil", "Germany"]
y1 = np.random.choice(range(1, 101), 10)
y2 = np.random.choice(range(1, 101), 10)
plt.bar(x1, y1)
plt.bar(x1, y2, bottom=y1)
plt.legend(("y1", "y2"))
plt.show()
