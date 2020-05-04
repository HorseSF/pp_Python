# 有序可变列表List
grades=[12,60,15,70,90]
print("获取所有元素")
print(grades[0])
print("------------")

print("获取第N元素")
grades[0]=55
print(grades[0])
print("------------")

print("获取第1到3的元素")
print(grades[1:4])
print("------------")

print("删除第1到3的元素")
grades[1:4]=[]
print(grades)
print("------------")

print("列表串接")
grades=grades+[12,33]
print(grades)
print("------------")

print("列表长度")
length=len(grades)
print(length)
print("------------")

print("多层列表")
data=[[3,4,5],[6,7,8]]
print(data[1][0:2])
print("------------")

# 有序不可变列表 Tuple
print("Tuple")
tuple=(3,4,5)
print(tuple[0:2])
print("------------")