# 载入pandas模组
import pandas as pd

# 建立Series
data=pd.Series([20,10,15])

# 最大值
print("最大值:",data.max())
print("-------------")

# 中间值
print("中间值",data.median())
print("-------------")

# 所有值扩大两倍
data=data*2
print("所有值扩大两倍",data)
print("-------------")

# 比较运算
# 得到布尔值的Series
data=data==20
print(data)
print("-------------")

# 建立DataFrame
data=pd.DataFrame({
    "name":["Amy","John","Bob"],
    "salary":["30000","50000","40000"]
})

# 取得特定的列
print("取得特定的列")
print(data["name"])
print("-------------")

# 取得特定的行
print("取得特定的行")
print(data.iloc[0])
print("-------------")