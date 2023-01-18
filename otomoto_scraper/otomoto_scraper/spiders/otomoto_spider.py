import scrapy
#from scrapy_selenium import SeleniumRequest
from ..items import OtomotoScraperItem


class OtomotoSpider(scrapy.Spider):
    name = 'otomoto' 
    start_urls = [
        "https://www.otomoto.pl/osobowe",
    ]

    
    def parse(self, response):
        
        #n_pages = int(response.css("li.pagination-item.ooa-1xgr17q a span::text")[-1].extract())
        n_pages = 4
        while n_pages >= 2:
            home = self.start_urls[0]
            link = home + '?page='+ str(n_pages)
            #print("@@@@@" + link + "@@@@@ - page " + str(n_pages))
            n_pages = n_pages - 1
            ##print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ - page " + str(n_pages))
            #yield response.follow(link, callback=self.parse)
            yield scrapy.Request(link, self.parse)
        
        all_articles = response.css('article.ooa-1txt27o.e1b25f6f0, article.ooa-op4lyf.e1b25f6f0, article.ooa-1wl9plw.e1b25f6f0')
        for car in all_articles:
            if len(car.css('li.ooa-1k7nwcr.e1teo0cs0::text').get())!=4 and car.css('li.ooa-1k7nwcr.e1teo0cs0::text')[3].get() in ['Elektryczny', 'Electric']:
                Year = 1
                Mileage = 2
                EngineCapacity = '0'
                FuelType = 3
            
            elif car.css('li.ooa-1k7nwcr.e1teo0cs0::text')[2].get() in ['Elektryczny', 'Electric']:
                Year = 0
                Mileage = 1
                EngineCapacity = '0'
                FuelType = 2
                
            elif len(car.css('li.ooa-1k7nwcr.e1teo0cs0::text').get())!=4:
                Year = 1
                Mileage = 2
                EngineCapacity = car.css('li.ooa-1k7nwcr.e1teo0cs0::text')[3].get()
                FuelType = 4
                
            else:
                Year = 0
                Mileage = 1
                EngineCapacity = car.css('li.ooa-1k7nwcr.e1teo0cs0::text')[2].get()
                FuelType = 3
                
            item = OtomotoScraperItem()
            item['id'] = car.css('article.ooa-1txt27o.e1b25f6f0::attr(id), article.ooa-op4lyf.e1b25f6f0::attr(id), article.ooa-1wl9plw.e1b25f6f0::attr(id)').get()
            item['carname'] = car.css('h2.e1b25f6f6.e1b25f6f20.ooa-10p8u4x.er34gjf0 a::text').get()
            item['price'] = car.css('span.ooa-1bmnxg7.e1b25f6f11::text').get()
            item['year'] = car.css('li.ooa-1k7nwcr.e1teo0cs0::text')[Year].get()
            item['km'] = car.css('li.ooa-1k7nwcr.e1teo0cs0::text')[Mileage].get()
            item['capacity'] = EngineCapacity
            item['fuel_type'] = car.css('li.ooa-1k7nwcr.e1teo0cs0::text')[FuelType].get()
            yield item