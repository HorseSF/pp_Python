# 定义函数
def multiply(x,y):
    return x*y

# 呼叫函数
x=int(input("输入第一个数字"))
y=int(input("输入第二个数字"))
value=multiply(x,y)
print(value)

# 函数的包装
def calculate(max):
    sum=0
    for i in range(1,max+1):
        sum=sum+i
    print(sum)

x=int(input("输入一个整数："))
calculate(x)