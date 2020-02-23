import requests_html
from requests_html import HTMLSession, HTMLResponse


session = HTMLSession()

source =session.get('https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm').html
#print(type(source.html))
#source.render()
#blocks = source.find('#test')

body=source.find('.lister-list')[0]
#print(body)

matches =body.find('tr')
for match in matches:

    title = match.find('.titleColumn a')[0]
    print(title.text)
    
    rating=match.find('td.ratingColumn.imdbRating')[0]
    print(rating.text)