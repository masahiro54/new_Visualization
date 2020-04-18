import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 100, 10)
y = np.random.randn(10)

print(type(x))
print(type(y))
#線グラフの描画
#折れ線
#plt.plot(x, y, color=(0,0,1))
#plt.show()
##曲線(調査中)
#plt.plot(x, y, color=(0,0,1))
#plt.show()
##散布図
#plt.scatter(x, y, color=(0,0,1))
#plt.show()
##棒グラフ
#plt.bar(x, y, color=(0,0,1))
#plt.show()
##ヒストグラム
#x = np.random.normal(50, 10, 1000)
#plt.hist(x,bins=16)
#plt.show()