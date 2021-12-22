import models
from models import JoelTest


class Company():

    def __init__(self, id, name, location, size, type, about_company, benefits, company_people, joel_test):
        self.id = id
        self.name = name
        self.location = location
        self.size = size
        self.type = type
        self.about_company = about_company
        self.benefits = benefits
        self.company_people = company_people
        self.joel_test = joel_test