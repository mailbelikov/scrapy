import requests
from bs4 import BeautifulSoup as bs

site = requests.get('https://habr.com/ru/news')
print(f'Read habr.com status: {site}')

habr = bs(site.text, 'lxml')

news = habr.find_all('a', class_='tm-article-snippet__title-link')

for el in news:
    print(el.attrs['href'])
    print(el.span.text)
    print('')

site.close()
