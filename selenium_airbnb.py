import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
options = Options()

#options.add_argument('--headless')

options.add_argument('window-size=400,800')

navegador = webdriver.Chrome(options=options)

navegador.get('https://www.airbnb.com')

sleep(2)

input_place = navegador.find_element_by_tag_name('input')
input_place.send_keys('São Paulo')
input_place.submit()

sleep(0.5)

button_stay = navegador.find_element_by_css_selector('button > img')
button_stay.click()




# site = BeautifulSoup(navegador.page_source, 'html.parser')

# print(site.prettify())
