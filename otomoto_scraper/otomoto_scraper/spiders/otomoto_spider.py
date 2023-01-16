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
        button = response.webdriver.find_element_by_xpath('//*[@id="__next"]/div/div/div/main/div[1]/article/fieldset/div/form/div[2]/button[2]')
        button.click()
        title = response.css('title::text').extract()
        yield {'titletext' : title}



