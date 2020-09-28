from django.test import TestCase
from io import StringIO
from django.core.management import call_command
import os
import json
import random


def check_codes_len() -> tuple:
    l = 0
    if os.path.isfile('data_file.json'):
        with open('data_file.json', 'r', encoding='utf-8') as f:
            dict_in_file = json.load(f)
            for key in dict_in_file.keys():
                l += len(dict_in_file[key])

    return l, len(dict_in_file)


def get_random_code() -> str:
    if os.path.isfile('data_file.json'):
        with open('data_file.json', 'r', encoding='utf-8') as f:
            dict_in_file = json.load(f)
            random_code = random.choice(dict_in_file[random.choice(list(dict_in_file.keys()))])
            return random_code


class GeneratorTest(TestCase):

    def test1_generate_codes(self):
        '''
        Create 58 promo codes and check this
        '''

        if os.path.isfile('data_file.json'):
            os.remove('data_file.json')

        out = StringIO()
        call_command('gen', '-a=10', '-g=агенства', stdout=out)
        self.assertIn('Codes generates successful', out.getvalue())

        call_command('gen', '-a=1', '-g=агенства', stdout=out)
        self.assertIn('Codes generates successful', out.getvalue())

        call_command('gen', '-a=42', '-g=avtostop', stdout=out)
        self.assertIn('Codes generates successful', out.getvalue())

        call_command('gen', '-a=5', '-g=1', stdout=out)
        self.assertIn('Codes generates successful', out.getvalue())

        self.assertEqual((58, 3), check_codes_len())

    def test2_check_code(self):
        '''
        Check code in JSON
        '''

        out = StringIO()
        call_command('chk', '-c={}'.format(get_random_code()), stdout=out)
        self.assertIn('True', out.getvalue())