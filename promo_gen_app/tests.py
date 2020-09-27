from django.test import TestCase
from io import StringIO
from django.core.management import call_command


class GeneratorTest(TestCase):
    def test_generate_codes(self):
        out = StringIO()
        call_command('gen', '-a 10', '-g test', stdout=out)
        self.assertIn('Codes generates successful', out.getvalue())
