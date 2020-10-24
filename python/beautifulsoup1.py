import requests_html
from requests_html import HTMLSession, HTMLResponse
from bs4 import BeautifulSoup

urls=[]
for i in range(1,51):
    urls.append(f'http://books.toscrape.com/catalogue/page-3.html')
count =1
for url in urls:
    session = HTMLSession()
    response =session.get('http://books.toscrape.com/').html
    source = response.html
    soup= BeautifulSoup(source,'lxml')
    #print(dir(soup))
    box=soup.find('ol')
    #print(type(box))
    book_title[]
    book_price[]

    elements=box.find_all('li')
    #print(element)

for element in elements:

    title=element.select('h3 a')[0]['title']
    book_title.append(title)
    price=element.find('p',class_='price_color')
    book_price.append
    image=element.find('img')['src']
    image_url='http://books.toscrape.com/'+image
    book_image.append(image_url)
    print (count,end='')
    count=count+1-1

    

    

