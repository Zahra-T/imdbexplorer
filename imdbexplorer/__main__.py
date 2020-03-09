import requests
from bs4 import BeautifulSoup
from movie import Movie

def topmovies():
    imdburl = 'https://www.imdb.com'
    url = 'https://www.imdb.com/list/ls068082370/?sort=user_rating,desc&st_dt=&mode=detail&pa0ge=1'
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='main')
    movies_content = results.find_all('div', class_='lister-item-content')

    movies = []

    for movie_elem in movies_content:
        header = movie_elem.find('h3')

        index = header.find('span', class_='lister-item-index unbold text-primary')

        title = header.find('a')

        link = title['href']

        description = movie_elem.find('p', class_='')

        moreinfo = movie_elem.find_all('p', class_='text-muted text-small')
        genre = moreinfo[0].find('span', class_='genre')
        director = moreinfo[1].find('a')


        rate = movie_elem.find('div', class_='ipl-rating-widget').find('span', class_='ipl-rating-star__rating')
        movie = Movie(title=title.text, 
                director=director.text, 
                genre=genre.text.strip().split(', '),
                rate=rate.text, 
                description=description.text)

        movie.setindex(index.text)
        movie.setlink(imdburl+link)
        movies.append(movie)

    return movies


def printmovies(movies):
    for movie in movies:
        movie.print()

def filter(movies, filterattr, info): 
    #movies -> list of the movies we want to filter
    #filterattr -> string type of Move class attribute that we want to filter base on that
    filtered = None
    if(filterattr == 'genre'):
        filtered = [m for m in movies if  set(info).issubset({item.lower() for item in getattr(m, filterattr)})]

    return filtered

movies = topmovies()

filtered = filter(movies, 'genre', {'drama'})
print(filtered)
printmovies(filtered)


