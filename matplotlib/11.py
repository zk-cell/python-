# 3D plot
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D    #matplotlib的3D模块

fig = plt.figure()
ax = Axes3D(fig)
# X,Y value
X = np.arange(-4,4,0.25)
Y = np.arange(-4,4,0.25)
X,Y = np.meshgrid(X,Y)
R = np.sqrt(X ** 2 + Y ** 2)
#height value
Z = np.sin(R)

# plot_surface：画3D图    edgecolor:线条颜色  rstride,cstride:行/列 跨度
ax.plot_surface(X,Y,Z,rstride = 1, cstride = 1, cmap = 'rainbow',edgecolor = 'black',linewidth = 0.5)

# contourf/contour  画3D等高线    zdir:沿哪个轴投影   offset:将图形压到特定值上（配合set_zlim3d调整等高线图的位置）
ax.contourf(X,Y,Z,zdir = 'z',offset = -2, cmap = 'rainbow')
ax.contourf(X,Y,Z,zdir = 'x',offset = -4, cmap = 'hot')

ax.set_xlim3d(-4,4)
ax.set_zlim3d(-2,2)

plt.show()