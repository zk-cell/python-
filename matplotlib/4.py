# legend
import matplotlib.pyplot as  plt
import numpy as np

x = np.linspace(-3,3,50)
y1 = 2*x + 1
y2 = x**2

plt.figure(1,figsize = (8,5))
#label 设置名字,再用plt.legend显示出来
plt.plot(x,y1)
plt.figure(2,figsize = (9,6))
# plt.plot返回只有一个元素的列表，l1,表示对列表解包
l1, = plt.plot(x,y2,color = 'red', linewidth = 1.0, linestyle = '--', label = 'up')
l2, = plt.plot(x,y1, label = 'down')
# legend参数 handle:控制线 labels:线的名字，会覆盖掉plot中的label loc：调整图例位置  best/    lower/higher + left+right等等
plt.legend(handles = [l1,l2,], labels = ['aaa','bbb'], loc = 'best' )

plt.xlim(-1,2)
plt.ylim(-2,5)
plt.xlabel('I am x')
plt.ylabel('I am y')

new_ticks = np.linspace(-1,2,5)
print(new_ticks)
plt.xticks(new_ticks)
plt.yticks([-2,-1.8,-1,1.22,3,],[r'$really\ bad\ \beta$',r'$bad\ \alpha$','普通',r'$good$',r'$really\ good$'],fontproperties = 'FangSong')



plt.show()