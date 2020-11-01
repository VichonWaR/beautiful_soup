from bs4 import BeautifulSoup
import requests
import re

# html url 
url = "https://www.indeed.com/jobs?as_and=python&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&salary=&radius=0&l=Sacramento%2C+CA&fromage=any&limit=50&sort=&psf=advsrch&from=advancedsearch"

# pull data from html page
response = requests.get(url)

# sending data from page to Beautiful soup 
soup = BeautifulSoup(response.content, 'html5lib')

# selecting ID data I pull
results = soup.find(id='resultsCol')


# pulling further actual jobs from the class
jobs = results.find_all('div', class_='result')
print('below is the len')
print(len(jobs))

# accessing a single element to get the title
#title = jobs[0].find('h2')
### pulling the link from the job 
#title_link = title.find('a')
# this will give you a partial, you need a full url"https.indeed "
#print(title_link['href']) 

### readable link / stripping extra html
#link_text = title_link.text
### clean it up
#print(link_text.strip())
# all together now
job_titles = [job.find('h2').find('a').text.strip() for job in jobs]
print(*job_titles, sep='\n')




#out_put = re.findall(r'python', str(response.content))

#print(out_put[1:8])
