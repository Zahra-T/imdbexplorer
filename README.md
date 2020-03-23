# imdbexplorer

A web scraper to extract movie information out of imdb website
and show them in terminal.
also you can filter them by specific movie attributes.

### Installation
```
pip3 install .
imdb completion install
```

### Usage

```
imdb [-h] [-v] {top,t} ...
```

### Optional arguments
```
  -h, --help     show this help message and exit
  -v, --version  Show version
```

### Sub commands
```
{top, t}:

usage: imdb top [-h] [-c COUNT] [-y YEAR] [-g GENRE] [-d DIRECTOR] [-s STAR]

optional arguments:
  -h, --help            show this help message and exit
  -c COUNT, --count COUNT
                        Maximum number of movies to be shown
  -y YEAR, --year YEAR  Production year of the movies
  -g GENRE, --genre GENRE
                        Genre of the movies
  -d DIRECTOR, --director DIRECTOR
                        Director of the movies
  -s STAR, --star STAR  The star who have acted in the movie
```
