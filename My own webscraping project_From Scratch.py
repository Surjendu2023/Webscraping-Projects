
import requests
from bs4 import BeautifulSoup
import pandas as pd


try:
    URL='https://quotes.toscrape.com/page/1/'
    responce=requests.get(URL)
    soup=BeautifulSoup(responce.content,'html.parser')
    content=soup.find_all('span',class_='text')
    author=soup.find_all('small',class_='author')
    
    contentfile=[]
    for contents in content:
        contentfile.append(contents.text.strip()[1:-1])

    authorfile=[]
    for authors in author:
        authorfile.append(authors.text.strip())


except Exception as e:
    print('A problem occur :',e)

else:
    df=pd.DataFrame({'content':contentfile,
                     'author':authorfile})
    df.to_csv(r"C:\Users\surje\Desktop\GitProject\sample.csv",index=False)


