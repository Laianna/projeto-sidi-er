from ast import IsNot
import scrapy
import pandas as pd
from americanas.items_links import LinksItem
import re
from scraper_api import ScraperAPIClient
# import Selector

# client = ScraperAPIClient('15158d4674ce528e593a775a4b90dcc9') #--> primeiro -> conta: Mari
client = ScraperAPIClient('39e2ae4a508557b0b178342d1664d3fd')
# client = ScraperAPIClient('1f24a49c4c9e3c0821691a5cbba13f51') #--> conta: lai

class LinksAmericanasSpider(scrapy.Spider):

    name = 'links_americanas'

    def start_requests(self):

        # self.load_links()
        lista_links  = []
        
        for paginacao in range(1, 84):
            
            url = f"https://www.americanas.com.br/categoria/informatica/notebooks?viewMode=list&limit=24&offset={paginacao*24}"
            #url = f"https://www.americanas.com.br/categoria/celulares-e-smartphones/smartphone?viewMode=list&limit=24&offset={paginacao*24}"

            lista_links.append(url)


        return [scrapy.Request(client.scrapyGet(url = url), callback = self.parse,  meta={'url': url}) for url in lista_links]
        # return [scrapy.Request(url = url, callback = self.parse, meta = {'url': url}) for url in urls]


    def parse(self, response):
        print("URL: {}".format(response.meta.get('url')))
        items = LinksItem()
        
        for i in range(1, 25):
            #print(f"{i}")
            for registro in response.selector.xpath(f'//*[@id="rsyswpsdk"]/div/main/div/div[3]/div[2]/div[{i}]/div/a/@href'): 
                #print(registro.extract()) #.get()
                
                items['links'] = registro.extract() if registro.extract() is not None else ""
                yield items
        

