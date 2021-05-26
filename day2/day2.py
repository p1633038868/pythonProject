# 羽绒服
clothesid1=1
clothestype1= "羽绒服"
clothesprice1=500
clothesquan1=50
clothesnorm1="xl"

# 牛仔裤
clothesid2=2
clothestype2= "牛仔裤"
clothesprice2=200
clothesquan2=20
clothesnorm2="xxl"

# 衬衫
clothesid3=3
clothestype3= "衬衫"
clothesprice3=100
clothesquan3=90
clothesnorm3="s"

# T恤
clothesid4=4
clothestype4= "T恤"
clothesprice4=600
clothesquan4=110
clothesnorm4="m"









print("---------------欢迎来到汤汤衣服商城-------------------")
print("编号    类型      价格      数量      规格")
print(clothesid1,"    ",clothestype1,"    ",clothesprice1,"    ",clothesquan1,"    ",clothesnorm1)
print(clothesid2,"    ",clothestype2,"    ",clothesprice2,"    ",clothesquan2,"    ",clothesnorm2)
print(clothesid3,"    ",clothestype3,"    ",clothesprice3,"    ",clothesquan3,"    ",clothesnorm3)
print(clothesid4,"    ",clothestype4,"    ",clothesprice4,"    ",clothesquan4,"    ",clothesnorm4)


print("--------------------------------------------------")

print("总金额:￥",(clothesprice1 * clothesquan1 + clothesprice2 * clothesquan2 + clothesprice3 * clothesquan3 + clothesprice4 * clothesquan4))
print(help("keywords"))

