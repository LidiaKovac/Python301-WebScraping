import scrapy
from scrapy.spiders import CrawlSpider, Rule #will allow us to navigate in the page and add rules
from scrapy.linkextractors import LinkExtractor #will allow us to click on links
from literature.items import ClothesItem #literature was the name of the previous spider

class ClothesSpider(scrapy.Spider):
    name = 'asos'
    allowed_domains = ['asos.com']
    start_urls = ['https://www.asos.com/it/asos-design/asos-design-maglione-beige-con-spalle-scoperte/prd/200237758']

    

    def parse(self, response):
        result = ClothesItem()
        result['title'] = response.css("h1::text").get()
        result['images'] = response.xpath("//img[starts-with(@src,'https://images.asos-media.com/products') and not(@class)]/@src").getall()
        return result


