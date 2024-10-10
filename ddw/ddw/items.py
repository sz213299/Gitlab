# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DdwItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 下载的路径
    name=scrapy.Field()
    price=scrapy.Field()
    src=scrapy.Field()
    link=scrapy.Field()
