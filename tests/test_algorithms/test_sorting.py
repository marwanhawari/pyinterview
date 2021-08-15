import pytest
from pyinterview.algorithms.sorting import topological_sort

def test_topological_sort():
    assert topological_sort([(1,3),(1,2)]) == [2, 3, 1]
    
def test_topological_sort_cycle():
    assert topological_sort([(1,2),(2,3),(3, 1)]) == []