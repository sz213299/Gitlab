import html
import os
import re

import requests
from lxml import etree

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "max-age=0",
    "Proxy-Connection": "keep-alive",
    "Referer": "http://ciyuandao.com/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
}
cookies = {
    "acw_tc": "b4a3921517286306163953503ee19de99c9afbbda3b67b2b4ec149c80b",
    ".ciyuandao.pass.antiforgery": "CfDJ8PaXm6KUSvRHhZel3GxIeRbvGekSMK3aDf3_Y3Qw-otMSYA-GLb2MxwS0BZGU7n9ws96PcZW1T49XBMwx_DbhQu9KKZLZdjryzBZnMpnTus9Px0heFS2T7pc8uFB0mTZy6031ZxN5x19PnvzwP07toM"
}
for i in range(1, 485):
    print(f'——————开始第{i}页————————')
    url = f"http://ciyuandao.com/photo/list/0-0-{i}"
    response = requests.get(url, headers=headers, verify=False)  # verify=False 跳过验证

    Html = response.text
    text = html.unescape(Html)

    old_title = re.findall('<title>(.*?) - 一站式coser成长平台|cos正片|cosplay图片|cos美图</title>', text)[0]

    title = re.sub(r'[\\/*?:"<>|]', "", old_title)

    res = etree.HTML(text)

    uls = res.xpath('//div[@class="pics"]/ul/li')
    num = 1
    dir_path = f'{title}_{i}'
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    for li in uls:
        name = li.xpath('.//p[1]/a/text()')[0]
        link = li.xpath('./a/img/@src')[0]
        # print(name, link, sep=' | ')
        img_src = requests.get(url=link, headers=headers, timeout=20).content
        file_path = os.path.join(dir_path, f'{name}_{num}.jpg')
        with open(file_path, mode='wb') as f:
            f.write(img_src)
            print(f'——————第{i}页，第{num}图片完成——————')
        num += 1
print("全部下载完毕")
