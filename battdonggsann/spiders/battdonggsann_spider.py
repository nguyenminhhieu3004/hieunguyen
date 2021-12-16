import scrapy


class BattdonggsannSpiderSpider(scrapy.Spider):
    name = 'battdonggsann_spider'
    allowed_domains = ['batdongsan.com.vn']
    start_urls = ['https://batdongsan.com.vn/nha-dat-ban-thua-thien-hue/']

    def parse(self, response):
        city = response.xpath('//a[@class,"href"]/text()').get()
        position = response.xpath('//div[@class,"<div class="re__sidebar-box re__product-count-box"]/text()').get()
        price = response.xpath('//div[@class="re__sidebar-box-content"]/text()').get()
        acreage = response.xpath('//div[@class="re__sidebar-box re__price-box"]/text()').get()
        item = BatdongsannItem()
        item["city"]= city
        item["position"]= position
        item["price"]= price
        item["acreage"]= acreage
        yield item
    




        pass
