import pandas as pd
import requests
from bs4 import BeautifulSoup

Jobs=[]
for i in range(1,50):

    URL=f'https://www.timesjobs.com/candidate/job-search.html?from=submit&luceneResultSize=25&txtKeywords=0DQT0data%20engineer0DQT0&postWeek=60&searchType=personalizedSearch&actualTxtKeywords=Data%20Engineer&searchBy=0&rdoOperator=OR&pDate=I&sequence=2&startPage={i}'

    responce=requests.get(URL)

    soup=BeautifulSoup(responce.text,'html.parser')

    poster=soup.find('ul',class_='new-joblist')


    jobs=poster.find_all('li',class_='clearfix job-bx wht-shd-bx')



    for job in jobs:
        company=job.find('h3',class_='joblist-comp-name').text.strip()

        profile=job.find('a').text.strip()

        skills=job.find('span',class_='srp-skills').text.strip()
        
        link=job.find('a')['href']

        Jobs.append([company,profile,skills,link])

df=pd.DataFrame(Jobs,columns=['company','profile','skills','link'])
df.to_csv(r"C:\Users\surje\Desktop\GitProject\Jobs.csv",index=False)




