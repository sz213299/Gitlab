books = [
    {"name": "红楼梦","price": 45.00,"author": "曹雪芹","number": 100},
    {"name": "西游记","price": 40.00,"author": "吴承恩","number": 120},
    {"name": "水浒传","price": 38.00,"author": "施耐庵","number": 90},
    {"name": "三国演义","price": 50.00,"author": "罗贯中","number": 80}
]
book =[]
flag =True
while flag:
    print('*********欢迎来到图书馆************')
    con = input('请选择你的操作 \n 1.借书 \n 2.还书 \n 3.查询你要查找的图书 \n 4.显示所有的图书 \n 5.退出')
    if con == '1':
        text = input('请输入你先要借阅图书的名称')
        for item in books:
            if text == item.get('name'):
                count=item.get('number')
                count-=1
                # 数量减一个后，重新复制给number
                item['number'] = count

                print(f'{text}这本书还剩余{count}本')
                print(f'{text}这本书借阅成功，记得按时归还')
                break
        else:
            print('不存在该书，请重新输入')

    elif con == '2':
        text = input('请输入归还书籍的名称')
        for item in books:
            if text == item.get('name'):
                count=item.get('number')
                count+=1
                # 数量减一个后，重新复制给number
                item['number'] = count
                print(f'{text}这本书还剩余{count}本')
                print(f'{text}这本书归还成功')
                break
        else:
            print('不存在该书，请重新输入')

        pass
    elif con == '3':
        text = input('请输入你要查找的图书名称')
        for item in books:
            if text == item.get('name'):
                print(item)
        pass
    elif con == '4':
        print('书名'.center(10), '价格'.center(10), '作者'.center(10), '数量'.center(10))
        for item in books:
            if item.get('name'):
                print(item['name'].center(10),str(item.get('price')).center(10),item['author'].center(10),str(item['number']).center(10))
                # continue

    elif con == '5':
        print('***********退出成功,欢迎下次光临**********')
        break
