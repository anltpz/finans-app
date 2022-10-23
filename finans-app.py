

from calendar import prcal
from logging.config import listen
from bs4 import BeautifulSoup
import requests
import json
from time import sleep

url= "https://finans.mynet.com/borsa/hisseler/"

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')


name = soup.findAll( "strong", 'mr-4' )
company_name=[]
for i in name:
    company_name_dict = {
        "company_name":i.text
    }
    company_name.append(company_name_dict)

    
    with open("company-name.json", "w") as f:
     json.dump(company_name, f, indent=4)

#hrefleri getir
link_list = []
href = soup.findAll('tbody')
for i in href:
      g = i.findAll('a')
      for j in g:
         a= link_list.append(j['href'])
         with open("bist.json", "w") as f:
          json.dump(link_list, f, indent=4)



def get_data():
    company_name={}
    listen=[]
    for url in link_list:

        page=requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        name = soup.find("h2")
        data_list_tag={}
        div =soup.find('div',class_='p-3')
        span = div.findAll('ul')
        for i in span:   
                    li = i.findAll('li')
                    for j in li:
                        span =j.find('span') #hisse bilgi adları
                        tag= j.select_one(":nth-child(2)") #hisse bilgi degerleri
                        data_list_tag[span.text]=tag.text
                        company_name={
                            name.text:data_list_tag
                        }
                        print(company_name)
        listen.append(company_name)
        
        with open("data-info.json", "w",encoding='utf-8') as f:
            json.dump(listen, f, indent=3,ensure_ascii=False)

get_data()
   


