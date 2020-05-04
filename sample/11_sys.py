import sys as system
print(system.platform)
print(system.maxsize)

# 添加模组搜索路径
system.path.append("modules")
# 模组的搜寻路径
print(system.path)