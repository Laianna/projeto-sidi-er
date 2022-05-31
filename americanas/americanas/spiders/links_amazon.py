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

class LinksAmazonSpider(scrapy.Spider):

    name = 'links_amazon'

    def start_requests(self):

        # self.load_links()
        lista_links  = []
        
        for paginacao in range(1, 13):
            
            
            #url = f"https://www.americanas.com.br/categoria/eletrodomesticos/fogao/g/tipo-de-produto-Cooktop/tipo-de-produto-Fogareiro/tipo-de-produto-Fog%C3%A3o/tipo-de-produto-Fog%C3%A3o%20Piso/tipo-de-produto-Forno?chave=prf_hi_dm2_at_1_00_fog&viewMode=list&limit=24&offset={paginacao*24}"
            # url = f"https://www.americanas.com.br/categoria/eletrodomesticos/geladeira-refrigerador/g/tipo-de-produto-Freezer/tipo-de-produto-Frigobar/tipo-de-produto-Geladeira/tipo-de-produto-Refrigerador?chave=prf_hi_dm2_at_1_00_gel&viewMode=list&limit=24&offset={paginacao*24}"
            # url = f"https://www.americanas.com.br/categoria/informatica/notebooks?viewMode=list&limit=24&offset={paginacao*24}"
            #url = f"https://www.americanas.com.br/categoria/celulares-e-smartphones/smartphone?viewMode=list&limit=24&offset={paginacao*24}"
            url = f"https://www.amazon.com.br/s?i=electronics&rh=n%3A16243822011&s=price-desc-rank&page={paginacao}&language=pt_BR&brr=1&qid=1654026558&rd=1&ref=sr_pg_{paginacao}" #tv

            lista_links.append(url)

        print(lista_links)
        return [scrapy.Request(client.scrapyGet(url = url), callback = self.parse,  meta={'url': url}) for url in lista_links]
        # return [scrapy.Request(url = url, callback = self.parse, meta = {'url': url}) for url in urls]


    def parse(self, response):
        print("URL: {}".format(response.meta.get('url')))
        items = LinksItem()
        

        for registro in response.selector.xpath(f'//a[@class="a-link-normal s-no-outline"]/@href'): 
            print(registro.extract()) #.get()
                
            items['links'] = f"https://www.amazon.com.br{registro.extract()}" if registro.extract() is not None else ""
            yield items
                
    
        

