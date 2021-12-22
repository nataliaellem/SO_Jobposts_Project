import scrapy
import models
from models import Role

class RolesSpider(scrapy.Spider):

    name = "roles"
    start_urls = ['https://stackoverflow.com/jobs']


    def parse(self, response):
        roles_list = response.xpath('/html//div[@class="d-flex gs4 gsy fd-column"]//select[@id="dr"]/option/text()').extract()
        for i in range(0, len(roles_list)):
            role = Role(name=roles_list[i])
            yield{'role_name':roles_list[i]}


# running: scrapy crawl roles -o roles.jl
