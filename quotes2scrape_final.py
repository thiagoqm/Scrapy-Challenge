from helium import *
from bs4 import BeautifulSoup
import sys
import json

from datetime import datetime


        
url = 'http://quotes.toscrape.com/js/'
browser = start_chrome(url, headless=True)
global fator
fator = 1

soup = BeautifulSoup(browser.page_source, 'html.parser')



lista = []

def parsing():
    quotes = soup.find_all('div', {'class': 'quote'})
    for i in quotes:
        text = i.find('span', {'class': 'text'}).text
        tags = i.find('div', {'class': 'tags'}).text
        author = i.find('small', {'class': 'author'}).text
        output = [
        {'Quote':text, 
        'tags*':tags,
        'author':author}
        ]
        
        lista.append(output)
        

a = parsing()

h = browser.page_source
 
while 'next' in h:
    fator = fator + 1
    browser.get('http://quotes.toscrape.com/js/'+f'/page/{fator}/')
    print(browser.current_url)
    h = browser.page_source
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    a = parsing()

t = datetime.now()
d = t.strftime("%d-%m-%Y %H-%M-%S")

with open(f'scraped_quotes_{d}.json', 'w', encoding="utf-8") as f:
    json.dump(lista, f, ensure_ascii=False, indent=4)

kill_browser()



            

    
    
    

    

   
    
