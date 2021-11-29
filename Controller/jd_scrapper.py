import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import json

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
    return result

def get_jobs_for_roles():
    final_res={"details":[]}
    for role in roles:
        jobs=get_jobs_for_cities(role)
        final_res["details"].append(jobs)
    with open('scrap.json', 'w', encoding='utf-8') as f:
        json.dump(final_res, f, ensure_ascii=False, indent=4)
    f_read = open('scrap.json')
    data = json.load(f_read)
    print(data)

def clean_text(text):
    encoded_text = text.encode("ascii", "ignore")
    clean_text = encoded_text.decode()
    clean_text=clean_text.replace("u'", "'")
    clean_text=clean_text.replace("\"", " ")
    clean_text=clean_text.replace("\n", "<br>")
    return clean_text

def extract_job_title_from_result(soup,city,result): 
    div=soup.find(name="div", attrs={"id":"mosaic-provider-jobcards"})
    a_ele_list=div.findAll("a",href=True)
    cntr=0
    for a_ele in a_ele_list:
        #To get one job per location per role..Can remove to get all
        if(cntr==1):
            return
        cntr+=1
        ele=a_ele.find("h2", {"class": re.compile("jobTitle*")})
        if(ele!=None):
            title=ele.text
            title=clean_text(title)
            href=a_ele["href"]
            job_url="https://www.indeed.com"+href
            job_page=requests.get(job_url)
            job_soup=BeautifulSoup(job_page.text,"html.parser")
            description_div=job_soup.find("div",{"class":"jobsearch-jobDescriptionText"})
            description=""
            if(description_div==None):
                continue
            else:
                description=description_div.text
            description=clean_text(description)
            location_div=job_soup.find("div",{"class":"jobsearch-jobLocationHeader-location"})
            if(location_div!=None):
                location=location_div.text

            else:
                location= city
            location=clean_text(location)
            res_dict={}
            res_dict["title"]=title
            res_dict["desc"]=description
            res_dict["location"]=location
            result.append(res_dict)

#This is the main function call. Response of this would be list of dicts
print(get_jobs_for_roles())