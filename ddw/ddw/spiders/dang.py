import scrapy

from ddw.items import DdwItem


class DangSpider(scrapy.Spider):
    name = "dang"
    allowed_domains = ["category.dangdang.com"]
    start_urls = ["https://category.dangdang.com/-cp01.17.00.00.00.00.html"]
    page = 1

    def parse(self, response):

        print("+++++++++++++++++++++++++")
        li_list = response.xpath('//ul[@id="component_59"]/li')
        for li in li_list:
            src_i = li.xpath('.//img/@src').extract_first()
            name = li.xpath('.//img/@alt').extract_first()
            price = li.xpath('.//p[@class="price"]/span[1]/text()').extract_first()
            src_de = li.xpath('.//img/@data-original').extract_first()
            if src_de:
                src = src_de
            else:
                src = src_i
            book = DdwItem(src=src, name=name, price=price)
            yield book
        if self.page < 100:
            self.page += 1
            url = f'https://category.dangdang.com/pg{self.page}-cp01.17.00.00.00.00.html'
            yield scrapy.Request(url=url, callback=self.parse)

# https://category.dangdang.com/pg2-cp01.17.00.00.00.00.html
# https://category.dangdang.com/pg3-cp01.17.00.00.00.00.html
