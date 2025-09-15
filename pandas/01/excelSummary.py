import pandas as pd

pd_read_excel = pd.read_excel('runoob_pandas_data.xlsx', skiprows=1)

print(pd_read_excel)

new_pd = pd.DataFrame({
    '姓名': ['小王', '小李', '小张'],
    '年龄': [18, 19, 20],
    '城市': ['上海', '北京', '广州']
})

print("\n ------------------------------------------------------ \n")
# 合并并写入excel中

new_pd.columns = pd_read_excel.columns

pd_read_excel = pd.concat([pd_read_excel, new_pd], ignore_index=True, axis=0).sort_values(by="Age", ascending=False)

print(pd_read_excel)

print("\n ------------------------------------------------------ \n")

# 使用openpyxl追加数据，不讲excel完整加载到内存中导致程序缓慢

# from openpyxl import load_workbook
#
## 只读取列名用于匹配
# column_names = pd.read_excel('runoob_pandas_data.xlsx', nrows=1).columns
#
## 创建要追加的新数据
# new_data = pd.DataFrame({
#    '姓名': ['小王', '小李', '小张'],
#    '年龄': [18, 19, 20],
#    '城市': ['上海', '北京', '广州']
# })
#
## 确保列名匹配
# new_data.columns = column_names
#
## 使用openpyxl直接追加到现有文件
# wb = load_workbook('runoob_pandas_data.xlsx')
# ws = wb.active
#
## 找到最后一行
# last_row = ws.max_row
#
## 追加新数据
# for i, row in new_data.iterrows():
#    for j, value in enumerate(row, 1):
#        ws.cell(row=last_row + i + 1, column=j, value=value)
#
# wb.save('runoob_pandas_data.xlsx')
# print("数据已成功追加到Excel文件中。")
#
# pd_read_excel = pd.read_excel('runoob_pandas_data.xlsx', skiprows=1)
#
# print(pd_read_excel)

print("\n ------------------------------------------------------ \n")

# 使用 ExcelFile 加载 Excel 文件
excel_file = pd.ExcelFile('runoob_pandas_data.xlsx')

# 查看所有表单的名称
print(excel_file.sheet_names)

# 读取指定的表单
df = excel_file.parse('sheet1')
print(df)

# 关闭文件
excel_file.close()

print("\n ------------------------------------------------------ \n")

# 使用 ExcelWriter 写入多个工作表

pd_f1 = pd.DataFrame(
    data=[
        ['小王', 11, '上海'],
        ['小李', 13, '北京'],
        ['小张', 12, '广州']
    ],
    columns=['姓名', '年龄', '城市']
)

pd_f2 = pd.DataFrame(
    data=[
        ['WANG', 11, 'NEW YORK'],
        ['DARM', 13, 'LOS ANGELS']
    ],
    columns=['NAME', 'AGE', 'CITY']
)

with pd.ExcelWriter("merge_file.xlsx") as writer:
    pd_f1.to_excel(writer, sheet_name="Sheet1")
    pd_f2.to_excel(writer, sheet_name="Sheet2")

    print("文件已保存。")

pd_read_excel = pd.ExcelFile("merge_file.xlsx")
print(pd_read_excel.sheet_names)

for sheet_name in pd_read_excel.sheet_names:
    print(pd_read_excel.parse(sheet_name))

print("\n ------------------------------------------------------ \n")

# 向现有excel追加内容
pd_f3 = pd.DataFrame(
    data=[
        ['GGBOND', 11, '上海'],
        ['FEIFEI', 13, '北京'],
        ['CHAORQ', 12, '广州']
    ],
    columns=['姓名', '年龄', '城市']
)
with pd.ExcelWriter('merge_file.xlsx', engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
    pd_f3.to_excel(writer, sheet_name="Sheet3")

pd_read_excel = pd.ExcelFile("merge_file.xlsx")
print(pd_read_excel.sheet_names)

for sheet_name in pd_read_excel.sheet_names:
    print(pd_read_excel.parse(sheet_name))
