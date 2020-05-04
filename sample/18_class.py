class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    # 定义方法
    def show(self):
        print(self.x, self.y)

    def distance(self,targetX,targetY):
        return (((self.x-targetX)**2+(self.y-targetY)**2)**0.5)

p1=Point(3,4)
p1.show()
result=p1.distance(0,0)
print(result)

class File:
    # 初始化函数
    def __init__(self,fileName):
        self.fileName=fileName
        self.file=None

    # 实体方法Open
    def Open(self):
        self.file=open(self.fileName,mode="r",encoding="utf-8")

    # 实体方法Read
    def Read(self):
        return self.file.read()

f1=File("18_data1.txt")
f1.Open()
data=f1.Read()
print(data)

f2=File("18_data2.txt")
f2.Open()
data=f2.Read()
print(data)