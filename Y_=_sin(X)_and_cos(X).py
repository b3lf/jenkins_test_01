import numpy as np
import matplotlib.pyplot as plt

# set the range
x = np.arange(-12, 12, 0.1)

# calculate
y1 = np.sin(x)
y2 = np.cos(x)

# set horizontal/vertical axises
plt.plot(x, y1, label="sin") # y1グラフに、ラベル「sin」付与。
plt.plot(x, y2, linestyle="--", label="cos") # y2グラフに、ラベル「cos」付与。linestyleで線のスタイルを指定。
plt.xlabel("x-axis") 
plt.ylabel("y-axis")
plt.title('Title: sin & cos')
plt.legend()

# set auxiliary line
plt.hlines(0, -12, 12, colors='r', linewidths=2)
plt.vlines(0, -2, 2, colors='r', linewidths=2)

# draw the graph
plt.xlim([-2,2])
plt.ylim([-2,2])
plt.grid(True)

# save as a png file
plt.savefig(r'.\plot.png')

# show the graph
# plt.show()
