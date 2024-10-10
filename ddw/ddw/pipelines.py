# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import urllib.request


# useful for handling different item types with a single interface


class DdwPipeline:

    def open_spider(self, spider):
        self.fp = open('book.json', 'w', encoding='utf-8')

    # item就是yield传过来的对象
    def process_item(self, item, spider):
        # 字符串，a
        # with open('book.json','a',encoding='utf-8') as fp:
        #     fp.write(str(item))

        self.fp.write(str(item))
        return item

    def close_spider(self, spider):
        self.fp.close()


class DdwPipeline2:
    def process_item(self, item, spider):
        url = 'http:' + item['src']
        filename = './book/' + item['name'] + '.jpg'
        urllib.request.urlretrieve(url=url, filename=filename)

        return item
