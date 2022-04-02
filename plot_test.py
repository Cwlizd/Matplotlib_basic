from matplotlib import markers
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, np.pi*2, 20)
y = np.sin(x)

plt.plot(x, y, "--gs", markerfacecolor="r", linewidth="3")
plt.show()
