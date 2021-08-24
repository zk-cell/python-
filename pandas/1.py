#numpy提供数据,pandas提供索引
import pandas as pd
import numpy as np
'''
Pandas Series 类似表格中的一个列（column），类似于一维数组，可以保存任何数据类型。
Series 由索引（index）和列组成，函数如下：

    pandas.Series( data, index, dtype, name, copy)

    data：一组数据(ndarray 类型)。

    index：数据索引标签，如果不指定，默认从 0 开始。

    dtype：数据类型，默认会自己判断。

    name：设置名称。

    copy：拷贝数据，默认为 False。
'''

#np.nan = None
s = pd.Series([1,3,6,np.nan],index = ['a','b','c','d'])
print(s)



'''
DataFrame 是一个表格型的数据结构，它含有一组有序的列，每列可以是不同的值类型（数值、字符串、布尔型值）。
DataFrame 既有行索引也有列索引，它可以被看做由 Series 组成的字典（共同用一个索引）。

    pandas.DataFrame( data, index, columns, dtype, copy)

参数说明：

    data：一组数据(ndarray、series, map, lists, dict 等类型)。

    index：索引值，或者可以称为行标签。

    columns：列标签，默认为 RangeIndex (0, 1, 2, …, n) 。

    dtype：数据类型。

    copy：拷贝数据，默认为 False。

Pandas DataFrame 是一个二维的数组结构，类似二维数组。
'''

#无索引
df1 = pd.DataFrame(np.arange(12).reshape((3,4)))
# print(df1)

#直接加上索引
dates = pd.date_range('20210823',periods = 10)  #生成索引数对应下面randn的行
# print(dates)
#np.random.randn:随机生成一个数组    index:行标签,columns:列标签
df2= pd.DataFrame(np.random.randn(10,4),index = dates, columns = ['a','b','c','d'])
# print(df2)

#用字典的键充当列标签
df2 = pd.DataFrame(
    {
        'A':1.0, 
        'B':pd.Timestamp('20130102'), 
        'C':pd.Series(1,index = list(range(4)), dtype ='float32'),
        'D':np.array([3]*4,dtype='int32'),
        'E':pd.Categorical(["test","tranin","test","train"]),
        'F':'foo',

    })
# print(df2)
#每一个键对应值的数据类型
# print(df2.dtypes)
#行标签
# print(df2.index)
#列标签
# print(df2.columns)
#所有的值
# print(df2.values)
#描述数字型数据的个数,平均值,方差等等统计学数据,好用!!!!
# print(df2.describe())
#把dataframe看作一个矩阵,转置
# print(df2.T)
#按index排序        axis : 0->index,1->column; ascending:正序,descending:倒序
# print(df2.sort_index(axis = 1, ascending = False))
# print(df2.sort_index(axis = 0, ascending = False))
#按values排序      by = index or columns
# print(df2.sort_values(by = 'A'))

