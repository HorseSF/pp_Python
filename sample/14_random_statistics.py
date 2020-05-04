# 随机模组
import random
# 随机选取1个数据
print("随机选取1个数据")
data=random.choice([1,2,3,4,5,6,7,8,9])
print(data)
print("-------------")

# 随机选取n个数据
print("随机选取n个数据")
data=random.sample([1,2,3,4,5,6,7,8,9],3)
print(data)
print("-------------")

# 随机调换顺序
print("随机调换顺序")
data=[1,2,3,4,5,6,7,8,9]
random.shuffle(data)
print(data)
print("-------------")

# 随机取得乱数
print("随机取得0到1之间的乱数 random()")
data=random.random()
print(data)
print("-------------")

print("随机取得0到1之间的乱数 uniform()")
data=random.uniform(60,100)
print(data)
print("-------------")

# 取得正态分布乱数
print("取得正太分布乱数，平均数100，标准差10")
data=random.normalvariate(100,10)
print(data)
print("-------------")

# 统计模组
import statistics as stat

# 平均数
print("平均数")
data=stat.mean([1,2,3,4,5,6,7,8,9,100])
print(data)
print("-------------")

# 中间数
print("中间数")
data=stat.median([1,2,3,4,5,6,7,8,9,100])
print(data)
print("-------------")

# 标准差
print("标准差")
data=stat.stdev([1,2,3,4,5,6,7,8,9,10])
print(data)
print("-------------")