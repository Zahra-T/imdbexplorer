

class Movie:

    def __init__(self, title, year, director, stars,  genre, duration, rate, description):
        self.title = title
        self.director = director
        self.stars = stars
        self.year = year
        self.rate = rate
        self.description = description
        self.genre = genre #a set of movie genres
        self.duration = duration

    def setindex(self, index):
        self.index = index

    def setlink(self, imdblink):
        self.imdblink = imdblink

    def print(self):
        print(f'{self.index}{self.title}')
        print(f'Year: {self.year}')
        print(f'Genre: {self.genre}')
        print(f'Duration: {self.duration}')
        print(f'Rate: {self.rate}')
        print(f'Director: {self.director}')
        print(f'Stars: {self.stars}')
        print(f'Description:{self.description}')
        print(f'imdb page:{self.imdblink}')
        print()
