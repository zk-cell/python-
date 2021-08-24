#分割array              参数axis = (1:行运算/0:列运算)
import numpy as np

a = np.arange(16).reshape(4,4)
print(a)

# #等块分割 np.split(数组,块数,方向)
# #按行分割(横着)  两种方法
print('横着分：方法一', np.split(a,2,axis = 0))
print('横着分：方法二', np.vsplit(a,2))
# #按列分割(竖着)  两种方法
print('竖着分：方法一', np.split(a,2,axis = 1))
print('竖着分，方法二', np.hsplit(a,2))

# #不等块分割 np.array_split()
# a = np.arange(12).reshape(3,4)
# print(a)
# #3行分成两块
# print(np.array_split(a,2,axis = 0))
