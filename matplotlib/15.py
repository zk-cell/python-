# 主次坐标轴
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,10,0.1)
y1 = 0.05 * x**2
y2 = -1 * y1

fg,ax1 = plt.subplots()
#把ax1的数据沿着x轴方向镜像对称过来
ax2 = ax1.twinx()
ax1.plot(x,y1,'g-')
ax2.plot(x,y2,'b--')

ax1.set_xlabel('X data')
ax1.set_ylabel('Y1',color = 'g')
ax2.set_ylabel('Y2',color = 'b')

plt.show()