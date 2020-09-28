from django.core.management.base import BaseCommand
import secrets, string
import json
from _vars import *


def make_code(n: int) -> str:
    return ''.join(secrets.choice(string.ascii_letters + string.digits) for i in range(n))


def check_duplicates(dict_in_file, a_list) -> list:
    for code in a_list:
        for key in dict_in_file.keys():
            if code in dict_in_file[key]:
                code = make_code(CODE_LEN)
    return a_list


def save_data(a_list, g) -> bool:
    dict_in_file = {}
    try:
        f = open('data_file.json', 'r+', encoding='utf-8')
        dict_in_file = json.load(f)
        a_list = check_duplicates(dict_in_file, a_list)
        f.close()
    except:
        pass
    with open('data_file.json', 'w+', encoding='utf-8') as f:
        if g in dict_in_file.keys():
            dict_in_file[g].extend(a_list)
        else:
            dict_in_file[g] = a_list
        json.dump(dict_in_file, f, ensure_ascii=False)
        return True


def generate_codes(a: int, g: str) -> bool:
    a_list = []
    for i in range(a):
        a_list.append(make_code(CODE_LEN))

    return save_data(a_list, g)


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
