import pytest
import random
import string
import copy

symbols = string.ascii_letters + string.digits


@pytest.fixture(scope='function')
def gen_int():
    return random.randint(-1_000_000_000, 1_000_000_000)


@pytest.fixture(scope='function')
def gen_str():
    return ''.join([random.choice(symbols) for _ in range(random.randint(0, 15))])


@pytest.fixture(scope='function')
def gen_list(gen_str):
    return [gen_str for _ in range(random.randint(1, 40))]


@pytest.fixture(scope='function')
def gen_dict(gen_list, gen_int):
    return dict.fromkeys(gen_list, gen_int)


@pytest.fixture(scope='function')
def gen_two_dicts(gen_dict):
    return gen_dict, gen_dict


def gen_simple_dict():
    return {k: v for k, v in
            [(random.randint(0, 1000), random.randint(5000, 6000)) for _ in range(20)]
            }


class TestDict:
    class Config:
        REPEATS_NUMBER = 400

    def test_from_keys(self, gen_dict):
        default_value = list(gen_dict.values())[0]
        for value in gen_dict.values():
            assert value == default_value

    def test_clear(self, gen_dict):
        assert len(gen_dict) != 0
        gen_dict.clear()
        assert len(gen_dict) == 0

    def test_update(self, gen_two_dicts):
        first_dict, second_dict = gen_two_dicts
        first_dict_copy = copy.deepcopy(first_dict)
        second_dict_copy = copy.deepcopy(second_dict)
        first_dict_copy.update(second_dict_copy)
        for key, value in first_dict_copy.items():
            if key not in first_dict.keys() and key not in second_dict.keys():
                raise KeyError("Strange key error")
            elif key in second_dict.keys():
                assert value == second_dict[key]
            else:
                assert value == first_dict[key]

    @pytest.mark.parametrize('key', [random.randint(0, 1000) for _ in range(Config.REPEATS_NUMBER)])
    def test_pop(self, key):
        gen_dict = gen_simple_dict()
        value = gen_dict[key] if key in gen_dict else ''
        is_key = key in gen_dict
        extracted_value = gen_dict.pop(key, 'Fail')
        if is_key:
            assert value == extracted_value
        else:
            assert 'Fail' == extracted_value

    @pytest.mark.parametrize('key', [random.randint(0, 1000) for _ in range(Config.REPEATS_NUMBER)])
    def test_get(self, key):
        gen_dict = gen_simple_dict()
        returned_value = gen_dict.get(key, 'Not Found')
        if key in gen_dict:
            assert returned_value == gen_dict[key]
        else:
            assert returned_value == 'Not Found'
