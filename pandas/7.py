#merge合并
import pandas as pd
import numpy as np

'''
Merge DataFrame or named Series objects with a database-style join.
The join is done on columns or indexes. If joining columns on columns, 
the DataFrame indexes *will be ignored*. Otherwise if joining indexes 
on indexes or indexes on a column or columns, the index will be passed on.

Briefly Speaking:merging two DataFrame by key/keys.


'''
# left = pd.DataFrame(
#     {
#         'key':['k0','k1','k2','k3'],
#         'A':['A0','A1','A2','A3'],
#         'B':['B0','B1','B2','B3']
#     }
# )
# right = pd.DataFrame(
#     {
#         'key':['k0','k1','k2','k3'],
#         'C':['C0','C1','C2','C3'],
#         'D':['D0','D1','D2','D3']
#     }
# )
# print(left)
# print(right)
# result = pd.merge(left,right,on = 'key')
# print(result)

#how : {'left', 'right', 'outer', 'inner'}, default 'inner',inner:合并输出相同部分
left = pd.DataFrame(
    {
        'key1':['k0','k0','k1','k2'],
        'key2':['k0','k1','k0','k1'],
        'A':['A0','A1','A2','A3'],
        'B':['B0','B1','B2','B3']
    }
)
right = pd.DataFrame(
    {
        'key1':['k0','k1','k1','k2'],
        'key2':['k0','k0','k0','k0'],
        'C':['C0','C1','C2','C3'],
        'D':['D0','D1','D2','D3']
    }
)
# print(left)
# print(right)

#inner
# result = pd.merge(left = left, right = right, on = ['key1','key2'])
# print(result)
#right    按left的key来合并
# result = pd.merge(left = left, right = right, on = ['key1','key2'],how = 'right')
# print(result)


#indicator = True:显示每一行的合并方式   默认名字为_merge
df1 = pd.DataFrame({'col1':[0,1],'col_left':['a','b']})
df2 = pd.DataFrame({'col1':[1,2,2],'col_right':[2,2,2]})
# print(df1,end = '\n\n')
# print(df2,end = '\n\n')
#outer :没有的元素填充nan 
result = pd.merge(df1,df2,on = 'col1',how = 'outer',indicator = True)
# print(result)
#give the indicator a custom name      自定义indicator名
result = pd.merge(df1,df2,on = 'col1',how = 'outer',indicator = 'indicator_column')

'''merged by index'''
left = pd.DataFrame({'A':['A0','A1','A2'],
                    'B':['B0','B1','B2']},
                  index = ['k0','k1','k2'] 
)
right = pd.DataFrame(
    {'C':['C0','C2','C3'],
        'D':['D0','D2','D3']},
        index = ['k0','k2','k3'],
)
# print(left)
# print(right)
#left_index and right_index
result1 = pd.merge(left,right,left_index=True,right_index=True,how = 'outer')
result2 = pd.merge(left,right,left_index=True,right_index=True,how = 'inner')
# print(result1)
# print(result2)

#handle overlapping(部分重叠)
boys = pd.DataFrame({'k':['K0','K1','K2'],'age':[1,2,3]})
girls = pd.DataFrame({'k':['K0','K0','K3'],'age':[4,5,6]})
#避免age重复,使用suffixes重命名     eg:suffixes: Suffixes = ("_x", "_y"),
result3 = pd.merge(boys,girls,on = 'k', suffixes=['_boy','_girl'],how = 'inner')
result4 = pd.merge(boys,girls,on = 'k', suffixes=['_boy','_girl'],how = 'outer')
print(boys)
print(girls)
print(result3)
print(result4)