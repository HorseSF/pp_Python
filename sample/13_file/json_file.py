import json

# 读取
with open("config.json",mode="r") as file:
    data=json.load(file)
print("name:",data["name"])
print("version:",data["version"])

# 修改
data["name"]="New Name"
with open("config.json",mode="w") as file:
    json.dump(data,file)