import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import re

base_url = "https://www.indeed.com/jobs?q={role}+%2420%2C000&l={city}"
roles=["software+engineer","data+scientist"]
city_set = ['New+York','Chicago','San+Francisco', 'Austin', 'Seattle', 'Los+Angeles', 'Philadelphia', 'Atlanta', 'Dallas', 'Pittsburgh', 'Portland', 'Phoenix', 'Denver', 'Houston', 'Miami', 'Washington+DC', 'Boulder']

def get_jobs_for_cities(role):
    result=[]
    for city in city_set:
        city_url=base_url.format(role=role,city=city)
        page = requests.get(city_url)
        soup = BeautifulSoup(page.text, "html.parser")
        extract_job_title_from_result(soup,city,result)
    df=pd.DataFrame(result)
    print(df.head())

def get_jobs_for_roles():
    for role in roles:
        get_jobs_for_cities(role)

def extract_job_title_from_result(soup,city,result): 
    div=soup.find(name="div", attrs={"id":"mosaic-provider-jobcards"})
    a_ele_list=div.findAll("a",href=True)
    cntr=0
    for a_ele in a_ele_list:
        if(cntr==5):
            return
        cntr+=1
        ele=a_ele.find("h2", {"class": re.compile("jobTitle*")})
        if(ele!=None):
            title=ele.text
            href=a_ele["href"]
            job_url="https://www.indeed.com"+href
            job_page=requests.get(job_url)
            job_soup=BeautifulSoup(job_page.text,"html.parser")

get_jobs_for_roles()