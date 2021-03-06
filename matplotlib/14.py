# 图中图
import matplotlib.pyplot as plt

fig = plt.figure()
x = [1,2,3,4,5,6,7]
y = [1,3,4,2,5,8,6]

#相对figure四条边界的百分比
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
ax1 = fig.add_axes([left, bottom, width, height]) 
ax1.plot(x,y,'r')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('title')

# method1
left, bottom, width, height = 0.2, 0.6, 0.25, 0.25
ax2 = fig.add_axes([left, bottom, width, height]) 
#x、y数据可以反过来
ax2.plot(y,x,'r')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('the inside 1')

# method2
plt.axes([0.6,0.2,0.25,0.25])
#把y的数据倒过来
plt.plot(y[::-1],x,'g')
plt.xlabel('x')
plt.ylabel('y')
plt.title('the inside 2')

plt.show()