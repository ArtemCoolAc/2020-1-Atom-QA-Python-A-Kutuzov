import pytest
import string
import random

symbols = string.ascii_letters + string.digits
digits = string.digits


@pytest.fixture(scope='function')
def gen_str():
    return ''.join([random.choice(symbols) for _ in range(100)])


@pytest.fixture(scope='function')
def gen_digits_str():
    return ''.join([random.choice(digits) for _ in  range(100)])


def gen_random_str():
    return ''.join([random.choice(symbols) for _ in range(150)])


class TestString:
    class Config:
        REPEATS_NUMBER = 50

    def test_multiplying(self, gen_str):
        assert gen_str * 2 == gen_str + gen_str

    @pytest.mark.parametrize('string', [gen_random_str() for _ in range(Config.REPEATS_NUMBER)])
    def test_capitalize(self, string):
        first_symbol = string[0]
        assert first_symbol.capitalize() + string[1:].lower() == string.capitalize()

    def test_isalnum(self, gen_digits_str):
        assert type(int(gen_digits_str)) == int

    def test_normal_string_strip(self, gen_str):
        assert gen_str == gen_str.strip()

    def test_reverse_of_reverse(self, gen_str):
        assert gen_str == gen_str[::-1][::-1]
