# 储存文件
# file=open("data.txt", mode="w", encoding="utf-8")
# file.write("测试中文1\n测试中文2")
# file.close
with open("data.txt", mode="w", encoding="utf-8") as file:
    file.write("5\n4\n3\n2\n1")

# 读取文件
# 求和
sum=0
with open("data.txt", mode="r", encoding="utf-8") as file:
    for line in file:
        sum+=int(line)
print(sum)