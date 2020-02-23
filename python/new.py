import requests_html
from requests_html import HTMLSession, HTMLResponse


session = HTMLSession()

source =session.get('https://www.imdb.com/movies-in-theaters/?ref_=nv_mv_inth').html
print(source)
boxes=source.find('div.list.detail.sub-list')[0]
print(boxes)
title=boxes.find('.overview-top')[0]
print(title.text)