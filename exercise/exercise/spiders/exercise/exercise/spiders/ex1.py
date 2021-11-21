import scrapy


class Ex1Spider(scrapy.Spider):
    name = 'ex1'
    allowed_domains = ['pythonscraping.com']
    start_urls = ['http://pythonscraping.com/linkedin/ietf.html']

    def parse(self, response):
        author = response.css('span.author-name::text').get()
        date = response.css('span.date::text').get()
        paragraphs = response.css('span.subheading::text').getall()
        result = {
            'author': author,
            'date': date,
        }
        it = 0
        for i in paragraphs:
            result["par" + str(it)] = i
            it += 1
        return result
