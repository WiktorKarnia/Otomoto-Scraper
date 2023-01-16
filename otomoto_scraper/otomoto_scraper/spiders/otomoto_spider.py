import scrapy
from scrapy_selenium import SeleniumRequest

class OtomotoSpider(scrapy.Spider):

    #def generate_urls(url, pages):
    #    urls = []
    #    for page in range(pages):
    #         urls.append(url + str(pages))
    #    return urls
#
    name = 'otomoto' 
    #start_urls = generate_urls("https://www.otomoto.pl/osobowe?page=" , 10)
    start_urls = [
        "https://www.otomoto.pl/osobowe?page=1",
        "https://www.otomoto.pl/osobowe?page=2",
        "https://www.otomoto.pl/osobowe?page=3",
        "https://www.otomoto.pl/osobowe?page=4",
        "https://www.otomoto.pl/osobowe?page=5",
        "https://www.otomoto.pl/osobowe?page=6",
        "https://www.otomoto.pl/osobowe?page=7",
        "https://www.otomoto.pl/osobowe?page=8",
        "https://www.otomoto.pl/osobowe?page=9",
        "https://www.otomoto.pl/osobowe?page=10",
        "https://www.otomoto.pl/osobowe?page=11",
        "https://www.otomoto.pl/osobowe?page=12",
        "https://www.otomoto.pl/osobowe?page=13",
        "https://www.otomoto.pl/osobowe?page=14",
        "https://www.otomoto.pl/osobowe?page=15",
    ]
    
    def parse(self, response):
        all_articles = response.css('article.ooa-1txt27o.e1b25f6f0, article.ooa-op4lyf.e1b25f6f0')
        for car in all_articles:
            if len(car.css('li.ooa-1k7nwcr.e1teo0cs0::text').get())!=4:
                yield {
                    'len' : len(car.css('li.ooa-1k7nwcr.e1teo0cs0::text').get()),
                    'carname' : car.css('h2.e1b25f6f6.e1b25f6f20.ooa-10p8u4x.er34gjf0 a::text').get(),
                    'price' : car.css('span.ooa-1bmnxg7.e1b25f6f11::text').get(),
                    'rok' : car.css('li.ooa-1k7nwcr.e1teo0cs0::text')[1].get(),
                    'km' : car.css('li.ooa-1k7nwcr.e1teo0cs0::text')[2].get(),
                    'pojemność' : car.css('li.ooa-1k7nwcr.e1teo0cs0::text')[3].get(),
                    'typ paliwa' : car.css('li.ooa-1k7nwcr.e1teo0cs0::text')[4].get() 
                   }
            else:
                yield {
                    'len' : len(car.css('li.ooa-1k7nwcr.e1teo0cs0::text').get()),
                    'carname' : car.css('h2.e1b25f6f6.e1b25f6f20.ooa-10p8u4x.er34gjf0 a::text').get(),
                    'price' : car.css('span.ooa-1bmnxg7.e1b25f6f11::text').get(),
                    'rok' : car.css('li.ooa-1k7nwcr.e1teo0cs0::text')[0].get(),
                    'km' : car.css('li.ooa-1k7nwcr.e1teo0cs0::text')[1].get(),
                    'pojemność' : car.css('li.ooa-1k7nwcr.e1teo0cs0::text')[2].get(),
                    'typ paliwa' : car.css('li.ooa-1k7nwcr.e1teo0cs0::text')[3].get() 
                    }


