import pytest
import random
import copy


@pytest.fixture(scope='module')
def gen_set():
    return {random.randint(-1_000, 1_000) for _ in range(random.randint(2, 100))}


@pytest.fixture(scope='function')
def gen_two_connected_sets(gen_set):
    first_set = gen_set
    second_set = first_set.union(gen_set)
    return first_set, second_set


def gen_one_separate_set(start, stop):
    return {random.randint(start, stop) for _ in range(random.randint(0, 100))}


def gen_two_separate_sets():
    return gen_one_separate_set(1000, 2000), gen_one_separate_set(3000, 4000)


class TestSet:
    class Config:
        REPEATS_NUMBER = 50

    def test_subset(self, gen_two_connected_sets):
        first_set, second_set = gen_two_connected_sets
        assert first_set.issubset(second_set)

    def test_superset(self, gen_two_connected_sets):
        first_set, second_set = gen_two_connected_sets
        assert second_set.issuperset(first_set)

    @pytest.mark.parametrize('sets', [gen_two_separate_sets() for _ in range(Config.REPEATS_NUMBER)])
    def test_difference(self, sets):
        assert sets[0].difference(sets[1]) == sets[0]

    @pytest.mark.parametrize('elem', [random.randint(-1000, 1000) for _ in range(Config.REPEATS_NUMBER)])
    def test_discard(self, elem, gen_set):
        copied_set = copy.deepcopy(gen_set)
        gen_set.discard(elem)
        if elem in copied_set:
            assert copied_set.difference(gen_set).pop() == elem
        else:
            assert copied_set == gen_set

    def test_method_resolution_order(self):
        assert set.mro() == [set, object]
