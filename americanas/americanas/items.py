# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmericanasItem(scrapy.Item):
    # define the fields for your item here like:
    titulo = scrapy.Field()
    ean = scrapy.Field()
    url = scrapy.Field()
    descricao = scrapy.Field()
    preco = scrapy.Field()
    categoria = scrapy.Field()