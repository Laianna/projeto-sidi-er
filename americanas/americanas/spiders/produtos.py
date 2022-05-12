from ast import IsNot
import scrapy
import pandas as pd
from americanas.items import AmericanasItem

class ProductSpider(scrapy.Spider):

    name = 'article'
    df_links  = None
    
    def load_links(self):
        self.df_links = pd.read_csv('americanas_links_2.csv')


    def start_requests(self):
        self.load_links()

        urls = self.df_links["links"][:10].to_list()
        # urls = ["https://www.americanas.com.br/produto/4875373969"]
        
        # urls = [
        #         'http://en.wikipedia.org/wiki/Python_'
        #         '%28programming_language%29',
        #         'https://en.wikipedia.org/wiki/Functional_programming',
        #         'https://en.wikipedia.org/wiki/Monty_Python']
        
        print(urls)

        return [scrapy.Request(url = url, callback = self.parse) for url in urls]


    def parse(self, response):
        
        items = AmericanasItem()

        url = response.url
        title = response.xpath('//*[@id="rsyswpsdk"]/div/main/div[3]/div[1]/div/div[2]/h1/text()').extract()
        ean = response.css('td:nth-child(2)::text').extract_first()
        # ean = response.select('//*[@id="rsyswpsdk"]/div/main/div[8]/div[2]/div/div[2]/table').extract()
        #descricao = response.xpath('//*[@id="info-section"]/div[2]/div/div/div/div').extract()
        descricao = response.xpath('//*[@id="info-section"]/div[2]/div/div/div/div').xpath('normalize-space()').getall()
        
        print('URL is: {}'.format(url))
        print('Title is: {}'.format(title))
        print('EAN is: {}'.format(ean))
        print('Descricao is: {}'.format(descricao))
        
        items['title'] = title[0] if len(title) != 0 else ""
        items['ean'] = ean if ean is not None else ""
        items['url'] = url
        items['descricao'] = descricao[0] if len(descricao) != 0 else ""
        
        yield items
       