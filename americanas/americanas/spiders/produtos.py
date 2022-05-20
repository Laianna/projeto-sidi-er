from ast import IsNot
import scrapy
import pandas as pd
from americanas.items import AmericanasItem
import re
from scraper_api import ScraperAPIClient
# client = ScraperAPIClient('15158d4674ce528e593a775a4b90dcc9')#Morreu 20/05 Maio
client = ScraperAPIClient('39e2ae4a508557b0b178342d1664d3fd') ##--> Mari 2

class ProductSpider(scrapy.Spider):

    name = 'produtos_americanas'
    df_links  = None
    
    def load_links(self):
        self.df_links = pd.read_csv('../../../Dados/americanas_links_notebooks.csv')
        #self.df_links = pd.read_csv('americanas_links_2.csv')


    def start_requests(self):

        self.load_links()

        urls = self.df_links["links"].to_list()
        #urls = ["https://www.americanas.com.br/produto/4875373969"]
        #urls = ["https://www.americanas.com.br/produto/2947509539"]
        
        print(urls)

        return [scrapy.Request(client.scrapyGet(url = url), callback = self.parse,  meta={'url': url}) for url in urls]
        #return [scrapy.Request(url = url, callback = self.parse, meta = {'dont_merge_cookies': True}) for url in urls]


    def parse(self, response):
        
        items = AmericanasItem()
       
        url_meta = response.meta.get('url')
        url = response.url

        titulo = response.xpath('//h1[@class = "product-title__Title-sc-1hlrxcw-0 jyetLr"]/text()').extract()
        ean = re.findall(r'digo de barras</td><td class="spec-drawer__Text-sc-jcvy3q-5 fMwSYd">([0-9]+)|$', str(response.body))
        descricao = response.xpath('//*[@id="info-section"]/div[2]/div/div/div/div').xpath('normalize-space()').getall()
        preco = response.xpath('//div[@class = "styles__PriceText-sc-x06r9i-0 dUTOlD priceSales"]/text()').extract()
        categoria = response.xpath('//li[@class = "styles__ListItem-sc-170sob9-2 kLKska"]/a/@href').extract()      


        '''print("\n\n###########################################################################")
        print("URL: {}".format(url))
        print("Meta URL: {}".format(url_meta))
        print("Titulo: {}".format(titulo))
        print("EAN: {}".format(ean))
        print("Descricao: {}".format(descricao))
        print("Preco: {}".format(preco))
        print("Categoria: {}".format(categoria))
        print("###########################################################################\n\n")'''

        items['titulo'] = titulo[0] if len(titulo) != 0 else ""
        items['ean'] = ean[0] if len(ean) != 0 else ""
        #items['ean'] = ean if ean is not None else ""
        items['url'] = url_meta
        items['descricao'] = descricao[0] if len(descricao) != 0 else ""
        items['preco'] = preco[0] if len(preco) != 0 else ""
        items['categoria'] = categoria[-1] if len(categoria) != 0 else ""
                
        yield items