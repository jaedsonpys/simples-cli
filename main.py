import argparse
from datetime import datetime

parser = argparse.ArgumentParser(description='Simples ferramenta CLI')
parser.add_argument('--time', action='store_true')
parser.add_argument('--date', action='store_true')

args = parser.parse_args()


def main():
    if args.date:
        time = datetime.now().strftime('%D')
        print(f'Data: {time}')

    if args.time:
        time = datetime.now().strftime('%H:%m')
        print(f'Horário: {time}')


main()
