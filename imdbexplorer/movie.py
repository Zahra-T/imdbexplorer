

class Movie:

    def __init__(self, title, director, genres, rate, description):
        self.title = title
        self.director = director
        self.rate = rate
        self.description = description
        self.genres = genres #a set of movie genres

    def setindex(self, index):
        self.index = index

    def setlink(self, imdblink):
        self.imdblink = imdblink

    def print(self):
        print(f'{self.index}{self.title}')
        print(f'Genre: {self.genres}')
        print(f'Rate: {self.rate}')
        print(f'Director: {self.director}')
        print(f'Description:{self.description}')
        print(f'imdb page:{self.imdblink}')
        print()
