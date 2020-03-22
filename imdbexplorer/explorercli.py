import easycli
import explorer

__version__ = '0.1.0'


class Top(easycli.SubCommand):
    __command__ = 'top'
    __aliases__ = ['t']
    __arguments__ = [
            easycli.Argument(
                'count',
                type=int,
                default=250,
                help='Maximum number of movies to be shown'
            )
    ]

    def __call__(self, args):
        for movie in explorer.topmovies(count=args.count):
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


