from django.core.management.base import BaseCommand
import json
import os


def check_code(code) -> tuple:
    if os.path.isfile('data_file.json'):
        with open('data_file.json', 'r', encoding='utf-8') as f:
            dict_in_file = json.load(f)
            for key in dict_in_file.keys():
                if code in dict_in_file[key]:
                    return True, key
    return False, None


class Command(BaseCommand):
    help = 'Check promo code'

    def handle(self, *args, **options):
        c = options['code']
        if len(c) > 0:
            return repr(check_code(c))

    def add_arguments(self, parser):
        parser.add_argument(
            '-c',
            '--code',
            action='store',
            type=str,
            required=True,
            help='Code to check'
        )