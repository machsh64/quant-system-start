import pandas as pd
import numpy as np

# 使用列表创建DataFrame
data = [['Google', 10], ['Runoob', 12], ['Wiki', 13]]

df = pd.DataFrame(data, columns=['Site', 'Age'])

# 使用astype方法设置每列的数据类型
df['Site'] = df['Site'].astype(str)
df['Age'] = df['Age'].astype(float)

print("\n df: \n", df)

# 也可以使用字典创建
data = {'Site':['Google', 'Runoob', 'Wiki'], 'Age':[10, 12, 13]}

df1 = pd.DataFrame(data, index=['a', 'b', 'c'])

print("\n df1: \n", df1)

# 使用 ndarray 创建
ndarray_data = np.array([
    ['Google', 10, 'China'],
    ['Runoob', 12, 'american'],
    ['Wiki', 13, 'japan']
])

df2 = pd.DataFrame(data= ndarray_data, columns=['Site', 'Age', 'country'])

print("\n df2 \n", df2)

# 用字典 key/value 创建
data = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]

df3 = pd.DataFrame(data)

print("\n df3 \n", df3)

# 可以使用 loc 函数，返回对应的行数据 [[...]], 可以返回多行数据 使用的是标签索引
print("\n df2.loc[[0, 2]] \n", df2.loc[[0, 2]])

# 可以使用 iloc 函数，返回对应的行数据 [[]], 可以返回多行数据  使用的是位置索引
print("\n df2.iloc[[0, 2]] \n", df2.iloc[[0, 2]])

# 获取指定行指定列的数据
print("\n df2.iloc[[0, 2], [0, 2]] \n", df2.iloc[[0, 2], [0, 2]])
