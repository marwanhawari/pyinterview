import pytest
from collections import deque
from pyinterview.graphs import (
    undirected_adj_list,
    directed_adj_list,
    inbound_degrees,
    find_sources,
)


@pytest.mark.parametrize(
    ("edges", "expected"),
    [
        ([("A", "B"), ("A", "C")], {"A": ["B", "C"], "B": ["A"], "C": ["A"]}),
        ([("A", "B"), ("B", "C")], {"A": ["B"], "B": ["A", "C"], "C": ["B"]}),
    ],
)
def test_undirected_adj_list(edges, expected):
    assert undirected_adj_list(edges) == expected


@pytest.mark.parametrize(
    ("edges", "expected"),
    [
        ([("A", "B"), ("A", "C")], {"A": ["B", "C"], "B": [], "C": []}),
        ([("A", "B"), ("B", "C")], {"A": ["B"], "B": ["C"], "C": []}),
    ],
)
def test_directed_adj_list(edges, expected):
    assert directed_adj_list(edges) == expected


@pytest.mark.parametrize(
    ("adj_list", "expected"),
    [
        ({"A": ["B", "C"], "B": [], "C": []}, {"A": 0, "B": 1, "C": 1}),
        ({"A": ["B"], "B": ["C"], "C": []}, {"A": 0, "B": 1, "C": 1}),
        ({"A": ["B"], "B": ["A"]}, {"A": 1, "B": 1}),
    ],
)
def test_inbound_degrees(adj_list, expected):
    assert inbound_degrees(adj_list) == expected


@pytest.mark.parametrize(
    ("inbounnd_degrees", "expected"),
    [
        ({"A": 0, "B": 1, "C": 1}, deque(["A"])),
        ({"A": 0, "B": 1, "C": 1}, deque(["A"])),
        ({"A": 1, "B": 1}, deque([])),
    ],
)
def test_find_sources(inbounnd_degrees, expected):
    assert find_sources(inbounnd_degrees) == expected
