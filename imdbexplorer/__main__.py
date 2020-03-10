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
        header = movie_elem.find('h3', class_='lister-item-header')

        index = header.find('span', class_='lister-item-index unbold text-primary')

        title = header.find('a')
        year = header.find('span', class_='lister-item-year')

        link = title['href']

        description = movie_elem.find('p', class_='')

        moreinfo = movie_elem.find_all('p', class_='text-muted text-small')
        genre = moreinfo[0].find('span', class_='genre')
        director = moreinfo[1].find('a')
        stars = moreinfo[1].find_all('a')[1:-1]
        starlist = []
        for star_elem in stars:
            starlist.append(star_elem.text.strip())

        rate = movie_elem.find('div', class_='ipl-rating-widget').find('span', class_='ipl-rating-star__rating')
        
        movie = Movie(title=title.text.strip(),
                year=int(year.text.strip()[1:-1]),
                director=director.text.strip(),
                stars = starlist,
                genre=genre.text.strip().split(', '),
                rate=float(rate.text.strip()), 
                description=description.text.strip())

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
        filtered = [m for m in movies if  set(info).issubset({item.lower() for item in m.genre})]
    if(filterattr == 'director'):
        filtered = [m for m in movies if m.director.lower() == info.lower()]
    if(filterattr == 'rate'):#info : a tuple defines start and end of range
        filtered = [m for m in movies if m.rate >= info[0] and m.rate <= info[1]]
    if(filterattr == 'year'):
        filtered = [m for m in movies if m.year >= info[0] and m.year <=info[1]]
    return filtered

movies = topmovies()
#print(printmovies(movies))
filtered = filter(movies, 'year', (1990, 2000))
print(filtered)
printmovies(filtered)


