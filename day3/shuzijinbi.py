import  random
# num=1
# num = random.randint(1,10)

# a=1
# while a<=10:
#     a=a+1
#     print(random.randint(10,100))



# print(random.randint(50,150))


#
# n1=input("请输入数字:")
# n2=input("请输入数字:")
# n3=input("请输入数字:")
# n4=input("请输入数字:")
# n5=input("请输入数字:")
# n6=input("请输入数字:")
# n7=input("请输入数字:")
# n8=input("请输入数字:")
# n9=input("请输入数字:")
# n10=input("请输入数字:")
# sum=int(n1)+int(n2)+int(n3)+int(n4)+int(n5)+int(n6)+int(n7)+int(n8)+int(n9)+int(n10)
#
# print(sum)


# 实现输入10个数字，并打印10个数的求和结果
# n = 0
# sum =0
# while n<10:
#      num = input("请输入10个数：")
#      sum = int(sum) + int(num)
#      n +=1
#      print()
# print("10个数的和为:%d" % sum)
# print("10个数的平均值为:%.2f" % (sum / 10))


# # 实现输入10个数字，并打印10个数的求和结果
# n=0
# sum=0
# while n<10:
#      num = input("请输入10个数：")
#      sum = int(sum) + int(num)
#      n +=1
# print()
# print("10个数的和为:%d" % sum)




#使用random模块，如何产生 50~150之间的数？
# print(random.randint(50,100))


# 从键盘输入任意三边，判断是否能形成三角形，若可以，则判断形成什么三角形（结果判断：等腰，等边，直角，普通，不能形成三角形。）



# a = int(input("输入三角形第一边长："))
# b = int(input("输入三角形第二边长："))
# c = int(input("输入三角形第三边长："))
#
# if a<=9 and b>2 and c>2  :
#     print("等腰")
# elif a<=8 and b>1 and c>5  :
#     print("直角")
# elif a<=5 and b>1 and c>5  :
#     print("等边")
# elif a<=2 and b>1 and c>5  :
#     print("普通")
# else:
#     print("不能形成三角形")



# a = 56
# b = 78
# a,b = b,a
# print(a)
# print(b)


# name ="root"
# password ="admin"
# a=3
# while  a>3:
#     namea= input("用户名")
#     passworda= input("密码")
# if name==namea and password==passworda:
#     print("玩命加载中...")
# elif namea!=name and passworda != password:
#     print("密码错误")
# else:
#     print("")




# random
num = random.randint(1,100)
money = 5000
count = 0
while True :
    money = money - 500
    count = count + 1
    if money >= 0 :
        a = int(input("请输入数字："))
        if a == num :
            if count <= 3 :
                print("恭喜你！猜对了！获得两百元奖励~")
                money+=200
                print(money)
                break
            else :
                print("猜对了！恭喜你！你猜了",count,"次")
                break
        elif a > num :
            print("大了！")
            print(money-200)
        else :
            print("小了！")
            print(money-200)
    else :
        print("您没钱了")
        break

print("答案为：",num)

