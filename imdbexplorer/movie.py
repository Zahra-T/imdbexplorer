

class Movie:

    def __init__(self, title, year, director, genre, rate, description):
        self.title = title
        self.director = director
        self.year = year
        self.rate = rate
        self.description = description
        self.genre = genre #a set of movie genres

    def setindex(self, index):
        self.index = index

    def setlink(self, imdblink):
        self.imdblink = imdblink

    def print(self):
        print(f'{self.index}{self.title}')
        print(f'Year: {self.year}')
        print(f'Genre: {self.genre}')
        print(f'Rate: {self.rate}')
        print(f'Director: {self.director}')
        print(f'Description:{self.description}')
        print(f'imdb page:{self.imdblink}')
        print()
