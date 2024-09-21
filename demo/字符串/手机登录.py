flag = True
while flag:
    name = input('用户名/手机号')
    if name.islower() and not name[0].isdigit() and len(name) > 6:
        while True:
            password = input('请输入密码')
            if len(password) == 6 and password.isdigit():
                if name == 'sz213299' and password == '123456':
                    print('登录成功')
                    flag = False
                    break
                else:
                    print("用户名或者密码错误")
                    break
            else:
                print("密码必须是数字")
    else:
        print("用户名或手机号格式错误")
