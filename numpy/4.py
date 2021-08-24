#基础运算(part2)      参数axis = (1:行运算/0:列运算)
import numpy as np

a = np.arange(2,14).reshape((3,4))
print(a)
#返回最值/平均值/中位数索引
# print('index of min number is = ',np.argmin(a))
# print('index of max number is =',np.argmax(a))
# print('mean of numbers in array is = ',np.mean(a),'or using np.average:', np.average(a))
# print('median of numbers in array is =', np.median(a))

#一个个累加  np.cumsum()
# print(np.cumsum(a))

#相邻数之差  np.diff()
# print(np.diff(a))

#非零数索引   np.nonzero(a)  第一个数组:行数,第二个数组:每一行的索引
# print(np.nonzero(a))

#给矩阵逐行排序   np.sort(a)
# a = np.arange(14,2,-1).reshape((3,4))
# print(a)
# print(np.sort(a))

#矩阵的转置  np.transpose(array)   /   array.T
# print(np.transpose(a))
at = a.T
# print(at)
# print(np.dot(a,at))

#clip
a = np.arange(2,14).reshape((3,4))
print(np.clip(a,5,10))