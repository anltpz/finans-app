

from bs4 import BeautifulSoup
import requests
import json

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


data_n=[]
span_data=[]
data_list_tag={}
for url in link_list:
       page=requests.get(url)
       soup = BeautifulSoup(page.content, 'html.parser')
       name = soup.find("h2")
       div =soup.find('div',class_='p-3')
       data_list_tag={"name:":name.text}
       span = div.findAll('ul')
       for i in span:
            li = i.findAll('li')
            for j in li:
                span =j.find('span') #hisse bilgi adları
                tag= j.select_one(":nth-child(2)") #hisse bilgi degerleri
                data_list_tag[span.text]=tag.text
                print(data_list_tag)
       data_n.append(data_list_tag)
       
       
       with open("data-info.json", "w",encoding='utf-8') as f:
          json.dump(data_n, f, indent=3,ensure_ascii=False)



   
    
