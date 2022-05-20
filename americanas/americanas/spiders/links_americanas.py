from ast import IsNot
import scrapy
import pandas as pd
from americanas.items_links import LinksItem
import re
from scraper_api import ScraperAPIClient
# import Selector

client = ScraperAPIClient('15158d4674ce528e593a775a4b90dcc9') #--> primeiro -> conta: Mari
#client = ScraperAPIClient('39e2ae4a508557b0b178342d1664d3fd')

class ProductAmazonSpider(scrapy.Spider):

    name = 'article'

    def start_requests(self):

        # self.load_links()
        lista_links  = []
        
        for paginacao in range(1, 84):
            
            url = f"https://www.americanas.com.br/categoria/informatica/notebooks?viewMode=list&limit=24&offset={paginacao*24}"
            #url = f"https://www.americanas.com.br/categoria/celulares-e-smartphones/smartphone?viewMode=list&limit=24&offset={paginacao*24}"

            lista_links.append(url)
        
        # urls = self.lista_links
        #urls = ["https://www.amazon.com.br/Notebook-Samsung-256GB-Windows-Chumbo/dp/B09N41J9K1/"]
        #urls = ["https://www.amazon.com.br/Mouse-Pad-Gaming-Havit-HV-MP830/dp/B0152HPXXE/"]
        
        print(lista_links)
        print(f"TAMANHO:>>>>>>>>>>>>{len(lista_links)}")

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
        


        
        '''print("###########################################################################")
        print("URL: {}".format(url))
        print("Meta URL: {}".format(url_meta))
        print("Titulo: {}".format(titulo))
        print("EAN: {}".format(ean))
        print("Descricao: {}".format(descricao))
        print("Preco: {}".format(preco))
        print("Categoria: {}".format(categoria))
        print("###########################################################################")'''
        

        # items['titulo'] = titulo[0].strip() if len(titulo) != 0 else ""
        # items['ean'] = ean[0] if len(ean) != 0 else ""
        # items['url'] = url_meta
        # items['descricao'] = descricao[0] if len(descricao) != 0 else ""
        # items['preco'] = preco if preco is not None else ""
        # items['categoria'] = categoria if categoria is not None else ""

        # yield items