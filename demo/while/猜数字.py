'''
random.randint(start,and)
参数一个随机数，可以猜多次，知道猜对为止，给出提示
'''

import  random
x=random.randint(1,40)

# 循环猜多次
count=0
while True:
    guss=int(input('请输入一个一到50之间的数字'))
    count += 1
    if guss == x:
        if count ==1:
            print("去买彩票")
        elif count > 6:
            print("运气一般")
        else:
            print("还行")
        print("恭喜才对；")
        break
    elif guss > x:
        print("猜大了")
    else:
        print("猜小了")
print("你已经猜了%d :"%(count))

