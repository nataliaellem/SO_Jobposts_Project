import scrapy
import time

class CompaniesidsSpider(scrapy.Spider):
    name = "companiesids"
    start_urls = ['https://stackoverflow.com/jobs/companies']
    companies_ids = []

    def parse(self, response):
        time.sleep(1)
        selectors = response.xpath('/html//div[@class="company-list"]//a[@class="s-link"]')

        for selector in selectors:
            time.sleep(1)
            # verificando se o selector não está repetido 
            company_link = selector.attrib['href']
            if company_link not in self.companies_ids:
                self.companies_ids.append(company_link)
                yield {'company_link' : company_link} 

        next_page = response.xpath('/html//div[@class="s-pagination"]//a/span[contains(text(), "next")]/..').attrib['href'] or None
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)


        # Running: scrapy crawl companiesids -o companiesids.jl


