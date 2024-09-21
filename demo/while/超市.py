total=0
numbers = 0
while True:
    price=float(input("请输入你的价格 :"))
    num=int(input("请输入数量 :"))
    total += price * num
    numbers +=num

    answer = input('当前商品的总价格 : %.2f, 是否继续添加商品（q表示退出 ？）'%(total))
    if answer=='q':
        break
    print('商品数量：%d,总营业额%d'%(numbers,total))


