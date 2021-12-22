import scrapy
import json

class TestsSpider(scrapy.Spider):
    name = "test"
    start_urls = ['https://stackoverflow.com/jobs']

    def parse(self, response):
        selectors = response.xpath('/html//div[@class = "listResults"]/div[@data-jobid]')
    
        for selector in selectors:
            yield {'jobid' : selector.attrib['data-jobid']} 

        next_page = response.xpath('/html//a[@class = "s-pagination--item"]')[-1].attrib['href']
        next_buttom = response.xpath('/html//a[@class = "s-pagination--item"]/span/text()')[-1].extract()
        if next_buttom == 'next':
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
