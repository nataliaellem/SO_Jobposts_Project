import scrapy
import time


# As tags têm uma descrição que está cortada neste link, para obter a descrição completa teria que
# entrar no link da tag onde tem várias outras informações sobre a tag 

class Technologies_Spider(scrapy.Spider):
    name = "technologies"
    start_urls = ['https://stackoverflow.com/tags']


    def parse(self, response):

        tags_list = response.xpath('/html//div[@id="tags-browser"]/div[@class="grid--item s-card js-tag-cell d-flex fd-column"]//a[@class="post-tag"]/text()').extract() 
        time.sleep(1)
        for i in range(0, len(tags_list)):
            time.sleep(1)
            yield{'tag_name': tags_list[i]}


        next_page = response.xpath('/html//div[@class="s-pagination site1 themed pager float-right"]/a[@rel="next"]').attrib['href']
        if  next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    # running: scrapy crawl technologies -o technologies.jl