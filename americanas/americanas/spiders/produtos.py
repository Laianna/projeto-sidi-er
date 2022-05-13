from ast import IsNot
import scrapy
import pandas as pd
from americanas.items import AmericanasItem
import re
from scraper_api import ScraperAPIClient
client = ScraperAPIClient('15158d4674ce528e593a775a4b90dcc9')

class ProductSpider(scrapy.Spider):

    name = 'article'
    df_links  = None
    
    def load_links(self):
        self.df_links = pd.read_csv('americanas_links_2.csv')


    def start_requests(self):

        self.load_links()

        urls = self.df_links["links"][1000:].to_list()
        #urls = ["https://www.americanas.com.br/produto/4875373969"]
        
        print(urls)

        return [scrapy.Request(client.scrapyGet(url = url), callback = self.parse) for url in urls]
        #return [scrapy.Request(url = url, callback = self.parse, meta = {'dont_merge_cookies': True}) for url in urls]


    def parse(self, response):
        
        items = AmericanasItem()
       
        url = response.url
        titulo = response.xpath('//*[@id="rsyswpsdk"]/div/main/div[3]/div[1]/div/div[2]/h1/text()').extract()
        ean = re.findall(r'digo de barras</td><td class="spec-drawer__Text-sc-jcvy3q-5 fMwSYd">([0-9]+)|$', str(response.body))
        descricao = response.xpath('//*[@id="info-section"]/div[2]/div/div/div/div').xpath('normalize-space()').getall()
      
        '''print("###########################################################################")
        print("URL is: {}".format(url))
        print("Title is: {}".format(titulo))
        print("EAN is: {}".format(ean))
        print("Descricao is: {}".format(descricao))
        print("###########################################################################")'''

        items['titulo'] = titulo[0] if len(titulo) != 0 else ""
        items['ean'] = ean[0]
        #items['ean'] = ean if ean is not None else ""
        items['url'] = url
        items['descricao'] = descricao[0] if len(descricao) != 0 else ""
        
        yield items