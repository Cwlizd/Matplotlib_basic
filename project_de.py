import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

url = "http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

col_name = ["sepal length", "sepal width",
            "petal length", "petal width", "class"]

df = pd.read_csv(url, names=col_name, header=None)

a = df["sepal length"]
b = df["sepal width"]
c = df["petal length"]
d = df["petal width"]

e_freq = df.groupby(["class"]).count()
e = e_freq["sepal length"]
print(e)

fig = plt.figure(figsize=(8, 9))
fig.subplots_adjust(wspace=0.7, hspace=0.5)
for i in range(1, 7):
    ax = fig.add_subplot(2, 3, i)
    if i == 1:
        ax.set_title("sepal length")
        ax.hist(a)
    elif i == 2:
        ax.set_title("sepal width")
        ax.hist(b)
    elif i == 3:
        ax.set_title("petal length")
        ax.hist(c)
    elif i == 4:
        ax.set_title("petal width")
        ax.hist(d)
    elif i == 6:
        ax.set_title("class")
        label = ["Iris-setosa", "Iris-versicolor", "Iris-virginica"]
        ax.pie(e, labels=label, autopct="%.2f%%")

fig.savefig("plot.png", dpi=fig.dpi)
plt.show()
