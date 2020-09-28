import pytest
from random import randint


def gen_random_int():
    return randint(-1_000_000_000, 1_000_000_000)


def gen_random_odd():
    return 2 * randint(-500_000_000, 500_000_000) + 1


def gen_random_even():
    return 2 * randint(-500_000_000, 500_000_000)


def gen_random_odd_even_pair():
    return gen_random_odd(), gen_random_even()


@pytest.fixture(scope='function')
def gen_big_positive_number():
    return randint(1_000_000_000, 10_000_000_000)


@pytest.fixture(scope='function')
def gen_big_negative_number():
    return randint(-20_000_000_000, -5_000_000_000)


class TestInt:
    class Config:
        PARAMETERS_NUMBER = 20

    @pytest.mark.parametrize('number', [gen_random_int() for _ in range(Config.PARAMETERS_NUMBER)])
    def test_zero_division(self, number):
        with pytest.raises(ZeroDivisionError):
            assert number / 0

    @pytest.mark.parametrize('number', [gen_random_int() for _ in range(Config.PARAMETERS_NUMBER)])
    def test_opposite_sum(self, number):
        subtracting = -number + number
        assert subtracting == 0

    @pytest.mark.parametrize('number', [gen_random_int() for _ in range(Config.PARAMETERS_NUMBER)])
    def test_doubling(self, number):
        assert (number * 2) % 2 == 0

    @pytest.mark.parametrize('numbers', [gen_random_odd_even_pair() for _ in range(Config.PARAMETERS_NUMBER)])
    def test_sum_odd_even(self, numbers):
        assert (numbers[0] + numbers[1]) % 2 == 1

    def test_different_signs_division(self, gen_big_positive_number, gen_big_negative_number):
        assert gen_big_negative_number / gen_big_positive_number < 0




