
import requests
from bs4 import BeautifulSoup
import time

def getscore():
    try:
        time.sleep(60)  # wait for 60 sec
        URL=(f"https://www.espncricinfo.com/series/duleep-trophy-2024-25-1445823/india-a-vs-india-d-3rd-match-1445834/live-cricket-score")
        responce=requests.get(URL)
        soup=BeautifulSoup(responce.text,'html.parser')
        score=soup.find('div',class_='ds-text-compact-m ds-text-typo ds-text-right ds-whitespace-nowrap').text.strip()
        notify(score) #getting data from getscore then triger notification
        
    except Exception as  e:
        error=('there is an error {}'.format(e))
        notify(error)
        
    else:
        pass  #place holder
        
    finally:
        pass  #place holder


def notify(msg):
    token='6653752665:AAGeGEqnSaraeY1dHNGjGLY-GEyyhDfCxgU'
    chat_id='1702937489'
    message=(f'current score is : {msg}')
    trigger=f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
    print(requests.get(trigger))