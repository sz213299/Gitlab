import requests
from lxml import etree

from concurrent.futures import ThreadPoolExecutor


def get_html(url):
    res = requests.get(url)
    pg = res.text
    res.close()
    return pg


def get_data(html):
    text = etree.HTML(html)
    # 列表
    tr_list = text.xpath('//table[@align="center"]//tr')[:-2]
    for tr in tr_list:
        pm = tr.xpath('./td[1]/text()')[0] if tr.xpath('./td[1]/text()') else (
            tr.xpath('./th[1]//text()')[0] if tr.xpath('./th[1]//text()') else None)
        year = tr.xpath('./td[2]//text()')[0] if tr.xpath('./td[2]//text()') else (
            tr.xpath('./th[2]//text()')[0] if tr.xpath('./th[2]//text()') else None)
        name = tr.xpath('./td[3]//text()')[0] if tr.xpath('./td[3]//text()') else (
            tr.xpath('./th[3]//text()')[0] if tr.xpath('./th[3]//text()') else None)
        num = tr.xpath('./td[4]/text()')[0] if tr.xpath('./td[4]//text()') else (
            tr.xpath('./th[4]//text()')[0] if tr.xpath('./th[4]//text()') else None)

        # print(pm, year, name, num)
        f.write(", ".join([pm, year, name, num]) + '\n')


def mian(url):
    # url = 'http://www.boxofficecn.com/boxoffice2023'
    # 获取源代码
    html = get_html(url)
    # 解析数据,直接存储在文件中
    get_data(html)


if __name__ == '__main__':
    f = open("data.json", "w", encoding="utf-8")
    lst = []
    for i in range(1994, 2025):
        lst.append(f'http://www.boxofficecn.com/boxoffice{i}')
    # print(lst)

    #     单线程逻辑
    #     for url in lst:
    #         mian(url)
    # 多线程逻辑
    with ThreadPoolExecutor(10) as t:
        for url in lst:
            print(f"正在下载这个{url}数据")
            t.submit(mian, url)
            print(f"这个{url}数据下载完成")
        print("全部完成")
