# if文
# python没有switch文

x=input("请输入数字:")
x=int(x)
if x>200:
    print("大于200")
elif x>100:
    print("大于100小于或等于200")
else:
    print("小于或等于100")

print("------------")
print("四则运算")
n1=int(input("请输入第一个数字："))
n2=int(input("请输入第二个数字："))
op=input("请输入运算符号：+,-,*,/")

if op=="+":
    print(n1+n2)
elif op=="-":
    print(n1-n2)
elif op=="*":
    print(n1*n2)
elif op=="/":
    print(n1/n2)
else:
    print("未知运算")