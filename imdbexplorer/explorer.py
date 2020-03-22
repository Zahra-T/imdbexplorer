import requests
from bs4 import BeautifulSoup
from movie import Movie
import re


def topmovies():
    imdburl = 'https://www.imdb.com'
    url = 'https://www.imdb.com/list/ls068082370/'
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='main')
    movies_content = results.find_all('div', class_='lister-item-content')

    movies = []

    for movie_elem in movies_content:
        header = movie_elem.find('h3', class_='lister-item-header')

        index = header.find('span', class_='lister-item-index unbold text-primary')

        title = header.find('a')
        yearobject = header.find('span', class_='lister-item-year')
        yearpattern = re.compile(r'(\d{4})')
        yearsearch = yearpattern.search(yearobject.text)
        yearnum = None
        if yearsearch:
            yearnum = int(yearsearch.group(0))

        link = title['href']

        description = movie_elem.find('p', class_='')

        moreinfo = movie_elem.find_all('p', class_='text-muted text-small')
        genre = moreinfo[0].find('span', class_='genre')
        duration = moreinfo[0].find('span', class_='runtime')
        director = moreinfo[1].find('a')
        stars = moreinfo[1].find_all('a')[1:-1]
        starlist = []
        for star_elem in stars:
            starlist.append(star_elem.text.strip())

        rate = movie_elem.find('div', class_='ipl-rating-widget').find('span', class_='ipl-rating-star__rating')
        
        movie = Movie(title=title.text.strip(),
                year=yearnum,
                director=director.text.strip(),
                stars = starlist,
                genre=genre.text.strip().split(', '),
                duration=int(duration.text.strip()[0:-4]),
                rate=float(rate.text.strip()), 
                description=description.text.strip())

        movie.setindex(index.text)
        movie.setlink(imdburl+link)
        movies.append(movie)


    return movies


def filter(movies, filterattr, info): 
    filtered = None
    if(filterattr == 'genre'):
        infoset = {item.lower() for item in info}
        filtered = [m for m in movies if  infoset.issubset({item.lower() for item in m.genre})]
    if(filterattr == 'star'):
        infoset = {item.lower() for item in info}
        filtered = [m for m in movies if infoset.issubset({item.lower() for item in m.stars})]
    if(filterattr == 'director'):
        filtered = [m for m in movies if m.director.lower() == info.lower()]
    if(filterattr == 'rate'):#info : a tuple defines start and end of range
        filtered = [m for m in movies if m.rate >= info[0] and m.rate <= info[1]]
    if(filterattr == 'year'):
        filtered = [m for m in movies if m.year in info]
    if(filterattr == 'duration'):
        filtered = [m for m in movies if m.duration >= info[0] and m.duration <= info[1]]
    return filtered



