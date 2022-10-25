

from calendar import prcal
from logging.config import listen
from bs4 import BeautifulSoup
import requests
import json
from time import sleep

url= "https://finans.mynet.com/borsa/hisseler/"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# class Basebs4:
#     url= "https://finans.mynet.com/borsa/hisseler/"
#     link_list = []
#     def __init__(self):
#         self.url = Basebs4
#         self.page = requests.get(Basebs4.url)
#         self.soup = BeautifulSoup(self.page.content, 'html.parser')
#     def  get_company_name(self):

#          company_name=[]
#          name = self.soup.findAll( "strong", 'mr-4' )
#          for i in name:
#             company_name_dict = {
#                 "company_name":i.text
#             }
#             print(company_name_dict)
#             company_name.append(company_name_dict)

    
#             with open("company-name.json", "w") as f:
#              json.dump(company_name, f, indent=4)

#     def get_href(self):

#         href = self.soup.findAll('tbody')
#         for i in href:
#             g = i.findAll('a')
#             for j in g:
#                 a= Basebs4.link_list.append(j['href'])
#                 with open("bist.json", "w") as f:
#                     json.dump(Basebs4.link_list, f, indent=4)

#     def  get_data(self):
#         company_name={}
#         listen=[]
#         for url in Basebs4.link_list:

#             page=requests.get(url)
#             name = self.soup.find("h2")
#             data_list_tag={}
#             div =self.soup.find('div',class_='p-3')
#             span = div.findAll('ul')
#             for i in span:   
#                         li = i.findAll('li')
#                         for j in li:
#                             span =j.find('span') #hisse bilgi adları
#                             tag= j.select_one(":nth-child(2)") #hisse bilgi degerleri
#                             data_list_tag[span.text]=tag.text
#                             company_name={
#                                 name.text:data_list_tag
#                             }
#                             print(company_name)
#             listen.append(company_name)
            
#             with open("data-info.json", "w",encoding='utf-8') as f:
#                 json.dump(listen, f, indent=3,ensure_ascii=False)
# base  = Basebs4()
# base.get_href()
# base.get_company_name()
# base.get_data()


                
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
        
    kaynak = "şçöğüıŞÇÖĞÜİ"
    hedef  = "scoguiSCOGUI"

    for url in link_list:
        çeviri_tablosu = str.maketrans(kaynak, hedef)
        
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
                        metin=span.text.translate(çeviri_tablosu).replace(" ","_")
                        data_list_tag[metin]=tag.text
                        company_name={
                            name.text:data_list_tag
                        }
        listen.append(company_name)
        
        with open("data-info.json", "w",encoding='utf-8') as f:
            json.dump(listen, f, indent=3,ensure_ascii=False)


if  __name__ == "__main__":
    get_data()

   


