msg = input('发表一句话:')

print('-'*50)
print('以下为回复内容:')

while True:
    username = input('用户名')
    while True:
        coumment = input('评论')
        coumment.strip()
        if len(coumment)!=0:
            if len(coumment) <=20:
                coumment = coumment.replace('傻逼','**')
                print(f'{username}发表的的评论是 :{coumment}')
                break
            else:

                print('长度不能超过20！')

    else:
        print('评论不能为空')