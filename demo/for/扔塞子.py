'''
有金币才能玩游戏，不然玩不了

10元20个金币 必须是10的倍数

玩游戏赠送金币1

无论输赢消耗金币5个

猜大小：猜对  鼓励金币2个·  猜错没有金币   超出6点以上就是大，否则就是小

游戏结束 1，主动退出 2 没有金币退出

退出打印 你剩余的金币数，共玩了几局

'''
import  random
count = 0 #金币数
num = 0
if count < 5:
    # count += 1
    print('余额不足，请充值')
    while True:
        money = int(input('请输入充值金额 : '))
        if money % 10 == 0 :
            count += money * 2
            print(f'充值成功!,当前金币剩余{count}个')
        #     开启游戏
            print('*********开始你的游戏之旅************')
            answer = input('是否开始玩游戏(Y?N)')

            while count > 5 and answer == 'Y' :
            #     扣金币
                count -= 5
            # 赠送金币
                count += 1
            # 游戏逻辑
                ran1 = random.randint(1,6)
                ran2 = random.randint(1,6)
                giss = input('洗牌完毕，请开始猜大小')
                if giss == '大' and ran1 + ran2 >= 6 or giss == '小' and ran1 + ran2  <=6 :
                    print('恭喜你猜对了')
                    count +=2
                else:
                    print('很遗憾你猜错了')
                num += 1 #计算玩的次数
                answer = input('是否继续玩游戏(Y?N)')
                print(f'第{num}局,剩余{count}个金币')
            print(f'共玩了{num}次,剩余{count}个金币')
            print("**************欢迎下次再来***************")
            break
        else:
            print('不是10的倍数，充值失败')


