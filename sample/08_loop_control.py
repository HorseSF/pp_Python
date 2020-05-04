# break
n=0
while n<5:
    if n==3:
        break
    print(n)
    n+=1
print("最后的n：",n)

# continue
i=0
for i in [0,1,2,3]:
    if i%2==0:
        continue
    print(i)
    i+=1
else:
    print("执行else")
print("最后的i：",i)

# else
sum=0
for j in range(11):
    sum+=j
else:
    print(sum)

# 输入整数求平方根
x=input("输入一个整数：")
x=int(x)
for i in range(x):
    if i*i==x:
        print("平方根为：",i)
        # break结束循环不会执行else
        break
else:
    print("没有平方根。")