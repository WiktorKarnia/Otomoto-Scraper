import scrapy
#from scrapy_selenium import SeleniumRequest
from ..items import OtomotoScraperItem


class OtomotoSpider(scrapy.Spider):
    name = 'otomoto' 
    start_urls = [
        "https://www.otomoto.pl/osobowe",
    ]

    
    def parse(self, response):
        
        n_pages = int(response.css('li[data-testid="pagination-list-item"] a span::text')[-1].extract())
        #n_pages = 10
        while n_pages > 1:
            home = self.start_urls[0]
            link = home + '?page='+ str(n_pages)
            print("@@@@@" + link + "@@@@@ - page " + str(n_pages))
            n_pages = n_pages - 1
            ##print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ - page " + str(n_pages))
            #yield response.follow(link, callback=self.parse)
            yield scrapy.Request(link, self.parse)
        
            all_articles = response.css('article[data-testid="listing-ad"]')
            #print(all_articles)
            for car in all_articles:
                if len(car.css('li::text').get())!=4 and car.css('li::text')[3].get() in ['Elektryczny', 'Electric']:
                    Year = 1
                    Mileage = 2
                    EngineCapacity = '0'
                    FuelType = 3
                
                elif car.css('li::text')[2].get() in ['Elektryczny', 'Electric']:
                    Year = 0
                    Mileage = 1
                    EngineCapacity = '0'
                    FuelType = 2
                    
                elif len(car.css('li::text').get())!=4:
                    Year = 1
                    Mileage = 2
                    EngineCapacity = car.css('li::text')[3].get()
                    FuelType = 4
                    
                else:
                    Year = 0
                    Mileage = 1
                    EngineCapacity = car.css('li::text')[2].get()
                    FuelType = 3
                    
                item = OtomotoScraperItem()
                item['id'] = car.css('article[id]::attr(id)').get()
                item['carname'] = car.css('h2[data-testid="ad-title"] a::text').get()
                item['price'] = car.css('span.ooa-1bmnxg7.e1p19lg711::text').get()
                item['year'] = car.css('li::text')[Year].get()
                item['km'] = car.css('li::text')[Mileage].get()
                item['capacity'] = EngineCapacity
                item['fuel_type'] = car.css('li::text')[FuelType].get()
                yield item