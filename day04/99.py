#
#
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



# i  = 1
# while i <= 4:  # 控制层数
#     # 打印星号
#     j = 1
#     while j <= i:  # 控制每层的打印个数
#         print("*",end="") # end="不换行"
#         j = j + 1
#     print()  # 换行
#     i = i + 1




a = ["AA","bb","cc","dd","gg","jj"]

import random
print("--------------欢迎来到教务管理系统--------------------")

while True:
    print("1:随机点名，2：随机处罚")
    num = input("请输入你的编号:")
    if num == "1":
        index=random.randint(0,5)

        print("恭喜你，",a[index],"!")
        ints=str(a)
        a.remove(a[index])


    elif num =="2":

        chose = random.randint(0,201)
        print(chose)
        print("恭喜，您被处罚",chose,"遍")
    elif num == "q" or num == "Q":
        print("下次欢迎光临！")

        break
    else:
        print("对不起，没有该业务，请重新输入！")

