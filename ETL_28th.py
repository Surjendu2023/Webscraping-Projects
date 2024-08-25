

import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime

Names=[]

Prices=[]


for page_num in range(1,101):
    URL=f'https://www.flipkart.com/search?q=Laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY&page={page_num}'

    responce=requests.get(URL)

    #print(responce.status_code)

    soup=BeautifulSoup(responce.text,'html.parser')

    name=soup.find_all('div',class_='KzDlHZ')

    price=soup.find_all('div',class_='Nx9bqj _4b5DiR')



    for i in name:
        mobile=i.text.strip()
        Names.append(mobile)

    
    for i in price:
        nprice=i.text.strip()[1:]
        Prices.append(nprice)
        
    df=pd.DataFrame({"Model Name":Names,"Price":Prices})
    df.to_csv(r'C:\Users\surje\Desktop\GitProject\data.csv',index=False)
    



