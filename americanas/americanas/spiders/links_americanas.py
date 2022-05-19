from ast import IsNot
import scrapy
import pandas as pd
from americanas.items import AmericanasItem
import re
from scraper_api import ScraperAPIClient
import Selector
client = ScraperAPIClient('15158d4674ce528e593a775a4b90dcc9')

class ProductAmazonSpider(scrapy.Spider):

    name = 'article'
    df_links  = None
    
    def load_links(self):

        for paginacao in range(1, 2):
            
            url = f"https://www.americanas.com.br/categoria/informatica/notebooks?viewMode=list&limit=24&offset={paginacao*24}"
            #url = f"https://www.americanas.com.br/categoria/celulares-e-smartphones/smartphone?viewMode=list&limit=24&offset={paginacao*24}"

        self.df_links.append(url)


    def start_requests(self):

        self.load_links()

        urls = self.df_links
        #urls = ["https://www.amazon.com.br/Notebook-Samsung-256GB-Windows-Chumbo/dp/B09N41J9K1/"]
        #urls = ["https://www.amazon.com.br/Mouse-Pad-Gaming-Havit-HV-MP830/dp/B0152HPXXE/"]
        
        print(urls)

        return [scrapy.Request(client.scrapyGet(url = url), callback = self.parse,  meta={'url': url}) for url in urls]
        # return [scrapy.Request(url = url, callback = self.parse, meta = {'url': url}) for url in urls]


    def parse(self, response):
        sel = Selector(response)
        
        # //*[@id="rsyswpsdk"]/div/main/div/div[3]/div[3]/div[1]/div
        
        for entry in sel.xpath("//div[@class='src__Wrapper-sc-1wgxjb2-0 dUUAKQ']/a"):
            print(entry.xpath('href').extract())

        # lista_divs = resp.find_all("div", {"class": "src__Wrapper-sc-1wgxjb2-0 dUUAKQ"})

        # for div in lista_divs:  
        #     for link in div.findAll('a', attrs={'href': re.compile("^/")}):
        #         links.append(f"https://www.americanas.com.br{link.get('href')}")
        
        
        
        
        
        # items = AmericanasItem()
        # # print(str(response.body))
        # url_meta = response.meta.get('url')
        # url = response.url
        
        # titulo = response.xpath('//*[@id="productTitle"]/text()').extract()
        # tabela = response.xpath('//*[@id="productDetails_techSpec_section_1"]/tr/*/text()').re('(\w+[^\n]+)')
        # tabela_string = ''.join(tabela) 
        # ean = re.findall(r'EAN.+?([0-9]+)|$', tabela_string)
        # descricao = response.xpath('//*[@id="productDescription"]/p/span/text()').getall()
        # preco = response.xpath('//*[@id="corePrice_feature_div"]/div/span/span[1]/text()').extract()

        # categoria = response.xpath('//a[@class="a-link-normal a-color-tertiary"]/text()').extract()
        # categoria = '/'.join(map(lambda x: x.strip(), categoria)).strip()

        
        '''print("###########################################################################")
        print("URL: {}".format(url))
        print("Meta URL: {}".format(url_meta))
        print("Titulo: {}".format(titulo))
        print("EAN: {}".format(ean))
        print("Descricao: {}".format(descricao))
        print("Preco: {}".format(preco))
        print("Categoria: {}".format(categoria))
        print("###########################################################################")'''
        

        items['titulo'] = titulo[0].strip() if len(titulo) != 0 else ""
        items['ean'] = ean[0] if len(ean) != 0 else ""
        items['url'] = url_meta
        items['descricao'] = descricao[0] if len(descricao) != 0 else ""
        items['preco'] = preco if preco is not None else ""
        items['categoria'] = categoria if categoria is not None else ""

        yield items