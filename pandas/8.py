#plot画图
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#np.random.randn:由正态分布随机生成一个数组      random.rand:由(0,1)的数随机生成
# data = pd.Series(np.random.randn(1000),index = np.arange(1000))
# data = data.cumsum()    #累加

#1000x4 二维数据,column为4个series的属性
data = pd.DataFrame(np.random.randn(1000,4), index = np.arange(1000),columns = list('ABCD'))
data = data.cumsum()
# print(data.head(3))              #打印前三个数据

# pd.df.plot()折线数据
'''
plot methods:
'bar','hist','box','kde','area','scatter','hexbin','pie'
'''
# data.plot()

# pd.df.scatter()散点数据     scatter只有x和y两种属性,因此使用plot.scatter(x = , y =)
ax = data.plot.scatter(x = 'A',y = 'B',color = 'DarkBlue',label = 'Class1')
#上面的数据附在下面 ax=ax(相当于让两张图显示在一起)
data.plot.scatter(x = 'A',y = 'C',color = 'DarkGreen',label = 'Class2',ax =ax)
#显示数据
plt.show()                      