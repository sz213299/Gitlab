import requests
from lxml import etree

# //div[@class="doulist-item"]//div[@class="title"]/a/@href
# //div[@class="doulist-item"]//div[@class="title"]/a/text()


url = 'https://www.douban.com/doulist/151387524/'

headers = {'User-Agent':
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'}

response = requests.get(url, headers=headers)

# 提取数据
etree = etree.HTML(response.text)

for i in etree.xpath('//div[@class="doulist-item"]//div[@class="title"]/a'):
    title = i.xpath('./text()')
    href = i.xpath('./@href')
    print(title)
    print(href)
