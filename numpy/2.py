#创建array
import numpy as np

#dtype数据类型
a = np.array([2,3,4], dtype = int)
# print(a)

#二维数组(矩阵)
a = np.array(
    [
        [1,2,3],
        [4,5,6]
    ]
)
# print(a)

#生成0矩阵,np.zeros((row,column))
a = np.zeros((3,4))
# print(a)

#1矩阵
a = np.ones((3,4), dtype = np.int16)
# print(a)

#有序矩阵  np.arange(start,stop,step)
a = np.arange(10,20,2)
# print(a)
#重新定义矩阵形状
a = np.arange(12).reshape((3,4))
# print(a)

#生成等差数列
a = np.linspace(1,10,10,dtype=int)
# print(a)

#起始1,终止10,步长为6,定义为两行三列
a = np.linspace(1,6,6,dtype=int).reshape((2,3))
# print(a)




