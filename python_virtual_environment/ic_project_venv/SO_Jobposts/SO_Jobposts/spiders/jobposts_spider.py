import models
from models import Company
from models import Benefit
from models import Industry
from models import JoelTest
from models import RemoteDetails
from models import Role
from models import Technology
from models import Jobpost as jp
from models import RemoteDetails

import scrapy
import re
import json
import time
from ..items import JobpostsItem


# Antes de rodar esta spider deve-se já ter rodado a spider "postsids"
# pois os ids já devem estar no arquivo "postsids"
# Os arquivos também devem estar atudalizados

class JobpostsSpider(scrapy.Spider):
    name = "jobposts"
    host = "https://stackoverflow.com/jobs"
    start_urls = []

    try:
        with open("./postsids.jl", "r") as file:
            for line in file:
                json_object = json.loads(line)
                jobid = json_object["jobid"]
                start_urls.append(host+"/"+jobid)
    except FileNotFoundError:
        pass


    def parse(self, response):
        
        time.sleep(2)

        # ------------- Job ----------------:

        job_id = response.xpath('/html//span[@class="ml12 js-react-toggle c-pointer"]')[0].attrib['data-job-id'] or None
        job_title = response.xpath('/html//a[@class="fc-black-900"]').attrib['title'] or None
        job_company = response.xpath('/html//div[@id="company-items"]//div[@class="flex--item fl1"]/a').attrib['href'] or None
        job_description = response.xpath('/html//section[@class="mb32 fs-body2 fc-medium"]').extract() or None
        salary_range_and_equity = None    
        experience_level = None
        job_type = None
        role = None
        industries = None                                                   
        try:
            salary_range_and_equity = response.xpath('/html//li[@title]/span[@class="fc-green-400"]/text()')[0].extract()
            experience_level = response.xpath('/html//span[contains(text(), "Experience level:")]/following-sibling::span/text()')[0].extract()
            job_type = response.xpath('/html//span[contains(text(), "Job type:")]/following-sibling::span/text()')[0].extract()
            role = response.xpath('/html//span[contains(text(), "Role:")]/following-sibling::span/text()')[0].extract()
            industries = response.xpath('/html//span[contains(text(), "Industry:")]/following-sibling::span/text()')[0].extract()
        except IndexError:
            pass
                                
        technologies = response.xpath('/html//section/h2[contains(text(), "Technologies")]/following-sibling::div/a/text()').extract() or None
        # Boolean attributes:
        remote = "Remote" in response.xpath('/html//span[@class="fc-yellow-500"]/text()').extract() or None
        paid_relocation = "Paid relocation" in response.xpath('/html//span[@class="fc-powder-400"]/text()').extract() or None
        visa_sponsor = "Visa sponsor" in response.xpath('/html//span[@class="fc-red-300"]/text()').extract()  or None
        onsite_and_limited_remote = "On-site and limited remote" in response.xpath('/html//span[@class="fc-yellow-500"]/text()').extract() or None
        high_response_rate = "High response rate" in response.xpath('/html//span[@class="fc-green-500 fw-bold"]/text()').extract() or None

        post_time = None
        likes_reactions = None
        dislikes_reactions = None
        love_reactions = None
        try:
            post_time = response.xpath('/html//svg[@class="svg-icon iconClock"]/following-sibling::text()')[0].extract()
            likes_reactions = response.xpath('/html//svg[@class="svg-icon iconThumbsUp"]/following-sibling::span/text()')[0].extract()
            dislikes_reactions = response.xpath('/html//svg[@class="svg-icon iconThumbsDown"]/following-sibling::span/text()')[0].extract()
            love_reactions = response.xpath('/html//svg[@class="svg-icon iconHeart"]/following-sibling::span/text()')[0].extract()
        except IndexError:
            pass


        # ------------------ Remote Details -------------------------------
        employers_note_str = "Employer's note:"
        employers_note = response.xpath('/html//span[contains(text(), employers_note_str)]/following-sibling::span/text()').extract() or None
        preferred_timezone = None
        office_location = None
        visa_sponsorhip = None
        relocation_assistance = None
        try:
            preferred_timezone = response.xpath('/html//span[contains(text(), "Preferred Timezone:")]/following-sibling::span/text()')[0].extract() or None
            office_location = response.xpath('/html//span[contains(text(), "Office Location:")]/following-sibling::span/text()')[0].extract() or None
            visa_sponsorhip = response.xpath('/html//span[contains(text(), "Visa Sponsorship:")]/following-sibling::span/text()')[0].extract() or None
            relocation_assistance = response.xpath('/html//span[contains(text(), "Relocation Assistance:")]/following-sibling::span/text()')[0].extract() or None
        except IndexError:
            pass


        # -------------------- Joel Test ---------------------------------

        # O joel test não aparece na página da empresa, apenas na página do jobpost

        # Verificando se no jobpost tem o joel test:
        aux = response.xpath('/html//section[@class="-joel-test mb32"]').extract() or None
        # As variaveis para cada teste são None se não tiver Joel test no post, 
        # serão True se o teste tiver o 'checked' e serão False se tiver o 'unchecked'
        source_control = None
        onestep_build = None
        daily_builds = None
        bug_database = None
        bugs_fixed_before_writing_new_code = None
        uptodate_schedule = None
        specs = None
        quiet_working_conditions = None
        best_tools_that_money_can_buy = None
        testers = None
        code_screening = None
        hallway_usability_testing = None
        if aux != None:
            joel_test_checked_list = response.xpath('/html//section[@class="-joel-test mb32"]/div/div/div/span[@class="fc-green-400"]/following-sibling::text()').extract() or []
            joel_test_unchecked_list = response.xpath('/html//section[@class="-joel-test mb32"]/div/div/div/span[@class="fc-red-500"]/following-sibling::text()').extract() or []
            
            for item in joel_test_checked_list:
                source_control = True if ('Source control' in item) else None
                onestep_build = True if ('One-step build' in item) else None
                daily_builds = True if ('Daily builds' in item) else None
                bug_database = True if ('Bug database' in item) else None
                bugs_fixed_before_writing_new_code = True if ('Bugs fixed before writing new code' in item ) else None
                uptodate_schedule = True if ('Up-to-date schedule' in item) else None
                specs = True if ('Specs' in item ) else None
                quiet_working_conditions = True if ('Quiet working conditions' in item) else None
                best_tools_that_money_can_buy = True if ('Best tools that money can buy' in item) else None
                testers = True if ('Testers' in item) else None
                code_screening = True if ('Code screening' in item) else None
                hallway_usability_testing = True if ('Hallway usability testing' in item) else None

            for item in joel_test_unchecked_list:
                source_control = False if ('Source control' in item) else None
                onestep_build = False if ('One-step build' in item) else None
                daily_builds = False if ('Daily builds' in item) else None
                bug_database = False if ('Bug database' in item) else None
                bugs_fixed_before_writing_new_code = False if ('Bugs fixed before writing new code' in item ) else None
                uptodate_schedule = False if ('Up-to-date schedule' in item) else None
                specs = False if ('Specs' in item ) else None
                quiet_working_conditions = False if ('Quiet working conditions' in item) else None
                best_tools_that_money_can_buy = False if ('Best tools that money can buy\r\n                                    ' in item) else None
                testers = False if ('Testers' in item) else None
                code_screening = False if ('Code screening' in item) else None
                hallway_usability_testing = False if ('Hallway usability testing' in item) else None
        
        
        # Instanciando objetos com as classes de 'models':
        
        new_remote_details = RemoteDetails(self, employers_note, preferred_timezone, office_location, visa_sponsorhip, relocation_assistance)

        company = Company()
        company.id = job_company
         
        # new_jobpost = jp.Jobpost()
        # new_jobpost.id(job_id)
        # new_jobpost.company = company
        # new_jobpost.title = job_title
        # new_jobpost.description = job_description
        # new_jobpost.salary_range = salary_range_and_equity
        # new_jobpost.experience_level = experience_level
        # new_jobpost.job_type = job_type
        # new_jobpost.onsite_and_limited_remote = onsite_and_limited_remote
        # new_jobpost.visa_sponsor = visa_sponsor
        # new_jobpost.paid_relocation = paid_relocation
        # new_jobpost.remote = remote
        # new_jobpost.post_time = post_time
        # new_jobpost.likes_reactions = likes_reactions
        # new_jobpost.dislikes_reactions = dislikes_reactions
        # new_jobpost.love_reactions = love_reactions
        # new_jobpost.job_remote_details = new_remote_details
        # new_jobpost.roles = role
        # new_jobpost.technologies = technologies
        # new_jobpost.industries = industries
 



        # Instancioando os objetos com as classes do tipo 'Item'
        jobpost = JobpostsItem()


        jobpost['job_id'] = job_id
        jobpost['job_title'] = job_title 
        jobpost['job_company'] = job_company
        jobpost['remote'] = remote  
        jobpost['paid_relocation'] = paid_relocation 
        jobpost['visa_sponsor'] = visa_sponsor 
        jobpost['onsite_and_limited_remote'] = onsite_and_limited_remote 
        jobpost['high_response_rate'] = high_response_rate 
        jobpost['post_time'] = post_time 
        jobpost['likes_reactions'] = likes_reactions 
        jobpost['dislikes_reactions'] = dislikes_reactions 
        jobpost['love_reactions'] = love_reactions 
        jobpost['salary_range_and_equity'] = salary_range_and_equity 
        jobpost['experience_level'] = experience_level 
        jobpost['job_type'] = job_type 
        jobpost['role'] = role 
        jobpost['industries'] = industries 
        jobpost['technologies'] = technologies
        jobpost['job_description'] = job_description
        jobpost['employers_note'] = employers_note
        jobpost['preferred_timezone'] = preferred_timezone
        jobpost['office_location'] = office_location
        jobpost['visa_sponsorhip'] = visa_sponsorhip
        jobpost['relocation_assistance'] = relocation_assistance
        jobpost['source_control'] = source_control
        jobpost['onestep_build'] = onestep_build
        jobpost['daily_builds'] = daily_builds
        jobpost['bug_database'] = bug_database
        jobpost['bugs_fixed_before_writing_new_code'] = bugs_fixed_before_writing_new_code
        jobpost['uptodate_schedule'] = uptodate_schedule
        jobpost['specs'] = specs
        jobpost['quiet_working_conditions'] = quiet_working_conditions
        jobpost['best_tools_that_money_can_buy'] = best_tools_that_money_can_buy
        jobpost['testers'] = testers
        jobpost['code_screening'] = code_screening
        jobpost['hallway_usability_testing'] = hallway_usability_testing



        yield jobpost




    # Running: scrapy crawl jobposts -o jobposts.json

