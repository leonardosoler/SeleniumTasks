import requests
from bs4 import BeautifulSoup


response = requests.get('https://g1.globo.com/')

content = response.content

site = BeautifulSoup(content, 'html.parser')

noticia = site.find('div', attrs={'class' : 'feed-post-body'} )

print(noticia.prettify())