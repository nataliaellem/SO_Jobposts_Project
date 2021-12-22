import scrapy 


class IndustriesSpider(scrapy.Spider):
    name = "industries"
    start_urls = ['https://stackoverflow.com/jobs']


    def parse(self, response):
        industries_list = response.xpath('/html//div[@class="d-flex gs4 gsy fd-column"]//select[@id="i"]/option/text()').extract()
        for i in range(0, len(industries_list)):
            yield{'industry_name': industries_list[i]}

    
# running: scrapy crawl industries -o industries.jl
