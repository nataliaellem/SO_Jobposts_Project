import scrapy
import json
import time
from ..items import CompaniesItem

class CompaniesSpider(scrapy.Spider):
    name = "companies"
    host = "https://stackoverflow.com"
    start_urls = []
 

    try:
        with open("./companiesids.jl", "r") as file:
            for line in file:
                json_object = json.loads(line)
                company_link = json_object["company_link"]
                start_urls.append(host + company_link)
    except FileNotFoundError:
        pass


    def parse(self, response):
        time.sleep(2)

        name = None
        size = None
        status = None
        industry = None
        founded = None
        try:
            name = response.xpath('/html//h1[@class="fs-display1 sticky:fs-title md:fs-headline1 t lh-xs fw-normal mb8 sticky:mt0 sticky:mb0 fc-black-900 sticky:sm:fs-subheading"]/text()')[0].extract()
            size = response.xpath('/html//p[contains(text(), "Size")]/following-sibling::span[@class="d-block"]/text()')[0].extract()
            status = response.xpath('/html//p[contains(text(), "Status")]/following-sibling::span[@class="d-block"]/text()')[0].extract()
            industry = response.xpath('/html//p[contains(text(), "Industry")]/following-sibling::span[@class="d-block"]/text()')[0].extract()
            founded = response.xpath('/html//p[contains(text(), "Founded")]/following-sibling::span[@class="d-block"]/text()')[0].extract()
        except IndexError:
            pass

        locations = response.xpath('/html//div[@class="mt32 js-locations"]//a/@data-query').extract() or None
        company_technologies = response.xpath('/html//div[@class="d-flex gs4 mb16 fw-wrap"]/a/text()').extract() or None
        people = response.xpath('/html//div[@id="people-items"]//a/@href').extract() or None
        jobs_openings = response.xpath('/html//div[@id="jobs-items"]/div[@class="listResults js-jobs"]/span/div/@data-jobid').extract() or None
        about_company = response.xpath('/html//div[@id="tech-stack-items"]/p/text()').extract() or None
        benefits = response.xpath('/html//div[@class="mt32"]/h2[contains(text(), "Company Benefits")]/following-sibling::ol//div/text()').extract() or None

        yield{'name': name,
            'size': size,
            'status': status,
            'industry': industry,
            'founded': founded,
            'locations': locations,
            'company_technologies': company_technologies,
            'about_company': about_company,
            'people': people,
            'jobs_openings': jobs_openings,
            'benefits': benefits}


        # running: scrapy crawl companies -o companies.jl