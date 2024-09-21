
con = []  # 购物车
flag = True
while flag:

    # 添加商品
    name = input("商品名称")
    price = float(input("商品价格"))
    number = input("商品数量")
    goods = [name, price, number]
    # 添加到车里面
    con.append(goods)
    answer = input("是否继续添加(按q键退出)")
    if answer.lower() == "q":
        flag = False
print('名称\t价格\t数量\t')
for  i in con:
    print(f'{i[0]}\t{i[1]}\t{i[2]}')

