import pytest
from pyinterview.graphs import undirected_adj_list


@pytest.mark.parametrize(
    ("edges", "expected"),
    [
        ([("A", "B"), ("A", "C")], {"A": ["B", "C"], "B": ["A"], "C": ["A"]}),
        ([("A", "B"), ("B", "C")], {"A": ["B"], "B": ["A", "C"], "C": ["B"]}),
    ],
)
def test_undirected_adj_list(edges, expected):
    assert undirected_adj_list(edges) == expected
