from django.core.management.base import BaseCommand
import secrets, string
import json


def make_code(n: int) -> str:
    return ''.join(secrets.choice(string.ascii_letters + string.digits) for i in range(n))


def save_data(a_list, g):
    infile = {}
    try:
        f = open('data_file.json', 'r+')
        infile = json.load(f)
        f.close()
    except:
        pass
    with open('data_file.json', 'w+') as f:
        if g in infile.keys():
            infile[g].extend(a_list)
        else:
            infile[g] = a_list
        json.dump(infile, f)


def generate_codes(a: int, g: str) -> bool:
    a_list = []
    for i in range(a):
        a_list.append(make_code(7))

    save_data(a_list, g)


class Command(BaseCommand):
    help = 'Generate promo codes'

    def handle(self, *args, **options):
        a = options['amount']
        g = options['group']
        if (a > 0) and (len(g) > 0):
            if generate_codes(a, g):
                return ('Codes generates successful')

    def add_arguments(self, parser):
        parser.add_argument(
            '-a',
            '--amount',
            action='store',
            type=int,
            required=True,
            help='Amount of codes'
        )
        parser.add_argument(
            '-g',
            '--group',
            action='store',
            type=str,
            required=True,
            help='Group of codes'
        )


if __name__ == '__main__':
    generate_codes(2, 'test1')