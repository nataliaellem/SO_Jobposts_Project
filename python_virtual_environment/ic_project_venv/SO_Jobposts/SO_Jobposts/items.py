# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobpostsItem(scrapy.Item):

    job_id = scrapy.Field()
    job_title = scrapy.Field()
    job_company = scrapy.Field()
    remote = scrapy.Field()
    paid_relocation = scrapy.Field()
    visa_sponsor = scrapy.Field()
    onsite_and_limited_remote = scrapy.Field()
    high_response_rate = scrapy.Field()
    post_time = scrapy.Field()
    likes_reactions = scrapy.Field()
    dislikes_reactions = scrapy.Field()
    love_reactions = scrapy.Field()
    salary_range_and_equity = scrapy.Field()
    experience_level = scrapy.Field()
    job_type = scrapy.Field()
    role = scrapy.Field()
    industries = scrapy.Field()
    technologies = scrapy.Field()
    job_description = scrapy.Field()
    employers_note = scrapy.Field()
    preferred_timezone = scrapy.Field()
    office_location = scrapy.Field()
    visa_sponsorhip = scrapy.Field()
    relocation_assistance = scrapy.Field()
    source_control = scrapy.Field()
    onestep_build = scrapy.Field()
    daily_builds = scrapy.Field()
    bug_database = scrapy.Field()
    bugs_fixed_before_writing_new_code = scrapy.Field()
    uptodate_schedule = scrapy.Field()
    specs = scrapy.Field()
    quiet_working_conditions = scrapy.Field()
    best_tools_that_money_can_buy = scrapy.Field()
    testers = scrapy.Field()
    code_screening = scrapy.Field()
    hallway_usability_testing = scrapy.Field()



class CompaniesItem(scrapy.Item):
    name = scrapy.Field()
    size = scrapy.Field()
    status = scrapy.Field()
    industry = scrapy.Field()
    founded = scrapy.Field()
    locations = scrapy.Field()
    company_technologies = scrapy.Field()
    about_company = scrapy.Field()
    benefits = scrapy.Field()
    people = scrapy.Field()
    jobs_openings = scrapy.Field()







