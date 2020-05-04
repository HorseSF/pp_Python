import sys as system
system.path.append("modules")
import geometry

# 计算两点距离
result=geometry.distance(1,1,5,5)
print("两点距离：",result)

# 计算斜率
result=geometry.slope(1,2,4,5)
print("斜率：",result)
