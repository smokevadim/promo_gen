from django.test import TestCase
from io import StringIO
from django.core.management import call_command
import os
import json


def check_codes_len() -> tuple:
    l = 0
    if os.path.isfile('data_file.json'):
        with open('data_file.json', 'r', encoding='utf-8') as f:
            dict_in_file = json.load(f)
            for key in dict_in_file.keys():
                l += len(dict_in_file[key])

    return l, len(dict_in_file)


class GeneratorTest(TestCase):

    def test_generate_codes(self):
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