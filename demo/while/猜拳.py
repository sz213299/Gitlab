import random
n = 1
p_count = 0
c_count = 0
while n <= 3:
    n += 1

    ran1 = random.randint(0,2)
    gu = int(input("请输入：剪刀（0） 石头（1） 布（2）\n"))
    if gu == 0 and ran1 == 2 or gu == 1 and ran1 == 2 or gu == 2 and ran1 == 1 :
        print("你赢")
        p_count += 1
    elif (ran1 == 0 and gu == 2) or (ran1 == 1 and gu == 2) or (ran1 == 2 and gu == 1) :
        c_count += 1
        print("电脑赢")
    else:
        print("平局")

if p_count > c_count:
    print("最终你赢")
elif p_count < c_count:
    print("最终你输")
else:
    print("最终平局")
