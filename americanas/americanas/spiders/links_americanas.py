from ast import IsNot
import scrapy
import pandas as pd
from americanas.items_links import LinksItem
import re
from scraper_api import ScraperAPIClient
# import Selector

# client = ScraperAPIClient('15158d4674ce528e593a775a4b90dcc9') #--> primeiro -> conta: Mari
#client = ScraperAPIClient('39e2ae4a508557b0b178342d1664d3fd')
client = ScraperAPIClient('1f24a49c4c9e3c0821691a5cbba13f51') #--> conta: lai
#client = ScraperAPIClient('4ee9c4689f503403d26167ad815beca3') #Lucas 

class LinksAmericanasSpider(scrapy.Spider):

    name = 'links_americanas'

    def start_requests(self):

        # self.load_links()
        lista_links  = []
        
        for paginacao in range(0, 67): #84
            
            
            #url = f"https://www.americanas.com.br/categoria/tv-e-home-theater/tv?viewMode=list&sortBy=higherPrice&limit=24&offset={paginacao*24}" # TV
            #url = f"https://www.americanas.com.br/categoria/eletrodomesticos/fogao/g/tipo-de-produto-Cooktop/tipo-de-produto-Fogareiro/tipo-de-produto-Fog%C3%A3o/tipo-de-produto-Fog%C3%A3o%20Piso/tipo-de-produto-Forno?chave=prf_hi_dm2_at_1_00_fog&viewMode=list&limit=24&offset={paginacao*24}" # fogão
            #url = f"https://www.americanas.com.br/categoria/eletrodomesticos/geladeira-refrigerador/g/tipo-de-produto-Freezer/tipo-de-produto-Frigobar/tipo-de-produto-Geladeira/tipo-de-produto-Refrigerador?chave=prf_hi_dm2_at_1_00_gel&viewMode=list&limit=24&offset={paginacao*24}" # geladeira
            #url = f"https://www.americanas.com.br/categoria/informatica/notebooks?viewMode=list&limit=24&offset={paginacao*24}" #notebook
            #url = f"https://www.americanas.com.br/categoria/celulares-e-smartphones/smartphone?viewMode=list&limit=24&offset={paginacao*24}" #celular
            url = f"https://www.americanas.com.br/categoria/celulares-e-smartphones/smartphone/g/tipo-de-produto-Smartphone?viewMode=list&sortBy=higherPrice&limit=24&offset={paginacao*24}"

            lista_links.append(url)


        return [scrapy.Request(client.scrapyGet(url = url), callback = self.parse,  meta={'url': url}) for url in lista_links]
        # return [scrapy.Request(url = url, callback = self.parse, meta = {'url': url}) for url in urls]


    def parse(self, response):
        print("URL: {}".format(response.meta.get('url')))
        items = LinksItem()
        
        for registro in response.selector.xpath(f'//div[@class="src__Wrapper-sc-1wgxjb2-0 dUUAKQ"]/a/@href'): 
            print(registro.extract()) #.get()
                
            items['links'] = f"https://www.americanas.com.br{registro.extract()}" if registro.extract() is not None else ""
            yield items
                
    
        

