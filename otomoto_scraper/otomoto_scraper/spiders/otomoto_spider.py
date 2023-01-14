import scrapy
from scrapy_selenium import SeleniumRequest

class OtomotoSpider(scrapy.Spider):

    name = 'otomoto'

    def start_requests(self):
        yield SeleniumRequest(
            url= 'https://www.otomoto.pl',
            wait_time=60,
            screenshot=True,
            callback=self.parse
        )

    def parse(self, response):
        title = response.css('title::text').extract()
        yield {'titletext' : title}



