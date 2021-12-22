import scrapy
import time


class PostsidsSpider(scrapy.Spider):
    name = "postsids"
    start_urls = ['https://stackoverflow.com/jobs']
    jobids = []

    def parse(self, response):
        time.sleep(2)

        selectors = response.xpath('/html//div[@class = "listResults"]/div[@data-jobid]')

        for selector in selectors:
            # verificando se o selector não está repetido 
            data_jobid = selector.attrib['data-jobid']
            if data_jobid not in self.jobids:
                self.jobids.append(data_jobid)
                yield {'jobid' : data_jobid} 

        next_page = response.xpath('/html//a[@class = "s-pagination--item"]')[-1].attrib['href']
        next_buttom = response.xpath('/html//a[@class = "s-pagination--item"]/span/text()')[-1].extract()
        if next_buttom == 'next':
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)


        # Running: scrapy crawl postsids -o postsids.jl