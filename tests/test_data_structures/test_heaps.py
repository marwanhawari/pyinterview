import pytest
from pyinterview.data_structures.heaps import *

@pytest.fixture
def nums():
    return [8, 3, 10, 1, 6, 14, 4, 7, 13]
    

def test_min_heap_heapify(nums):
    minheap = MinHeap()
    minheap.heapify(nums)
    assert nums == [1, 3, 4, 7, 6, 14, 10, 8, 13]
    

def test_max_heap_heapify(nums):
    maxheap = MaxHeap()
    maxheap.heapify(nums)
    assert nums == [14, 13, 10, 7, 6, 8, 4, 3, 1]