# Point类 平面坐标
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

p1=Point(1,1)
print(p1.x,p1.y)

p2=Point(2,2)
print(p2.x,p2.y)

# FullName类
class FullName:
    def __init__(self,firstName,lastName):
        self.firstName=firstName
        self.lastName=lastName

name1=FullName("x.f","ma")
print(name1.firstName,name1.lastName)

name2=FullName("z.l","lin")
print(name2.firstName,name2.lastName)
