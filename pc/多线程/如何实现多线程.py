# 倒包
from threading import Thread


# 第一种写法
# def download(url):
#     #     想象一下这里是下载图片的代码
#     for i in range(1000):
#         print(url, i)
#
#
# if __name__ == '__main__':
#     t1 = Thread(target=download, args=('链接',))
#     t2 = Thread(target=download, args=('佩奇',))
#     t1.start()
#     t2.start()

#  定好任务
# def func():
#     for i in range(1000):
#         print("我的任务是", i)
#
#
# # 编写mian   if __name__ == '__main__':
#
# if __name__ == '__main__':
#     #  创建一个线程 t=Thread(),不会直接执行，需要调度
#     t = Thread(target=func)  # target任务
#     #     调度线程执行
#     t.start()  # 在这里才真正的告诉线程开始执行
#
#     #     主线程应该可以继续往下走
#     for j in range(1000):
#         print("我是店长", j)

# 面向对象的写法

class MyThread(Thread):  # 可以创建子线程

    def __init__(self, name):
        super(MyThread, self).__init__()
        self.name = name  # self 是和线程变化的保持一致

    def run(self):  # run 任务
        print('我是run', self.name)
        # for i in range(10):
        #     print('子线程', i)


if __name__ == '__main__':
    t = MyThread('涨价龙')  # 创建一个子线程
    t.start()  # 线程开启  -》 自动会让子线程执行run 功能

    t1 = MyThread('始祖名')
    t1.start()
    # for j in range(10):
    #     print('我是主线程', j)
