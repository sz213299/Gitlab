'''
角色： 姓名，性别，年龄

添加，删除，修改，查找，显示所有角

退出

'''
list = []
import time

print('**********欢迎进入王者荣耀角色管理系统******************')
while True:
    con = input('\n 请选择功能：\n 1.添加角色 \n 2.删除角色 \n 3.修改角色 \n 4.查找角色 \n 5.显示所有角色 \n 6.退出系统 \n')
    if con == '1':
        print('添加角色模块:\n')
        name = input('角色名')
        sex = input('性别')
        job = input('职业')
        list.append([name,sex,job])
        print(f'成功添加{name}角色到系统')
    elif con == '2':
        print('删除角色模块')
        de_name = input('请输入你要删除的角色')
    #   查找角色是否存在
        for u in list:
            if u[0] == de_name:
                x = input("确定删除?(y)")
                if x=='y':
                    list.remove(u)
                    print(f'成功删除{de_name}角色')
                    break
        else:
            print(f'本系统不存在{de_name}角色')
    elif con == '3':
        print("修改角色模块")
        x_name = input('请输入你要修改的角色')
        for t in list:
            if t[0] == x_name:
                ty = input('\n请选择你要修改的信息  \n 1.角色名称 \n 2.角色性别 \n 3.角色职业')
                if ty == '1':
                    n_name = input('请输入修改后的名称')
                    t[0] = n_name
                    print('名称修改成功')
                if ty =='2':
                    n_sex = input('请输入修改后的性别')
                    t[1] = n_sex
                    print('性别修改成功')
                if ty == '3':
                    n_job = input('请输入修改后的职业')
                    t[2] = n_job
                    print('职业修改成功')
            print('修改完成')


    elif con == '4':
        print('查询角色模块')
        de_name = input('\t请输入你要查询的角色')
        #   查找角色是否存在
        for u in list:
            if u[0] == de_name:
                print('存在角色信息如下：')
                print(f'\t{u[0].ljust(10)}\t{u[1].ljust(10)}{u[2].ljust(10)}')
                break
        else:
            print(f'本系统不存在{de_name}角色')
        pass
    elif con == '5':
        print('显示所有角色的模块')
        print(f'{'名称'.center(10)}{'角色'.center(10)}{'职业'.center(10)}')
        for i in list:
            print(i[0].center(10),end='')
            print(i[1].center(10),end='')
            print(i[2].center(10),end='')
            print()
    elif con == '6':
        print("正在退出系统")
        time.sleep(4)
        print("退出成功")
    else:
        print("输入错误，请重新输入")
