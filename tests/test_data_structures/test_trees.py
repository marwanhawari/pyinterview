import pytest
from pyinterview.data_structures.trees import *

@pytest.fixture
def root():
    return deserialize([8, 3, 10, 1, 6, 'X', 14, 'X', 'X', 4, 7, 13, 'X', 'X', 'X', 'X', 'X', 'X', 'X'])
    
def test_in_order_traversal(root):
    assert in_order_traversal(root) == [1, 3, 4, 6, 7, 8, 10, 13, 14]    
def test_in_order_traversal_edge():
    assert in_order_traversal(None) == []

def test_pre_order_traversal(root):
    assert pre_order_traversal(root) == [8, 1, 3, 4, 6, 7, 10, 13, 14]
def test_pre_order_traversal_edge():
    assert pre_order_traversal(None) == []
    
def test_post_order_traversal(root):
    assert post_order_traversal(root) == [1, 3, 4, 6, 7, 10, 13, 14, 8]
def test_post_order_traversal_edge():
    assert post_order_traversal(None) == []
    
def test_level_order_traversal(root):
    assert level_order_traversal(root) == [[8], [3, 10], [1, 6, 14], [4, 7, 13]]
def test_level_order_traversal_edge():
    assert level_order_traversal(None) == []


