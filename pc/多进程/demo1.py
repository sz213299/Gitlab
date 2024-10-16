from multiprocessing import Process  # 多进程


def func():
    for i in range(100):
        print("我是子进程", i)


if __name__ == '__main__':
    # 创建子进程
    P = Process(target=func, args=())

    # 启动这个进程
    P.start()
    for i in range(100):
        print('我是猪进程', i)

'''
多线程： 任务之间的相似度非常高


多进程： 任务之间的相似度很低，关联性也相对较低



'''
