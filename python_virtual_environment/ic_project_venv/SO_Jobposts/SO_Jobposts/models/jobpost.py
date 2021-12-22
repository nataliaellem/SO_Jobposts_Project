import models
from models import RemoteDetails
from models import Company


class Jobpost():

    id = None
    company = Company()
    title = None
    description = None
    salary_range_and_equity = None
    experience_level = None
    job_type = None
    onsite_and_limited_remote = None
    visa_sponsor = None
    paid_relocation = None
    remote = None
    post_time = None
    likes_reactions = None
    dislikes_reactions = None
    love_reactions = None
    job_remote_details = RemoteDetails()
    roles = []
    technologies = []
    industries = []



    def __init__(self, id, company, title, description, salary_range_and_equity, experience_level, job_type, onsite_and_limited_remote, visa_sponsor, paid_relocation, remote, post_time, likes_reactions, dislikes_reactions, love_reactions, job_remote_details, roles, technologies, industries):
        self.id = id
        self.company = company
        self.title = title 
        self.description = description 
        self.salary_range_and_equity = salary_range_and_equity 
        self.experience_level = experience_level 
        self.job_type = job_type 
        self.onsite_and_limited_remote = onsite_and_limited_remote 
        self.visa_sponsor = visa_sponsor 
        self.paid_relocation = paid_relocation 
        self.remote = remote 
        self.post_time = post_time 
        self.likes_reactions = likes_reactions 
        self.dislikes_reactions = dislikes_reactions 
        self.love_reactions = love_reactions 
        self.job_remote_details = job_remote_details 
        self.roles = roles 
        self.technologies = technologies 
        self.industries = industries 