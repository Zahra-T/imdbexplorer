import requests
from bs4 import BeautifulSoup
from movie import Movie

imdburl = 'https://www.imdb.com'
url = 'https://www.imdb.com/list/ls068082370/?sort=user_rating,desc&st_dt=&mode=detail&pa0ge=1'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='main')
movies = results.find_all('div', class_='lister-item-content')

for movie_elem in movies:
    header = movie_elem.find('h3')
    index = header.find('span', class_='lister-item-index unbold text-primary')
    title = header.find('a')
    link = title['href']
    description = movie_elem.find('p', class_='')
    director = movie_elem.find_all('p', class_='text-muted text-small')[1].find('a')
    rate = movie_elem.find('div', class_='ipl-rating-widget').find('span', class_='ipl-rating-star__rating')

    movie = Movie(title.text, director.text, rate.text, description.text)
    movie.setindex(index.text)
    movie.setlink(link)
    movie.print()
