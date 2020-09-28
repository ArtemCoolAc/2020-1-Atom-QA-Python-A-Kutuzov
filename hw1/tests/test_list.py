import pytest
import random
import copy


@pytest.fixture(scope='function')
def gen_non_unique_list():
    quantity = random.randint(5, 20)
    element = random.randint(5, 10)
    first_list = [element] * quantity + \
                 [random.randint(1000, 2000) for _ in range(random.randint(10, 100))]
    random.shuffle(first_list)
    return first_list, element, quantity


@pytest.fixture(scope='function')
def gen_list():
    return [random.randint(-1000, 1000) for _ in range(random.randint(10, 1000))]


class TestList:
    class Config:
        REPEATS_NUMBER = 30

    def test_method_resolution_order(self):
        assert list.mro() == [list, object]

    def test_count(self, gen_non_unique_list):
        some_list, element, quantity = gen_non_unique_list
        assert some_list.count(element) == quantity

    def test_append(self, gen_list):
        first_list = gen_list
        second_list = gen_list
        first_list.append(second_list)
        assert first_list[-1] == second_list

    def test_reverse(self, gen_list):
        copied_list = copy.deepcopy(gen_list)
        copied_list.reverse()
        assert copied_list == gen_list[::-1]

    @pytest.mark.parametrize('element', list(range(Config.REPEATS_NUMBER)))
    def test_append_one_element(self, element, gen_list):
        gen_list.append(element)
        assert gen_list[-1] == element
