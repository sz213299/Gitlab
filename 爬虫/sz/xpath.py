#1.lxml 模块
# pip list lxml     库 etree 转换为element对象

from lxml import etree
text='''

<div class="s-hotsearch-title"><a class="hot-title" href="https://top.baidu.com/board?platform=pc&amp;sa=pcindex_entry" target="_blank"><div class="title-text c-font-medium c-color-t" aria-label="百度热搜"><i class="c-icon"></i><i class="c-icon arrow"></i></div></a><a id="hotsearch-refresh-btn" class="hot-refresh c-font-normal c-color-gray2"><i class="c-icon refresh-icon"></i><span class="hot-refresh-text">换一换</span></a></div>
'''
html=etree.HTML(text)
# print(html)
print(html.xpath('//div[@class="s-hotsearch-title"]/a/@href'))
