import scrapy


class CarSpider(scrapy.Spider):
    name = "car"
    allowed_domains = ["www.autohome.com.cn"]
    start_urls = ["https://www.autohome.com.cn/price/"]

    def parse(self, response):
        print("======================================")
        price_list = response.xpath('//div[@class="tw-mt-1 tw-px-4"]/p/text()')
        name_list = response.xpath('//div[@class="tw-mt-1 tw-px-4"]/a/text()')
        image_list = response.xpath('//div[@class="tw-h-40 tw-origin-bottom tw-scale-[0.9] tw-overflow-hidden tw-px-4 tw-transition-all tw-duration-300 tw-ease-in-out group-hover:tw-origin-bottom group-hover:tw-scale-[1]"]/img/@src')
        for i in range(len(price_list)):
            price = price_list[i].extract()
            name = name_list[i].extract()
            image = image_list[i].extract()
            print(name, price,image)
