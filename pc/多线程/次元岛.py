import httpx
from lxml import etree
from urllib.parse import urljoin
import os
import re
import time
import random
from concurrent.futures import ThreadPoolExecutor

# HTTP请求的头部信息
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "max-age=0",
    "Proxy-Connection": "keep-alive",
    "Referer": "http://ciyuandao.com/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
}

# Cookies
cookies = {
    ".ciyuandao.pass.antiforgery": "CfDJ8MZQFyUZy1lMgDZIIjMWjYOfKRN7TzeOaVjRM32fIPCRby-eYMSXhYlT0nY-xDNbOeuUAa6ywDummoKTuws3rjkE-MLeCDfclubdu48ipjH5Fw1A5jhkXhG3PmPj7t7J07gSESecj7_hn94i4bPHHVs",
    "acw_tc": "b4a3921e17290514213332765e51c3b8c4ee7359b5c675897c7177770b"
}


# 发送请求
def get_html(url):
    try:
        res = httpx.get(url, headers=headers, cookies=cookies, timeout=15)  # 添加headers和cookies
        if res.status_code == 200:
            return res.text
        else:
            print(f"获取网页 {url} 失败，状态码：{res.status_code}")
            return None
    except Exception as e:
        print(f"请求 {url} 时出现错误: {e}")
        return None


# 解析数据
def data_list(html):
    tree = etree.HTML(html)
    list_data = tree.xpath('//div[@class="pics"]/ul/li')
    result = []
    for data in list_data:
        try:
            link = data.xpath('./a/@href')[0]
            link = urljoin('http://ciyuandao.com', link)
            mingzi = data.xpath('.//a[@class="fleft blue line"]/text()')[0]
            result.append((link, mingzi))
        except IndexError:
            print("无法提取详情页链接或名字")
    return result


# 下载图片
def download_images(image_links, name):
    for i, img_link in enumerate(image_links, start=1):
        try:
            img_res = httpx.get(img_link, headers=headers, cookies=cookies, timeout=30)  # 添加headers和cookies
            if img_res.status_code == 200:
                file_name = os.path.join(name, f'{name}_{i}.jpg')
                with open(file_name, 'wb') as fp:
                    fp.write(img_res.content)
                print(f"保存图片: {file_name}")
            else:
                print(f"图片下载失败，状态码：{img_res.status_code}，链接：{img_link}")
        except Exception as e:
            print(f"下载图片时发生未知错误: {e}")


# 下载页面
def download(link, mingzi, retries=3):
    print(f"开始下载: {mingzi} - {link}")
    try_count = 0
    while try_count < retries:
        try:
            res = httpx.get(link, headers=headers, cookies=cookies, timeout=30)  # 添加headers和cookies
            if res.status_code == 200:
                text = res.text
                tt = etree.HTML(text)
                name = tt.xpath('//title/text()')[0]  # 标题名字
                mingzi = re.sub(r'[\\/*?:"<>|]', "", name)
                dir_path = f'{mingzi}'
                if not os.path.exists(dir_path):
                    os.makedirs(dir_path)

                # 收集图片链接
                image_links = tt.xpath('//div[@class="talk_pic hauto"]/p//img/@src')

                # 下载所有图片
                download_images(image_links, dir_path)
                return  # 成功下载后直接返回
            else:
                print(f"详情页 {link} 获取失败，状态码：{res.status_code}")
                return  # 如果获取失败，直接返回
        except Exception as e:
            try_count += 1
            print(f"下载 {link} 时出现错误: {e}，重试第 {try_count} 次")
            time.sleep(random.uniform(2, 5))  # 随机等待2到5秒
        if try_count >= retries:
            print(f"下载 {link} 失败，超过最大重试次数")


# 主函数
def main(url):
    html = get_html(url)
    if html:
        data = data_list(html)
        for link, mingzi in data:
            download(link, mingzi)


# 启动
if __name__ == '__main__':
    lst = [f'http://ciyuandao.com/photo/list/2-0-{i}' for i in range(1, 47)]
    with ThreadPoolExecutor(max_workers=5) as executor:  # 减少并发量
        futures = [executor.submit(main, url) for url in lst]
        for future in futures:
            future.result()  # 等待所有任务完成
    print("全部完成")
