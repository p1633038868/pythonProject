a = ['小明', '小张', '小黄', '小杨']
b = ['小黄', '小李', '小王', '小杨', '小周']
c = ['小杨', '小张', '小吴', '小冯', '小周']

d = a + b + c
s = 0
for index, value in enumerate(d):
    if value in d[:index]:
        continue
    else:
        print(value, d.count(value))

# 求选课学生总共有多少人


# 求只选了第一个学科的人的数量和对应的名字
for x in a:
    print(x, a.count(x),end="")

# 3)	求只选了一门学科的学生的数量和对应的名字
t = 0
lis = []
for x in d:
    lis.append(x)
    t=t+1
print(t,lis)
