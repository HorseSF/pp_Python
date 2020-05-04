import pandas as pd

# 自建索引
data=pd.Series([5,4,-2,3,7],index=["a","b","c","d","e"])

# 参数
print("数据型",data.dtype)
print("数据数量",data.size)
print("数据索引",data.index)

# 根据顺序取得数据
print("根据顺序取得数据")
print(data[2])
print("---------------")

# 根据索引取得数据
print("根据索引取得数据")
print(data["e"])
print("---------------")

# 数字运算
print("最大值")
print(data.max())
print("---------------")

print("总和")
print(data.sum())
print("---------------")

print("标准差")
print(data.std())
print("---------------")

print("中间值")
print(data.median())
print("---------------")

print("最大前三")
print(data.nlargest(3))
print("---------------")

print("最小两位")
print(data.nsmallest(2))
print("---------------")

# 字符串运算
data=pd.Series(["您好","Python","Pandas"])

print("全小写")
print(data.str.lower())
print("---------------")

print("长度")
print(data.str.len())
print("---------------")

print("连接字符串")
print(data.str.cat(sep="_"))
print("---------------")

print("判断是否包含特定字符")
print(data.str.contains("P"))
print("---------------")

print("替换为")
print(data.str.replace("您好","Hello"))
print("---------------")