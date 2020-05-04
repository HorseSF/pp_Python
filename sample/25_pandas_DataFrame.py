import pandas as pd

# 建立DataFrame
data=pd.DataFrame({
    "name":["Amy","Bob","Charles"],
    "salary":[3000,5000,4000]
},index=["a","b","c"])
print(data)
print("----------")

# 参数
print("数据数量",data.size)
print("数据型",data.shape)
print("数据索引",data.index)
print("----------")

# 取得行
print("取得第2行",data.iloc[1], sep="\n")
print("----------")

print("取得第c行",data.loc["c"], sep="\n")
print("----------")

# 取得列
print("取得name列",data["name"], sep="\n")
print("----------")

# DataFrame->Series
names=data["name"]
print("所有名字转大写",names.str.upper(), sep="\n")

tolSal=data["salary"]
print("取得薪水的平均值",tolSal.mean())

# 添加新的列
data["revenue"]=[50000,40000,30000]
print(data)

data["rank"]=pd.Series([3,6,1], index=["a","b","c"])
print(data)

data["cp"]=data["revenue"]/data["salary"]
print(data)