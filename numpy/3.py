#基础运算(part1)
import numpy as np
from numpy.lib.function_base import angle

a = np.array([10,20,30,40])
b = np.arange(4)
c = a+b
d = a-b
# print(a,b,c,d)

#显示b中小于3的数为哪些, 返回true/false
# print(b<3)

# **:将数组每一个数都平方
e = b**2
# print(b,e)

#sin(弧度)     1度 = 2*pi/360 = pi/180    1rad = 180/pi
angles = [30,45,60,90]
for i in angles:
    f = np.sin(i *  (np.pi/180))
    # print(f)
radians = [1/6,1/3,1/2]
for i in radians:
    g = np.sin(i * np.pi)
    # print(g)

#矩阵乘法    c = np.dot(a,b)或者c = a.dot(b)
a = np.array([10,20,30,40]).reshape((2,2))
b = np.arange(4).reshape((2,2))
c = np.dot(a,b)
# print(a,b,c,sep='\n,') # 或者 c = a.dot(b)

#再如
a = np.array([[1,2],[3,4]])
b = np.array([[11,12],[13,14]])
# print(a,b,np.dot(a,b),sep = '\n,')

#普通乘法(各元素相乘)
# print(a,b,a*b,sep = ',\n')

#生成随机矩阵     np.random.random(size = (row,column))  元素值0-1
a = np.random.random(size = (2,2))
print(a)

#求和,最值     np.sum(array)/.max/.min
# 针对某一行则加上 axis = (1:行/0:列)
print('按行求和sum = ',np.sum(a,axis = 1))
print('按列找最大值max=',np.max(a,axis = 0))
print('矩阵中的最小值=',np.min(a))