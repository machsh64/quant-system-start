import pandas as pd
import numpy as np

# 进行dataframe的加减列
df = pd.DataFrame(np.array([
    ["Alice", 31, "New York"],
    ["Bob", 30, "Los Angeles"],
    ["David", 40, "Houston"]
]))

df.columns = ["name", "age", "city"]

# 直接指定列引添加新行
df["newColumn"] = ["c1", "c2", "c3"]

df["age"] = df["age"].astype(int)

print(df)

print("\n ---------------------------------------------------------------------------------------------------------------- \n")

# 添加新行

# 使用 loc 为特定索引添加新行
df.loc[3] = ["Ren", 14, "chongqing", "c4"]
print(df)

print("\n ---------------------------------------------------------------------------------------------------------------- \n")

# 使用 append 添加新行到末尾 pandas 1.4被弃用，不再使用，改用concat 合并2个或多个dataframer
new_row = {'name': ["machsh", "trump"], 'age': [15, 18], 'city': ["chongqing", "new york"], 'newColumn': ["c5", "c6"]}
# df = df.append(new_row, ignore_index=True)
# print(df)

# 使用 concat 合并两个或多个
df = pd.concat([df, pd.DataFrame(new_row)], ignore_index=True)
print(df)

print("\n ---------------------------------------------------------------------------------------------------------------- \n")

# 使用 numpy 创建时，会出现类型推断的情况，导致这里的age参数是object 类型，后续的排序就会出现类型不统一，需要进行类型转换
df2 = pd.DataFrame(np.array([
    ["machsh1", 15, "chongqing", "c5"],
    ["trump1", 18, "new york", "c6"]
]))
df2.columns = ["name", "age", "city", "newColumn"]

df = pd.concat([df, df2], ignore_index=True)

print(df)

print("\n ---------------------------------------------------------------------------------------------------------------- \n")

df['age'] = pd.to_numeric(df['age'], errors='coerce')

df.sort_values(by="age", ascending=False)

print(df)

print("\n ---------------------------------------------------------------------------------------------------------------- \n")

# 更推荐使用字典进行创建dataframer

new_row = pd.DataFrame({
    "name": ["machsh2", "trump2"],
    "age": [15, 18],
    "city": ["chongqing", "new york"],
    "newColumn": ["c5", "c6"]
})

df = pd.concat([df, new_row], ignore_index=True)

print(df)
