import asyncio


async def func():
    print(123)


if __name__ == '__main__':
    f = func()
    # 方案二  时间循环关闭操作，容易和管理器相冲突
    asyncio.run(f)

#     方案一
'''
    # 协程函数想要运行 就必须这样做
    # 1. 创建协程对象
    print(f)
    # 2.必须有一个超大的event_looop ---> 事件循环
    event_loop = asyncio.get_event_loop()
    # 3.用 event_loop 运行协程对象，让协程中的对象可以执行，等待执行完毕
    event_loop.run_until_complete(f)


'''
