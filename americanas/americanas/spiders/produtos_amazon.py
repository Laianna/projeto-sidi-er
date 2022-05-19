from ast import IsNot
import scrapy
import pandas as pd
from americanas.items import AmericanasItem
import re
from scraper_api import ScraperAPIClient
client = ScraperAPIClient('15158d4674ce528e593a775a4b90dcc9')

class ProductAmazonSpider(scrapy.Spider):

    name = 'article'
    df_links  = None
    
    def load_links(self):
        self.df_links = pd.read_csv('amazon_links_2.csv') #Mudar para os links corretos


    def start_requests(self):

        # self.load_links()

        # urls = self.df_links["links"][500:].to_list()
        urls = ["https://www.amazon.com.br/Notebook-Samsung-256GB-Windows-Chumbo/dp/B09N41J9K1/"]
        
        print(urls)

        # return [scrapy.Request(client.scrapyGet(url = url), callback = self.parse,  meta={'url': url}) for url in urls]
        return [scrapy.Request(url = url, callback = self.parse, meta = {'url': url}) for url in urls]


    def parse(self, response):
        
        items = AmericanasItem()
        # print(str(response.body))
        url_meta = response.meta.get('url')
        url = response.url
        titulo = response.xpath('//*[@id="productTitle"]/text()').extract()
        
        tabela = response.xpath('//*[@id="productDetails_techSpec_section_1"]/tbody/tr[1]')
        print(tabela)
        ean = re.findall(r'EAN </th>   <td class="a-size-base prodDetAttrValue">\n                \u200e([0-9]+)|$', str(tabela))
        #  EAN </th>   <td class="a-size-base prodDetAttrValue">\n                &lrm;7892509120784 </td>
        descricao = response.xpath('//*[@id="productDescription"]/p/span').xpath('normalize-space()').getall()
        preco = response.xpath('//*[@id="corePrice_feature_div"]/div/span/span[1]').extract()
      
        print("###########################################################################")
        print("URL: {}".format(url))
        print("Meta URL: {}".format(url_meta))
        print("Titulo: {}".format(titulo))
        print("EAN: {}".format(ean))
        print("Descricao: {}".format(descricao))
        print("Preco: {}".format(preco))
        print("###########################################################################")

        # items['titulo'] = titulo[0] if len(titulo) != 0 else ""
        # items['ean'] = ean[0]
        # #items['ean'] = ean if ean is not None else ""
        # items['url'] = url_meta
        # items['descricao'] = descricao[0] if len(descricao) != 0 else ""
        # items['preco'] = descricao[0] if len(descricao) != 0 else ""
        
        # yield items