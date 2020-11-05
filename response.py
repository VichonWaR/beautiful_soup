from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import numpy as np

kwords = ['python','security','clearance','military','database','mysql','remote','customer','service','mongodb','code','api','github','data','analysis']

# html url 
url = "https://www.indeed.com/jobs?as_and=python&as_phr&as_any&as_not&as_ttl&as_cmp&jt=all&st&salary&radius=0&l=Sacramento%2C%20CA&fromage=any&limit=50&sort&psf=advsrch&from=advancedsearch&vjk=3e2c26d1eeb5673f"

# pull data from html page / second attr to only pull english
headers = {"Accept-Language": "en-US, en;q=0.5"}
response = requests.get(url, headers=headers)

# sending data from page to Beautiful soup / had to import html5 into system to use
soup = BeautifulSoup(response.content, 'html5lib')

# selecting ID data I pull / job_descript only pulls NonType ((( needs fixing!!!! )))
results = soup.find(id='resultsCol')
job_descriptions = soup.find('div', class_ ='jobsearch-jobDescriptionText', recurisive=True)


# pulling further actual jobs from the class / this is to dive deeper into html
jobs = results.find_all('div', class_='result')
#descriptions = job_descriptions.find_all('div', class_ ='jobsearch-jobDescriptionText', recursive=True)
pays = results.find_all('div', class_='salarySnippet')
print('below is the len')
print(len(jobs))

# accessing a single element to get the title
#title = jobs[0].find('h2')
### pulling the link from the job 
#title_link = title.find('a')
# this will give you a partial, you need a full url"https.indeed "
#print(title_link['href']

### readable link / stripping extra html
#link_text = title_link.text
### clean it up
#print(link_text.strip())
# all together now
#job_description = [description.find_all('div').text.strip() for description in descriptions]

# was pulling 50, indexed to pull 2 titles for troubleshooting / pay works but not all blocks come with pay - so unmathicng results with titles pull
job_titles = [job.find('h2').find('a').text.strip() for job in jobs[:2]]
job_pay = [pay.find('span').find('span').text.strip()for pay in pays]

    

print(type(results))
print(type(job_descriptions))

#print(*descriptions, sep='\n')

#print(len(descriptions))




#out_put = re.findall(r'python', str(response.content))

#print(out_put[1:8])
