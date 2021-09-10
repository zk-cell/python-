#设置坐标轴 axis
import matplotlib.pyplot as  plt
import numpy as np

x = np.linspace(-3,3,50)
y1 = 2*x + 1
y2 = x**2

plt.figure(1,figsize = (8,5))
plt.plot(x,y1)
plt.figure(2,figsize = (9,6))
plt.plot(x,y2,color = 'red', linewidth = 1.0, linestyle = '--')
plt.plot(x,y1)

#限制坐标轴显示范围及设置标签
plt.xlim(-1,2)
plt.ylim(-2,5)
plt.xlabel('I am x')
plt.ylabel('I am y')

#修改坐标轴文字描述
new_ticks = np.linspace(-1,2,5)
print(new_ticks)
plt.xticks(new_ticks)
#  $  $为latex语法，    显示中文需要设置fontpropertites
plt.yticks([-2,-1.8,-1,1.22,3,],[r'$really\ bad\ \beta$',r'$bad\ \alpha$','普通',r'$good$',r'$really\ good$'],fontproperties = 'FangSong')

#移动坐标轴
# gca  = 'get current axis'
ax = plt.gca()
# spines.set_color设置边线颜色
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('white')
#设置底部为x轴，左边为y轴
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
#spines.set_position设置边线位置      参数有data,outward,axes等
ax.spines['bottom'].set_position(('data',-1))   #x轴对应的是y轴的-1处，即'普通'
# ax.spines['left'].set_position(('data',-1))      #y轴对应x轴的0点

plt.show()

