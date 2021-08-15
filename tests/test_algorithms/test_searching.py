import pytest
from pyinterview.algorithms.searching import binary_search

@pytest.fixture
def empty_array():
    return []

@pytest.fixture
def unsorted_array():
    return [2,9,1,7,8]

@pytest.mark.parametrize(("array"), [
    ([1,2,3,4,5]),
    ([-1,2,3,4,10])
])
@pytest.mark.parametrize(("target", "output"),
[
    (2, 1),
    (3, 2),
    (4, 3)
    ])
def test_binary_search_hit(array, target, output):
    assert binary_search(array, target) == output 

def test_binary_search_miss():
    assert binary_search([1,2,3,4,5], 6) == -1

def test_binary_search_edge(empty_array):
    assert binary_search(empty_array, 0) == -1

def test_binary_search_unsorted(unsorted_array):
    assert binary_search(unsorted_array, 9) == -1