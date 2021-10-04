import requests
from bs4 import BeautifulSoup

url_base = 'https://lista.mercadolivre.com.br/'

produto_nome = input('Qual produto você deseja?')

response = requests.get(url_base + produto_nome)

# content = response.content

site = BeautifulSoup(response.text, 'html.parser')



# #HTML da noticia
produtos = site.findAll('div', attrs={
                    'class': 'andes-card andes-card--flat andes-card--default ui-search-result ui-search-result--core andes-card--padding-default'})

#print(produto.prettify())
# print('Titulo do produto :', titulo.text)
# print('Link do produto :', link['href'])
# print('Preço do produto : R$', real.text + ',' + centavos.text)



for produto in produtos:
    #Titulo

    titulo = produto.find('h2', attrs={ 'class': 'ui-search-item__title'})
    link = produto.find('a', attrs={ 'class': 'ui-search-item__group__element ui-search-link'})

    real = produto.find('span', attrs={ 'class': 'price-tag-fraction'})
    centavos = produto.find('span', attrs={ 'class': 'price-tag-cents'})

    print('Titulo do produto :', titulo.text)
    print('Link do produto :', link['href'])
    if (centavos):
        print('Preço do produto : R$', real.text + ',' + centavos.text)
    else:
        print('Preço do produto : R$', real.text)
    

    print('\n\n')