import argparse
from gooey import Gooey

@Gooey
def main():
    parser = argparse.ArgumentParser(description='Get highest int in a list.')
    parser.add_argument('integers',
                        metavar='N',
                        type=int,
                        nargs='+',
                        help="enter list of integers")
    parser.add_argument('--sum',
                        dest='accumulate',
                        action='store_const',
                        const=sum,
                        default=max,
                        help='sum the integers (default: find the max)')

    args= parser.parse_args()
    print(args.accumulate(args.integers))

if __name__ == "__main__":
    main()

