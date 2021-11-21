import scrapy
# will allow us to navigate in the page and add rules
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor  # will allow us to click on links
# literature was the name of the previous spider
from literature.items import ClothesItem
from scrapy_selenium import SeleniumRequest

class ClothesSpider(scrapy.Spider):
    name = 'asos'
    allowed_domains = ['asos.com']
    start_urls = ['https://www.asos.com/it/search/?q=sciarpa']

    
    def parse(self, response):
        products = response.css("a._3TqU78D::attr(href)").getall() #get all the links in the page
        for prd in products: #for loop
            yield scrapy.Request(url = prd, callback = self.parseitem) #exec a request for each link in the page
        

    def parseitem(self,response): 
        result = ClothesItem() #build item for the JSON file
        result['title'] = response.xpath("//h1/text()").get()
        result['images'] = response.xpath("//img[starts-with(@src,'https://images.asos-media.com/products') and not(@class)]/@src").getall()
        result['url'] = response.url
        results = []
        results.append(result)
        return results #return json file to be output

        

        