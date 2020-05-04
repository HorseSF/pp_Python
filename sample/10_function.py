# 参数预设变量
def power(base,exp=0):
    print(base**exp)
power(3,2)
power(3)

# 参数的名称对于
def divide(n1,n2):
    print(n1/n2)
divide(2,4)
divide(n2=2,n1=4)

# 不确定参数
def avg(*ns):
    sum=0
    for i in ns:
        sum=sum+i
    print(sum/len(ns))
avg(3,5,10)
