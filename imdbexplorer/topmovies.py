import requests
from bs4 import BeautifulSoup

imdburl = 'https://www.imdb.com'
url = 'https://www.imdb.com/list/ls068082370/?sort=user_rating,desc&st_dt=&mode=detail&page=1'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='main')
movies = results.find_all('div', class_='lister-item-content')

for movie in movies:
    header = movie.find('h3')
    index = header.find('span', class_='lister-item-index unbold text-primary')
    title = header.find('a')
    link = title['href']
    description = movie.find('p', class_='')
    ratingstar = movie.find('div', class_='ipl-rating-widget').find('span', class_='ipl-rating-star__rating')

    print(f'{index.text}{title.text}')
    print(f'Star: {ratingstar.text}')
    print(f'Description:{description.text}')
    print(f'imdb page:{imdburl}{link}')
    print()





