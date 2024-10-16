from concurrent.futures import ThreadPoolExecutor


def download(name):
    for i in range(1000):
        print(name, i)
    # 下载图片


if __name__ == '__main__':
    # 准备好10个任务   2表示线程池个数、
    with ThreadPoolExecutor(2) as t:
        # 第一种方法
        # for i in range(10):
        #     job = f'任务{i}'
        #     t.submit(download, job)  # 第一个参数表示任务，后面的参数表示任务的执行信息
        #     第二种方法
        t.map(download, ['任务'])
    print("我是猪现场")
