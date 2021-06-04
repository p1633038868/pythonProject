import random

# 银行的库
names = {}
'''
{
        "zs":{address:"沙河桥底下",money:546},
        "ls":{address:"沙河桥底下",money:546}
}
'''

# 开户行名称
bank_name = "中国工商银行昌平支行"
# 欢迎来到页面模板
welcome = '''
    ------------------------------------
    -   欢迎来到中国工商银行账户管理系统    -
    -1.开户                             -
    -2.存钱                             -
    -3.取钱                             -
    -4.转账                             -
    -5.查询                             -
    -6.Bye！                            -
'''


def getRandom():
    li = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
          "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
          "w", "x", "y", "z",
          "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
          "W", "X", "Y", "Z"]
    string = ""
    for i in range(8):
        ch = li[random.randint(0, len(li) - 1)]
        string = string + ch
    return string


# 银行开户逻辑
def bank_addUser(account, username, password, money, country, province, street, door):
    # 判断是否存在
    if len(names) >= 100:
        return 3

    # 判断是否存在:依据是用户名
    if username in names:
        return 2

    # 3.正常开户
    names[username] = {
        "account": account,
        "username": username,
        "password": password,
        "money": money,
        "counttry": country,
        "province": province,
        "street": street,
        "door": door,
        "bank_name": bank_name
    }
    return 1


# 开户操作
def addUser():
    username = input("请输入您的姓名：")
    password = input("请输入你的密码：")
    money = int(input("请输入您的账户余额：")) # "123"  123
    print("下面请输入您的个人地址信息：")
    country = input("请输入您的国籍：")
    province =  input("请输入您的省份：")
    street = input("请输入您的居住街道：")
    door = input("请输入您的门牌号：")
    account = getRandom()
    status = bank_addUser(account,username,password,money,country,province,street,door)
    if status == 1:
        print("恭喜开户成功！以下是您的个人信息：")
        info = '''
            ----------个人信息 【工商银行】--------
            用户名：%s,
            密码：%s,
            账号：%s,
            余额：%s,
            国家：%s,
            省份：%s,
            街道:%s,
            门牌号：%s
            开户行名称：%s
            ------------------------------------
        '''
        print(info % (username,password,account,money,country,province,street,door,bank_name))


    elif status == 2:
        print("对不起您的账户已存在！请勿重复开户")
    elif status == 3:
        print("对不起,用户库已满")


def moneys():
    username = input("请输入账号")
    money = int(input("输入你存款的钱"))
    ss = bank_moneys(username, money)
    if ss == False:
        print("不存在")


def bank_moneys(username, money):

    if username in names:
        s = money + names[username]['money']
        s=names[username]['money']
        print("存款成功现在账户余额为", s,"之前为",names[username]['money'])
    else:
        print("账户不存在")






def quqian():

    username= input("请输入用户名")
    account = input("请输入账号")
    password=input("请输入您的密码")
    money=int(input("请输入取钱金额"))


    ss = bank_money(username,account,password, money)
    if ss == 1:
        print("用户名不存在")
    elif ss == 2:
        print("密码不对")
    elif ss == 3:
        print("钱不够")
    elif ss==4:
        print("账号不存在")



def bank_money(username,account,password, money):
    if username not in names:
        return 1
    if password not in  names[username]['password']:
        return 2
    if money > names[username]['money']:
        return 3
    if account not in names[username]['account']:
        return 4
    mo=names[username]['money']- money
    names[username]['money']=mo
    print("取款成功,当前账户为", mo)
    return 0






#入口程序
while True:
    print(welcome)
    chose = input("请输入您的业务编号")
    if chose == "1":
        # 直接调用
        addUser()
    elif chose == "2":
        moneys()
    elif chose == "3":
        quqian()
    elif chose == "4":
        pass
    elif chose == "5":
        pass
    elif chose == "6":
        break
    else:
        print("输入非法！别几把弄！")
