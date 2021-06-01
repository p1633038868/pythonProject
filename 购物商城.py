'''
-------------------地狗商城系统----------------
    购物车：
    1.初始化自己的薪资余额
    2.展示哪些商品
    需求：
        前提：有 3张lenovo的5折券，4张ipnone&mac的6这券。买东西之前随机抽奖。在最终结算的时候使用券完成优惠！
        1.若金钱够了，可以购买，将当前这个商品添加到购物车。
        2.若不够，不能购买，温馨提示：穷鬼！金钱不够！
        3.若商品编号不存在，打印错误信息，给温馨提示：别瞎弄！
        4.输入Q或者q，购物结束，并打印购物小条。
'''
import  random
# 存个商品
shop = [
    ["Iphone 12 pro",12000],
    ["HUAWEI watch",2000],
    ["lenovo PC",5000],
    ["Mac pc",13000],
    ["卫龙辣条",5],
    ["老干妈",7.5]
]
coupon = []
random.randint()

# 1.展示商品
for  index,value  in enumerate(shop):
    print(index,value)
# 2.初始化薪资
salary = input("请输入您的薪资：")
salary = int(salary)
# 3.推个空的购物车
mycart = []
# 4.开始购物，死循环
while True:
    # 打印超市商品
    for index,value in enumerate(shop):
        print(index,"",value)
    # 2.提示用户输入
    num = input("请输入您要的商品编号：")
    # 3.判断输入是否合法
    if num.isdigit():  # 判断“56” 能不能看成  56
        num = int(num)
        # 4.判断输入的编号的商品是否存在
        if num > len(shop): # 判断上平是否存在
            print("对不起，您要的商品不存在！请选择其他商品！")
        else:
            # 看钱够不够
            if salary < shop[num][1]:
                print("对不起，您的余额不足，穷鬼！")
            else:
                # 添加购物车
                mycart.append(shop[num])
                # 将薪资减去对应的金额
                salary = salary - shop[num][1]
                print("恭喜您！添加成功！您的余额为：￥",salary)
    elif num == 'q' or num == 'Q':
        print("欢迎下次光临！")
        break
    else:
        print("输入非法，别瞎弄！请重新输入！")
# 打印小条
print("您本次的购物情况如下：")
for index,value in enumerate(mycart):
    print(index,"",value)
print("您的余额为：￥",salary)





























