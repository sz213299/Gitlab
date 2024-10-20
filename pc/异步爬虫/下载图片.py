import asyncio


async def download(url):
    print('我要开始下载了')

    await asyncio.sleep(3)

    print('下载成功')


async def main():
    # 想办法从网站里面拿到一堆url
    urls = ['11', '23', '44', '55', '66', '77', '88', '99']
    lists = []
    for url in urls:
        t = asyncio.create_task(download(url))  # 创建一个任务，任务里面是一个协程对象，该协程对象指向的是某一个url
        lists.append(t)

    await asyncio.wait(lists)


if __name__ == '__main__':
    f = main()
    asyncio.run(f)
