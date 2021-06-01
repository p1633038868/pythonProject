import random

# discount=["lenovo5折","ipnone6折","Mac6折","卫龙6折","老干妈7折"]
while True:
    discount = ["lenovo5折", "ipnone6折", "Mac6折", "卫龙辣条6折"]
    num = input("抽奖\n请输入1:")
    if num == "1":
        index = random.randint(0, 3)
        ss = str(discount[index])
        print("恭喜你获得", ss, "优惠券")
    break

shop = [
    ["Ipone 12 pro", 12000],
    ["HUAWEI WATCH", 2000],
    ["LENOVO PC", 15000],
    ["卫龙辣条", 1400],
    ["Mac", 13000],
    ["老干妈", 1200]

]
# 展示商品
for index, Value in enumerate(shop):
    print(index, Value)

# 初始化新资
salary = input("请输入您的新资:")
salary = int(salary)
print("您的新资为：", salary)

# 3.推个购物车
mycart = []

# 4开始购物，死循环
while True:
    # 打印超市商品
    for index, Value in enumerate(shop):
        print(index, Value)
    # 提示用户输入
    num = input("请输入您要的商品编号:")
    # 判断输入是否非法
    if num.isdigit():  # 判断“56”能不能看成56
        num = int(num)
        # 4.判断输入的编号的商品是否存在
        if num > len(shop):
            print("对不起您要的商品不存在，请选择其他商品！")
        else:
            # 看钱够不够
            if salary < shop[num][1]:
                print("对不起您的余额不足！")
            else:
                # 添加购物车
                mycart.append(shop[num][1])

                if ss == "lenovo5折":
                    sa = shop[num][1] * 0.5

                elif ss == "ipnone6折":
                    sa = shop[num][1] * 0.7
                elif ss == "Mac6折":
                    sa = shop[num][1] * 0.8
                elif ss == "卫龙辣条6折":
                    sa = shop[num][1] * 0.9
                else:
                    sa = shop[num][1]

                # 将薪资减去对应的金额
                salary = salary - sa
                print(ss)

                print("添加成功：￥", salary)



    elif num == "q" or num == "Q":
        print("欢迎下次光临！")
        break
    else:
        print("输入非法，请重新输入！")

# 打印小条
for index, Value in enumerate(mycart):
    print(index, "", Value)
print("您的本次余额", salary)
