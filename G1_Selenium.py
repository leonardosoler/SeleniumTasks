import requests
from bs4 import BeautifulSoup


response = requests.get('https://g1.globo.com/')

content = response.content

site = BeautifulSoup(content, 'html.parser')

#HTML da noticia
noticias = site.findAll('div', attrs={'class' : 'feed-post-body'} )

for noticia in noticias:
    #Titulo
    titulo = noticia.find('a', attrs= {'class': 'feed-post-link'})

    subtitulo = noticia.find('a', attrs={'class': 'feed-post-body-title'})
    if (subtitulo):
        print("Subtitulo : " + subtitulo.text)

        #print(noticia.prettify())

    print("Titulo : " + titulo.text)

    