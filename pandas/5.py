#导入导出
import csv
import pandas as pd

#导入并读取数据       read_csv
data1 = pd.read_csv('./python/pandas/test.csv')
# print(data1)

#导出数据            to.csv    to_json to_pickle   etc...
data1.name = [1,2,3,4,5,6,7,8,9]
# print(data1)
data1.to_csv('./python/pandas/test_modified.csv')