# animation 动画    终端中运行可以动起来
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

fig,ax = plt.subplots()

x = np.arange(0, 2*np.pi, 0.01)
# plot返回列表，赋值为变量时加上，  即可返回第一个元素
line, = ax.plot(x,np.sin(x))
# print(isinstance(line,list))
# print(line)
# print(line[0])

# print(type(line,))
# print(line,)

# i:第i帧
def animate(i):
    #(随着x的增大),更新y的数据
    line.set_ydata(np.sin(x+i/100))
    return line,

def init():
    line.set_ydata(np.sin(x))
    return line,

#frames:帧数，即animate中的参数i,调用时自动传入 interval:更新频率   blit: true->更新变化的点，false->更新全部点
ani = animation.FuncAnimation(fig = fig, func= animate, frames = 100, init_func = init, interval = 10, blit = False)
plt.show()