import requests
import pandas as pd
from bs4 import BeautifulSoup
import cx_Oracle
from sqlalchemy import create_engine



engine=create_engine('oracle+cx_oracle://System:admin@localhost:1521/xe')

connection=engine.connect()

books=[]
for i in range(1,1):

    URL=f'https://books.toscrape.com/catalogue/page-{i}.html'

    responce=requests.get(URL)

    soup=BeautifulSoup(responce.content,'html.parser')

    list=soup.find('ol',class_='row')

    articles=list.find_all('article',class_='product_pod')


    for article in articles :
        img=article.find('img')
        title=img.attrs['alt']
        star=article.find('p')
        star=star['class'][1]
        price=article.find('p',class_='price_color').text
        price=float(price[1:])
        availability=article.find('p',class_='instock availability').text.strip()
        books.append([title])

        df=pd.DataFrame(books,columns=['TITLE'])
        df.to_sql('books',engine,index=False,if_exists='append')

connection.close()