from bs4 import BeautifulSoup

import random
html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify)


print(soup.a)
print(soup.a.name)
print(soup.a.string)
print(soup.title.parent.name)
print(soup.p.string) # buldugu ilk p  nin strin degerini getirir 

print(soup.p["class"]) 
#<p class="title"><b>The Dormouse's story</b></p>
# ['title']

for link in soup.find_all('a'):
   print(link.get('href'))
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# http://example.com/elsie
# http://example.com/lacie
# http://example.com/tillie

print(soup.find(id='link3').string)

#bütün texleri getirir
print(soup.get_text())

for string in soup.stripped_strings:
    print(repr(string))

dict ={

}

arraylist=[]


counter =0
for x in range(0,10):
   dict["name"]=x
   arraylist.append(dict)
   
   print(x)
   for i in  range(0,10):
      dict["data"]="test"
   arraylist.append(dict)
   
print(arraylist)


#random int