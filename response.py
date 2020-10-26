import requests
import re

url = "https://www.indeed.com/jobs?q=python&l=Dallas%2C+TX&radius=35"
response = requests.get(url)

outp = re.findall(r'python', str(response.content))

print(outp)

input()
