from lxml import etree
import requests

# https://www.douban.com/doulist/151387524/?start=25&sort=seq&playable=0&sub_type=
# https://www.douban.com/doulist/151387524/?start=50&sort=seq&playable=0&sub_type=
url = 'https://movie.douban.com/top250'

headers = {'User-Agent':
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'}

for i in range(4):
    params = {
        'start': i * 25
    }
    response = requests.get(url, headers=headers, params=params)
    tree = etree.HTML(response.text)

    title = tree.xpath('//div[@class="hd"]/a/span[1]/text()')
    # href = tree.xpath('//div[@class="doulist-item"]//div[@class="title"]/a/@href')
    with open('dd.txt', 'a+', encoding='utf') as f:
        f.write(str(title)+'\n')
