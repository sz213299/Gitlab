import asyncio
import os
import requests
import aiofiles
import aiohttp
from lxml import etree
import re


def get_info(url):
    html = requests.get(url)
    html.encoding = 'utf-8'  # 确保使用正确的编码
    text = html.text
    html.close()

    result = []
    tree = etree.HTML(text)
    # 获取书籍列表
    book_list = tree.xpath('//div[@class="book_list"]/li')
    for book in book_list:
        chapter = {}
        # 获取章节名称
        chapter_name = book.xpath('./a/text()')[0]

        # 获取链接
        chapter_hrefs = [book.xpath('./a/@href')[0]]
        chapter['chapter_name'] = chapter_name
        chapter['chapter_hrafs'] = chapter_hrefs
        result.append(chapter)
    return result


async def download(name, href):
    # 创建session
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(href) as resp:
                if resp.status == 200:
                    page_source = await resp.text(encoding='utf-8')
                    # 解析页面源代码
                    tree = etree.HTML(page_source)

                    # 获取文件名并清理非法字符
                    file_name_raw = tree.xpath('//div[@class="book-content"]//text()')[0]
                    # 去除非法字符并去掉空白符或换行符
                    file_name = re.sub(r'[\\/*?:"<>|\n\r]+', '', file_name_raw).strip()

                    # 获取文章内容
                    content = ''.join(tree.xpath('//div[@class="neirong"]//text()')).strip()

                    # 确保文件名合法
                    file_name = file_name.replace('/', '_').replace('\\', '_')

                    # 写入文件
                    async with aiofiles.open(f'{name}/{file_name}.txt', mode='w', encoding='utf-8') as f:
                        await f.write(content)
                    print(f"{file_name} 下载完成")
                else:
                    print(f"获取 {href} 时出现错误，状态码: {resp.status}")
        except Exception as e:
            print(f"下载 {href} 时发生错误: {e}")


async def download_chapter(name, hrefs):
    # 创建文件夹
    if not os.path.exists(name):
        os.makedirs(name)

    # 分配任务
    tasks = []
    for href in hrefs:
        # 创建任务
        t = download(name, href)
        tasks.append(t)

    await asyncio.gather(*tasks)


async def main():
    url = 'https://m.mingchaonaxieshier.com/'
    # 获取主页面内容，并将数据管理成一个超大列表
    chardet_info = get_info(url)

    # 遍历每个章节，执行下载任务
    tasks = []
    for chardet in chardet_info:
        chapter_hrefs = chardet['chapter_hrafs']
        chapter_name = chardet['chapter_name']
        tasks.append(download_chapter(chapter_name, chapter_hrefs))

    # 并发执行所有章节下载任务
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
