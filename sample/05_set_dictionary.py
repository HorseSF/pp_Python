s1={3,4,5}

# 判断对象是否在集合里
print("判断3是否在集合中")
print(3 in s1)
print("判断10是否不在集合中")
print(10 not in s1)
print("------------")

s2={4,5,6,7}

# 交集
print("交集")
s3=s1&s2
print(s3)
print("------------")

# 连集
print("连集")
s3=s1|s2
print(s3)
print("------------")

# 差集
print("差集")
s3=s1-s2
print(s3)
print("------------")

# 反交集
print("反交集")
s3=s1^s2
print(s3)
print("------------")

# 拆解字符串成集合
print("拆解字符串成集合")
s=set("hello")
print(s)
print("h" in s)
print("------------")

#字典 Key-value
print("字典")
dic={"apple":"苹果","orange":"橘子"}
print(dic["apple"])
dic["apple"]="青苹果"
print(dic["apple"])
print("------------")

# 判断对象是否在字典里
print("判断对象是否在字典里")
print("apple" in dic)
print("------------")

# 删除字典中的键值
print("删除键")
print(dic)
del dic["apple"]
print(dic)
print("------------")

# 列表转换字典
print("列表转换字典")
dic={i:i*2 for i in [3,4,5]}
print(dic)
print("------------")