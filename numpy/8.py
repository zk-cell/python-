#赋值与copy
import numpy as np

a = np.arange(4)

#复制a(a变 bc也变)
# b = a
# c = a
# a[0] = 11
# print(a,b,c)
# print(b is a,c is a)

# copy(a变，b不变)
b = a.copy()
a[0] = 11
print(a,b,a is b)

