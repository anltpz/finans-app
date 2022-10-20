
from distutils.log import info
from itertools import count
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

data_info_dict = {}
data_list={}
data_n=[]
for url in link_list:
       page=requests.get(url)
       soup = BeautifulSoup(page.content, 'html.parser')
       name = soup.find("h2")
       print(name.text)
       div =soup.find('div',class_='p-3')
       span = div.findAll('ul')
       data_info_dict["name"]=name.text  
       for i in span:
          li = i.findAll('li')
          for j in li:
                span =j.find('span') #hisse bilgi adları
                tag= j.select_one(":nth-child(2)") #hisse bilgi degerleri
                data_info_dict[span.text]=tag.text
       text = {
          "name":name.text,
          "data":data_info_dict
           }
       data_n.append(text)

       
       with open("data-info.json", "w",encoding='utf-8') as f:
          json.dump(data_n, f, indent=3,ensure_ascii=False)



   
    
