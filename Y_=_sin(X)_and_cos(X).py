import numpy as np
import matplotlib.pyplot as plt

# 描画範囲の指定
# x = np.arange(x軸の最小値, x軸の最大値, 刻み)
x = np.arange(-12, 12, 0.1)

# 計算式
y1 = np.sin(x)
y2 = np.cos(x)

# 横軸の変数。縦軸の変数。
plt.plot(x, y1, label="sin") # y1グラフに、ラベル「sin」付与。
plt.plot(x, y2, linestyle="--", label="cos") # y2グラフに、ラベル「cos」付与。linestyleで線のスタイルを指定。
plt.xlabel("x-axis") 
plt.ylabel("y-axis")
plt.title('Title: sin & cos')
plt.legend()

# 補助線
plt.hlines(0, -12, 12, colors='r', linewidths=2)
plt.vlines(0, -2, 2, colors='r', linewidths=2)

# 描画実行
plt.xlim([-2,2])
plt.ylim([-2,2])
plt.grid(True)
plt.savefig(r'.\plot.png')
plt.show()