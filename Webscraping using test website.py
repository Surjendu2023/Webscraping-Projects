import requests
from bs4 import BeautifulSoup
import pandas as pd


URL='https://webscraper.io/test-sites/e-commerce/allinone'

responce=requests.get(URL)

# print(responce)

soup=BeautifulSoup(responce.text,'html.parser')

# title=soup.find('title').text.strip()
# paragraph=soup.find('p',class_='lead').text.strip()


#box=soup.find_all('div',class_='col-md-4 col-xl-4 col-lg-4')

productname=soup.find_all('p',class_='description card-text')

price=soup.find_all('h4',class_='price float-end card-title pull-right')

productlink=soup.find_all('a',class_='title')

print(price)

# product_list=[]
# for i in productname:
#     name=i.text.strip()
#     product_list.append(name)

# price_list=[]
# for i in price:
#     prices=i.text.strip()
#     price_list.append(prices)


# links=[]
# for i in productlink:
#     link="https://webscraper.io"+i.get('href')
#     links.append(link)


# df=pd.DataFrame({"Product Name":product_list,"Prices":price_list,"Product Link":links})

# df.to_csv(r'C:\Users\surje\Desktop\GitProject\data.csv',index=False)