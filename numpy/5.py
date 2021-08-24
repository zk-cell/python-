#索引
import numpy as np

#可当作列表来对array索引
a = np.arange(3,15).reshape((3,4))
print(a)
#二维数组两种索引方式
# print(a[0][1])
# print(a[0,1])

#  :表示所有行/列  
# print(a[1,:])
# print(a[:,1])
# print(a[:2,2])

#打印每一行
# for row in a:
    # print(row)

#打印每一列
# for column in a.T:
#     print(column)

#将a转换成一行,再迭代出所有元素   flatten:转换成数组,flat:返回一个可迭代对象
print(a.flatten())
for item in a.flat:
    print(item,end=' ')