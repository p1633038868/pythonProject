a = ['小明', '小张', '小黄', '小杨']
b = ['小黄', '小李', '小王', '小杨', '小周']
c = ['小杨', '小张', '小吴', '小冯', '小周']

ad = set(a)
bd = set(b)
cd = set(c)

# 选课学生总共有多少人求选课学生总共有多少人
fff = ad | bd | cd
t = 0
for x in fff:
    t = t + 1
print("选课学生总数", t)

# # 2)	求只选了第一个学科的人的数量和对应的名字
count = 0
for i in a:
    if a:
        count = count + 1
        print(i, end=" ")
print(count)

#
# # 3)	求只选了一门学科的学生的数量和对应的名字

# count = 0
# for i in a:
#     if i not in b and i not in c:
#         count = count + 1
#         print(i)
# for i in b:
#     if i not in a and i not in c:
#         count =count + 1
#         print(i)
# for i in c:
#     if i not in b and i not in a:
#         count = count + 1
#         print(i)
# print(count)


# 求只选了第一个学科的人的数量和对应的名字
t = 0
lis1 = []
for x in a:
    lis1.append(x)
    t = t + 1
print(t, lis1)

# 求只选了语文和英语的学生的数量和对应的名字

ad = set(a)
bd = set(b)
cd = set(c)

f = ad & cd
t = 0
list = []
for x in f:
    list.append(x)
    t = t + 1
print("语文和英语对应的数量和名字", t, list)

# 求只选了一门学科的学生的数量和对应的名字
B = ad ^ bd ^ cd ^ (bd & ad & cd)
t = 0
list2 = []
for x in B:
    list2.append(x)
    t += 1
print('只选了一门学科的人数：', t, list2)


