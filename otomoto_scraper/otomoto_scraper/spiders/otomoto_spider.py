import scrapy
from scrapy_selenium import SeleniumRequest

class OtomotoSpider(scrapy.Spider):
    name = 'otomoto' 
    start_urls = [
        'https://www.otomoto.pl/osobowe?search%5Bfilter_enum_fuel_type%5D=electric',
        "https://www.otomoto.pl/osobowe?page=1",
        #"https://www.otomoto.pl/osobowe?page=2",
        #"https://www.otomoto.pl/osobowe?page=3",
        #"https://www.otomoto.pl/osobowe?page=4",
        #"https://www.otomoto.pl/osobowe?page=5",
        #"https://www.otomoto.pl/osobowe?page=6",
        #"https://www.otomoto.pl/osobowe?page=7",
        #"https://www.otomoto.pl/osobowe?page=8",
        #"https://www.otomoto.pl/osobowe?page=9",
        #"https://www.otomoto.pl/osobowe?page=10",
        #"https://www.otomoto.pl/osobowe?page=11",
        #"https://www.otomoto.pl/osobowe?page=12",
        #"https://www.otomoto.pl/osobowe?page=13",
        #"https://www.otomoto.pl/osobowe?page=14",
        #"https://www.otomoto.pl/osobowe?page=15",
    ]
    
    def parse(self, response):
        all_articles = response.css('article.ooa-1txt27o.e1b25f6f0, article.ooa-op4lyf.e1b25f6f0')
        for car in all_articles:
            if car.css('li.ooa-1k7nwcr.e1teo0cs0::text')[2].get() in ['Elektryczny', 'Electric']:
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
                
            yield {
                    'carname' : car.css('h2.e1b25f6f6.e1b25f6f20.ooa-10p8u4x.er34gjf0 a::text').get(),
                    'price' : car.css('span.ooa-1bmnxg7.e1b25f6f11::text').get(),
                    'year' : car.css('li.ooa-1k7nwcr.e1teo0cs0::text')[Year].get(),
                    'km' : car.css('li.ooa-1k7nwcr.e1teo0cs0::text')[Mileage].get(),
                    'capacity' : EngineCapacity,
                    'fuel type' : car.css('li.ooa-1k7nwcr.e1teo0cs0::text')[FuelType].get()
                   }