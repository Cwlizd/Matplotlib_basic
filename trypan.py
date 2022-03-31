import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, np.pi*2)
y1 = np.sin(x)
y2 = np.cos(x)
y6 = np.tan(x)


fig = plt.figure(figsize=(8, 6))
fig.subplots_adjust(wspace=0.5, hspace=0.5)
for i in range(6):
    ax = fig.add_subplot(2, 3, i+1)
    ax.set_xlim(0, 7)
    ax.set_ylim(-2, 2)
    ax.set_xlabel("x-axis")
    ax.set_ylabel("y-axis")
    ax.grid(True)
    ax.set_xticks([0, np.pi*0.5, np.pi, np.pi*1.5, np.pi*2])
    ax.set_xticklabels(["0°", "90°", "180°", "270°", "360°"])

    if i == 0:
        ax.plot(x, y1, c="r")
        ax.set_title("y=sin(x)")
    elif i == 1:
        ax.plot(x, y2, c="g")
        ax.set_title("y=cos(x)")
    elif i == 5:
        ax.plot(x, y6, c="b")
        ax.set_title("y=tan(x)")
plt.show()
