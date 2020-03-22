import easycli
import explorer

__version__ = '0.1.0'


class Top(easycli.SubCommand):
    __command__ = 'top'
    __aliases__ = ['t']
    __arguments__ = [
            easycli.Argument(
                '-c', '--count',
                type=int,
                default=250,
                help='Maximum number of movies to be shown'
            ),
            easycli.Argument(
                '-y', '--year',
                type=int,
                action='append',
                help='Production year of the movies'
            ),
            easycli.Argument(
                '-g', '--genre',
                type=str,
                action='append',
                help='Genre of the movies'
            )
    ]


    def __call__(self, args):
        movies = explorer.topmovies()
        if args.year:
            movies = explorer.filter(movies, 'year', args.year)
        if args.genre:
            movies = explorer.filter(movies, 'genre', args.genre)
        movies = movies[:min(args.count, len(movies))]

        for movie in movies:
            movie.print()


class Explorer(easycli.Root):
    __help__ = 'Easy imdb explorer'
    __arguments__ = [
            easycli.Argument(
                '-v', '--version',
                action='store_true',
                help='Show version'
            ),
            Top
        ]

    def __call__(self, args):
        if args.version:
            print(__version__)
            return

        return super().__call__(args)


