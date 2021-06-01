'''
    1.len(): 求任何数据的长度
    "jason"
    li = [1,5,7,8]
    2.for  x   in y:    y(一般都是一个容器)    x 代表就是每个元素的变量

'''
# num= input("请输入N层三角形：")
# num = int(num)
#
# i = 1
# while i <= num:
#     # 打印空格
#     j = 1
#     while j <= num - i:
#         print(" ",end="")
#         j = j + 1
#     # 打印星号
#     k = 1
#     while k <= i:
#         print("* ",end="")
#         k = k + 1
#
#     print()  # 换行
#     i = i + 1

# li = [36710.36,35427.10,29863.23,29667.39,27665.36,27650.45,27620.38,25369.20,8936.23]
# sum = 0
#
# for data in li:
#     sum = sum + data
#
# print("总和为：",sum,"，平均值为：",(sum / len(li)))
# li = [56,52,32,41,12,74,85,95,100]
#
# i = 0
# while i < len(li)//2:
#     s = li[i]
#     li[i] = li[len(li)-1-i]
#     li[len(li)-1-i]=s
#     i = i + 1
# print(li)

li = [1,5,6,7,4,1,3,2,8,4,5,6]

# print(li[1:3])   起始角标 ： 结束角标    start  ~  end - 1
# li[1:]
# for index,value  in  enumerate(li):# 0,1
# #     if value in li[:index]: # 排重
# #         continue
# #     else:   # 统计
# #         print(value,"出现了",li.count(value),"次！") #count统计







li = [1,5,6,7,4,1,3,2,8,4,5,6]
i = 0
while i < len(li):  #len下标长度
    count = 0
    # 排重
    k = 0
    flag = 0 #True
    while k < i:
        if li[i] == li[k]:
            flag = 1 #false
            break  #终止
        k = k + 1

    if flag == 1:
        i = i + 1
        continue # 终止后面的程序，直接进行下一轮
    # 统计
    j = i
    while j < len(li):
        if li[i] == li[j]:
            count = count + 1
        j = j + 1
    print(li[i],"出现了",count,"次！")
    i = i + 1


li = [5,6,8,9,10,12,15,74,10]

# 列表排序

#排序
# for a in range(len(li)):
#     for s in range(a+1,len(li)):
#         if li[a]<li[s]:
#              li[a],li[s]=li[s],li[a]
#
#
# print(li)
#
# count=0
# for a in range(len(li)):
#     for s in range(a+1,len(li)):
#         if li[a]>li[s]:
#              li[a],li[s]=li[s],li[a]
# print(li)




# num = input("请输入一个数")
# num=int(num)
# i=1
# while i<=num: #控制层数
#     j = 1
#     while j<=i:#每层打印
#         print(j,"x",i,"=",(j*i),"     ",end="") #打印每层的乘法表
#         j=j+1
#     print()# 换行
#     i+=1# 下一行



#
# i=9
# while i>=1: #控制层数
#     j = 1
#     while j<=i:#每层打印
#         print(j,"x",i,"=",(j*i),"   ",end="") #打印每层的乘法表
#         j=j+1
#     print()# 换行
#     i=i-1# 下一行