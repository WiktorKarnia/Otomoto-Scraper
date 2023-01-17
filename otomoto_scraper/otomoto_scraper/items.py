# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class OtomotoScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    carname = scrapy.Field()
    price = scrapy.Field()
    year = scrapy.Field()
    km = scrapy.Field()
    capacity = scrapy.Field()
    fuel_type = scrapy.Field()
