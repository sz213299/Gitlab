import asyncio
import time


# 1  3 5 6 2 4
async def main():
    print("dunc----入  1")
    # 发送网络请求
    # 休眠一下，模拟网络请求
    await asyncio.sleep(2)  #
    print("func----出  2")


async def main1():
    print("dunc1----入  3")
    await asyncio.sleep(5)
    print("func1----出  4")


async def main2():
    print("dunc2----入   5")
    await asyncio.sleep(1)
    print("func2----出   6")


async def main3():
    print("我是main")
    # 创建三个协程对象
    f = main()
    f1 = main1()
    f2 = main2()
    # await  挂起  让函数运行的时候允许被挂起
    # 这样没法挂起  需要封装在一个列表中 同意进行操作
    list = []
    # 创建三个任务
    l = asyncio.create_task(f)
    l1 = asyncio.create_task(f1)
    l2 = asyncio.create_task(f2)

    list.append(l)
    list.append(l1)
    list.append(l2)
    # 统一进行挂起
    await asyncio.wait(list)
    print("哈哈哈哈哈哈")
    # await f
    # await f1
    # await f2
    print("结束")


if __name__ == "__main__":
    s = time.time()
    m = main3()
    asyncio.run(m)
    e = time.time()
    print(e - s)
