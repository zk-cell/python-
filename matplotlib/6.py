#tick
import matplotlib.pyplot as  plt
import numpy as np

x = np.linspace(-3,3,50)
y = 0.1*x

plt.figure(1,figsize = (8,5))
# zorder图层
plt.plot(x,y,linewidth = 10, zorder = 1)
plt.ylim(-2,2)

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('white')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data',0))   
ax.spines['left'].set_position(('data',0))   

for label in ax.get_xticklabels()+ax.get_yticklabels():
    label.set_fontsize(12)
    label.set_bbox(dict(facecolor = 'white', edgecolor = 'None', alpha = 0.7))
    label.set_zorder(2)
plt.show()