
for i in range(3):
    username = input("用户名")
    password = input("密码")
    if username == "admin" and password == "123456":
        print("登录成功")
        break
    print("账号或密码错误")
if i == 2:
    print("________________账号被锁定__________________")
'''
for i in range(3):
    username = input("用户名")
    password = input("密码")
    if username == "admin" and password == "123456":
        print("登录成功")
        break
    print("账号或密码错误")
else:
    print("________________账号被锁定__________________")


'''