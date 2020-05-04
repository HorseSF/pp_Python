# 定义类别
# 定义一个类别IO
class IO:
    supportedSrc=["console","file"]

    def read(src):
        if src not in IO.supportedSrc:
            print("Not supported")
        else:
            print("Read from",src)

print(IO.supportedSrc)
IO.read("file")
IO.read("internet")