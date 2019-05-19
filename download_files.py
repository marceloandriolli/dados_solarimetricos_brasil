import re
import scrapy
from scrapy.crawler import CrawlerProcess



class EstacoesSonda(scrapy.Spider):
    name = 'example.com'
    allowed_domains = ['http://sonda.ccst.inpe.br']
    start_urls = [
        'http://sonda.ccst.inpe.br/basedados/saomartinho.html',
        'http://sonda.ccst.inpe.br/basedados/triunfo.html',
        'http://sonda.ccst.inpe.br/basedados/brasilia.html',
        'http://sonda.ccst.inpe.br/basedados/cachoeira.html',
        'http://sonda.ccst.inpe.br/basedados/caico.html',
        'http://sonda.ccst.inpe.br/basedados/campogrande.html',
        'http://sonda.ccst.inpe.br/basedados/cuiaba.html',
        'http://sonda.ccst.inpe.br/basedados/ourinhos.html',
        'http://sonda.ccst.inpe.br/basedados/palmas.html',
        'http://sonda.ccst.inpe.br/basedados/petrolina.html',
        'http://sonda.ccst.inpe.br/basedados/rolimdemoura.html',
        'http://sonda.ccst.inpe.br/basedados/chapeco.html',
        'http://sonda.ccst.inpe.br/basedados/curitiba.html',
        'http://sonda.ccst.inpe.br/basedados/florianopolis.html',
        'http://sonda.ccst.inpe.br/basedados/joinville.html',
        'http://sonda.ccst.inpe.br/basedados/sombrio.html',
    ]

    def parse(self, response):
        tables = response.xpath('//*[@id="tbl_dados"]')
        for table in tables:
            year = table.xpath('thead/tr[1]/td/text()').get()            
            for month in table.xpath('tbody/tr[1]/td/text()').getall():
                url = table.xpath('tbody/tr[2]/td/a/@href').get()
                header_version = table.xpath('tbody/tr[2]/td/text()').get() or '<3.3'
                yield {'year':year, 'month': month, 'header_version': header_version, 'url': url}


process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})


process.crawl(EstacoesSonda)
process.start()
