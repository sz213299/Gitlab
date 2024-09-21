import random

file = input("请输入文件全称")


if file.endswith('jpg') or file.endswith('jpeg') or file.endswith('png'):
    i = file.rfind('.')
    name = file[:i]


    if len(name) < 6:
        filename = ''
        s = 'dfytfcdudgcuygduycgue'


        for u in range(4):
            index = random.randint(0, len(s) - 1)
            filename += s[index]
        file = filename + file[i:]
    print(f'成功上传文件{file}')
else:
    print('格式错误，上传失败')
