import easycli


__version__ = '0.1.0'


class Explorer:
    __help__ = 'Easy imdb explorer'
    __arguments__ = [
            easycli.Argument(
                '-v', '--version',
                action='store_true',
                help='Show version'
            ),
        ]

    def __call__(self, args):
        if args.version:
            print(__version__)
            return

        return super().__call__(args)


