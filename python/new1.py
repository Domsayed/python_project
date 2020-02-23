import reqwuests_html
from requests_html import HTMLSession, HTMLResponse
from bs4 import BeautifulSoup

session = HTMLSession()
response =session.get('http://quotes.toscrape.com/').html
source = response.html
phars=[]
#element=[]

soup= BeautifulSoup(source,'lxml')
boxs=soup.select('.quote')
for box in boxs:
    #element=box.find_all('div')
    phars=box.find_all('span')[0]
    
    print(phars.text)
