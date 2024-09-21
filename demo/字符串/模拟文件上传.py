import random
file = input("请输入文件全称")
if file.endswith('jpg') or file.endswith('jpeg') or file.endswith('png'):
    i = file.rfind('.')
    name = file[:i]
    print(name)
    if len(name) < 6:
        n = random.randint(100000,789808)
        new_name = str(n) + file[i:]
        print(new_name)
    print('成功上传文件')
else:
    print('格式错误，上传失败')