# scatter
import matplotlib.pyplot as plt
import numpy as np

n = 1024
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)
T = np.arctan2(Y,X) #for color value

plt.scatter(X,Y, s = 75, c = T, alpha = 0.5)

plt.xlim((-1.5,1.5))
plt.ylim((-1.5,1.5))
#隐藏坐标轴刻度
plt.xticks(())
plt.yticks(())

plt.show()