#array合并
import numpy as np

a = np.array([1,1,1])
b = np.array([2,2,2])

# # 纵向合并  vstack(tuple):   vertical stack
c = np.vstack((a,b))
# #横向合并   hstack
d = np.hstack((a,b))
# print(c.shape)
# print(d.shape)

#行向量无法通过 .T/.transpose 转换成列向量
# print(a.T.shape)
#因此使用如下方法:       newaxis = None,即一行或一列,:为所有元素
e = a[np.newaxis,:]     #变成行向量
f = a[:,np.newaxis]     #变成列向量
# print(e,e.shape)
# print(f,f.shape)

'''小结:
array[np.newaxis,:]   将array变成行向量
array[:,np.newaxis]   将array变成列向量
'''

#concatenate(tuple,axis:控制方向):多个array合并,各array维度必须相同 
a = np.array([1,1,1])[np.newaxis,:]  
b = np.array([2,2,2])[np.newaxis,:]  
g = np.concatenate((a,b,b,a),axis = 0)      #归为一列
print('axis = 0,\ng = \n', g)

g = np.concatenate((a,b,b,a),axis = 1)      #归为一行
print('axis = 1,\ng = \n', g)