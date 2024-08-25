import pandas as pd
import requests
from bs4 import BeautifulSoup

URL='https://www.naukri.com/data-analyst-jobs?k=data+analyst'

responce=requests.get(URL)

soup=BeautifulSoup(responce.text,'html.parser')

poster=soup.find(class_='cust-job-tuple layout-wrapper lay-2 sjw__tuple')

jobs=poster.find_all(class_='srp-jobtuple-wrapper')

for job in jobs:
    title=job.find('a').text
    print(title)