import scrapy

class JobpostshtmlSpider(scrapy.Spider):
    name = "jobpostshtml"

    def start_requests(self):
        url = 'https://stackoverflow.com/jobs?pg=25'
        tag = getattr(self, 'tag', None)
        if tag is not None:
            url = url + 'tag/' + tag
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        filename = 'jobposts_2.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Arquivo salvo %s' % filename)
    
    # def parse(self, response):
    #     for job in response.xpath('//*[@id="content"]/div[3]/div/div[1]/div/div[1]'):
    #         yield {
    #             'title': job.xpath('//*[@id="content"]/div[3]/div/div[1]/div/div[1]/div[1]/div[2]/div[2]/h2/a/text()').get(),
    #         }

    #     next_page = response.xpath('//*[@id="content"]/div[3]/div/div[1]/div/div[2]/div[1]/div[1]/div/a[6]@href').get()
    #     if next_page is not None:
    #         next_page = response.urljoin(next_page)
    #         yield scrapy.Request(next_page, callback=self.parse)
        
    #     filename = 'jobposts.html'
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)
    #     self.log('Arquivo salvo %s' % filename)


