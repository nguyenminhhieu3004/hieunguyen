import scrapy


class Battdonggsannspider1Spider(scrapy.Spider):
    name = 'battdonggsannspider1'
    allowed_domains = ['batdongsan.com.vn']
    start_urls = ['http://batdongsan.com.vn/']

    def parse(self, response):
        pass
