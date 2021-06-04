import random
# 银行的库
names = {}
'''
{
    "张三":{address:"沙河北大桥桥底下",money:546,account:1a5sdf1af},
    "李四":{address:"沙河北大桥桥底下",money:546}
}
'''
# 开户行名称
bank_name = "中国建设银行昌平支行"
# 欢迎页面的模板
welcome = '''
    -----------------------------------------
    -     欢迎来到中国建设银行账户管理系统     -
    -----------------------------------------
    -   1.开户                               -
    -   2.存钱                               -
    -   3.取钱                               -
    -   4.转账                               -
    -   5.查询                               -
    -   6.Bye!                               -
    ------------------------------------------
'''

def getRandom():
    li = ["1","2","3","4","5","6","7","8","9","0","a","b","c","d","e","f"]
    string = ""
    for i in range(8):
        ch = li[random.randint(0,len(li) - 1)]
        string = string +  ch
    return string

# 银行的开户逻辑
def bank_addUser(account,username,password,money,country,province,street,door):
    # 1.判断是否已满
    if len(names)  >= 100:
        return 3
    # 2.判断是否存在:依据是用户名
    if username in names:
        return 2
    # 3.开户
    names[username] = {
        "account":account,
        "username":username,
        "password":password,
        "money":money,
        "country":country,
        "province":province,
        "street":street,
        "door":door,
        "bank_name":bank_name
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
        print("对不起，您的账户已存在！请勿重复开户！")
    elif status == 3:
        print("对不起，用户库已满，请携带证件到其他银行办理！")

# 银行的转账逻辑  周福航
def bank_trans(username,account,password,money,account1,username1):
    if username not in names and username1 not in names:
        return 4
    if account not in names[username]["account"] or account1 not in names[username1]["account"]:
        return 1
    if password not in names[username]["password"]:
        return 2
    if names[username]["money"] < money:
        return 3
    if names[username]["money"] >= money:
        return 0
# 转账操作
def trans():
    username = input("请输入您的用户名：")
    account = input("请输入您的账户：")
    password = input("请输入您的密码：")
    username1 = input("请输入对方用户名：")
    account1 = input("请输入对方账号:")
    money = int(input("请输入转账金额:"))
    status = bank_trans(username, account, password, money, account1, username1)
    if status == 4:
        print("用户名错误，请重新输入！")
    if status == 1:
        print("账户错误，请重新输入！")
    if status == 2:
        print("密码错误，请检查密码！")
    if status == 3:
        print("余额不足，请重试")
    if status == 0:
        names[username1]["money"] = names[username1]["money"] + money
        names[username]["money"] = names[username]["money"]-money
        print("转账成功，账户余额",names[username]["money"],"元")

# 银行的查询逻辑  周福航
def bank_search(account,password,username):
    if account not in names[username]["account"]:
        return
    if password not in names[username]["password"]:
        return
    if account in names[username]["account"] and password in names[username]["password"]:
        return 1
# 查询操作
def search():
    username = input("请输入用户名：")
    account = input("请输入账号：")
    password = input("请输入密码：")
    money = names[username]['money']
    country = names[username]['country']
    province = names[username]['province']
    street = names[username]['street']
    door = names[username]['door']
    status = bank_search(account,password,username)
    if account not in names[username]["account"]:
        print("账号错误")
    if password not in names[username]["password"]:
        print("密码错误")
    if status == 1:
        print("查询成功，以下是详细信息：")
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
        print(info % (username, password, account, money, country, province, street, door, bank_name))

# 取款操作  裴情杰
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

# 银行的取款逻辑
def bank_money(username,account,password, money):
    if username not in names:
        return 1
    if password not in  names[username]['password']:
        return 2
    if money > names[username]['money']:
        return 3
    if account not in names[username]['account']:
        return 4
    mo=names[username]['money']-money
    names[username]['money']=mo
    print("取款成功,当前账户为", mo)
    return 0

# 存款 宫浩凯
def cunkuan():
    username = input("请输入您的帐号：")
    # 1判断是否存在
    if username in names:
        mima = input("请输入您的帐号密码：")
        # 判断密码是否正确
        if mima == names.get(username).get("password"):
            jine = input("请输入您要存款的金额：")
            s = int(names.get(username).get("money"))
            jine = int(jine)
            s = s + jine
            names[username]['money'] = s
            print("存款操作成功,您当前的余额为：",s,"￥")
        else:
            print("输入密码错误！请重新输入！")
    else:
        print("没有此账号！")

# 入口程序
while True:
    print(welcome)
    chose = input("请输入您的业务编号：")
    if chose == '1':
        addUser()
    elif chose == '2':
        cunkuan()
    elif chose == '3':
        quqian()
    elif chose == '4':
        trans()
    elif chose == '5':
        search()
    elif chose == '6':

        break
    else:
        print("输入非法！别瞎弄！")







