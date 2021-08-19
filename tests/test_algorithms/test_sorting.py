import pytest
from pyinterview.algorithms.sorting import quick_sort, merge_sort, topological_sort

def test_quick_sort():
    assert quick_sort([5,1,2,6,7,0,9]) == [0,1,2,5,6,7,9]
    assert quick_sort([9,8,7,6,5,4,3,2,1]) == [1,2,3,4,5,6,7,8,9]
    assert quick_sort([23.4,12.33,4.2,8]) == [4.2,8,12.33,23.4]

def test_quick_sort_duplicates():
    assert quick_sort([5,1,1,2,0,0]) == [0,0,1,1,2,5]

def test_quick_sort_edge():
    assert quick_sort([]) == []


def test_merge_sort():
    assert merge_sort([5,1,2,6,7,0,9]) == [0,1,2,5,6,7,9]
    assert merge_sort([9,8,7,6,5,4,3,2,1]) == [1,2,3,4,5,6,7,8,9]
    assert merge_sort([23.4,12.33,4.2,8]) == [4.2,8,12.33,23.4]

def test_merge_sort_duplicates():
    assert merge_sort([5,1,1,2,0,0]) == [0,0,1,1,2,5]

def test_merge_sort_edge():
    assert merge_sort([]) == []


def test_topological_sort():
    assert topological_sort([(1,3),(1,2)]) == [2, 3, 1]
    
def test_topological_sort_cycle():
    assert topological_sort([(1,2),(2,3),(3, 1)]) == []