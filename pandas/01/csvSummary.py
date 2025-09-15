import pandas as pd

# 读取 csv 数据
pd_read_csv = pd.read_csv('nba.csv')

print(pd_read_csv)

# 导出为csv
pd_output_csv = pd.DataFrame({
    'Name': ['Tom', 'Nick', 'John'],
    'Age': [20, 21, 19],
    'City': ['New York', 'London', 'Paris'],
    'Salary': [5000, 6000, 7000]
})

# 导出，index默认为true，保留索引，columns 默认为true，保留列名，sep 默认为','
pd_output_csv.to_csv('output.csv', index=False)