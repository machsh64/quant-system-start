import json
import pandas as pd
from glom import glom
from io import StringIO

# 将df转换为json

data = [
    {
        "id": "A001",
        "name": "菜鸟教程",
        "url": "www.runoob.com",
        "likes": 61
    },
    {
        "id": "A002",
        "name": "Google",
        "url": "www.google.com",
        "likes": 124
    },
    {
        "id": "A003",
        "name": "淘宝",
        "url": "www.taobao.com",
        "likes": 45
    }
]
df = pd.DataFrame(data)
df.to_json("json_file.json")
print(df)

print("\n ------------------------------------------------------ \n")

# 读取json文件
pd_read_json = pd.read_json("json_file.json")
print(pd_read_json.to_string())

print("\n ------------------------------------------------------ \n")

# json与pd的字典类型相似，所以可以直接将字段转换为df
json_data = {
    "id": {"row1": "A001", "row2": "A002", "row3": "A003"},
    "name": {"row1": "菜鸟教程", "row2": "Google", "row3": "淘宝"},
    "url": {"row1": "www.runoob.com", "row2": "www.google.com", "row3": "www.taobao.com"}
}

pd_data_frame = pd.DataFrame(json_data)
print(pd_data_frame)

print("\n ------------------------------------------------------ \n")

# 还可以从在线json文件中读取为df
URL = 'https://static.jyshare.com/download/sites.json'
#df = pd.read_json(URL)
#print(df)

print("\n ------------------------------------------------------ \n")

# 从json字符串中解析为df
# JSON 字符串
json_data = '''
[
  {"Name": "Alice", "Age": 25, "City": "New York"},
  {"Name": "Bob", "Age": 30, "City": "Los Angeles"},
  {"Name": "Charlie", "Age": 35, "City": "Chicago"}
]
'''

# 从 JSON 字符串读取数据
df = pd.read_json(StringIO(json_data))
data = json.loads(json_data)
df2 = pd.DataFrame(data)
print("df1: ", df)
print("df2: ", df2)

print("\n ------------------------------------------------------ \n")

# 从复杂json中，展平获取其中某个字段的df
read_json = pd.read_json('nested_list.json')
print(read_json) # 此种读取方式，只能读取最外层字段

# 使用 Python JSON 模块载入数据, 逐行读取文件并加载进json
with open('nested_list.json', 'r') as f:
    data = json.loads(f.read())

# 展平json数据，并加载为df，展平函数为 json_normalize
# 参数 record_path 参数指定了嵌套列表的子字段
# 参数 meta 参数指定需要展示的指定嵌套字段外的字段元数据，meta只能指定一级字段，嵌套字段无法展平
df_nested_list = pd.json_normalize(
    data,
    record_path=['students'],
    meta=['school_name', 'class']
)
print(df_nested_list)

print("\n ------------------------------------------------------ \n")

# 更复杂一点的json中，除 record 指定嵌套字段外的字段需要展示，同样用 meta，但是在meta内部用[1,2,3]表示1.2.3级嵌套的元数据

with open('nested_mix.json', 'r') as f:
    data = json.loads(f.read())

df = pd.json_normalize(
    data,
    record_path=['students'],
    meta=[
        'class',
        ['info', 'president'],
        ['info', 'contacts', 'tel']
    ]
)

print(df.to_string())

print("\n ------------------------------------------------------ \n")

# 如果需要读取内嵌数据中的某个字段，则要用到glom，glom可以支持用 . 来访问嵌套字段，类似于 students.grade.chemistry
# 例如读取nested_deep中的chemistry字段
deep_json_df = pd.read_json('nested_deep.json')
data_chemistry = deep_json_df["students"].apply(lambda x: glom(x, 'grade.chemistry'))
print(data_chemistry)

print("\n ------------------------------------------------------ \n")

# 将df转换为json
df = pd.DataFrame(
    data={
        "id": [1, 2, 3],
        "name": ["Alice", "Bob", "Charlie"],
        "age": [25, 30, 35]
    },
    index=[1, 2, 3]
)

json_str = df.to_json()
print(json_str)
# 转换到文件里
df.to_json("json_output_file.json")
print(pd.read_json("json_output_file.json"))
# 使用records模式
df.to_json("json_output_file.json", orient="records")
print(pd.read_json("json_output_file.json"))
# 查看records方式的json
with open('json_output_file.json', 'r') as f:
    json_loads = json.loads(f.read())
print(json_loads)
