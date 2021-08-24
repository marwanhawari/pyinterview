from typing import Sequence
from collections import deque


def undirected_adj_list(edges: Sequence[Sequence]) -> dict:
    d = {}
    for start, end in edges:
        if start not in d:
            d[start] = []
        d[start].append(end)

        if end not in d:
            d[end] = []
        d[end].append(start)

    return d


def directed_adj_list(edges: Sequence[Sequence]) -> dict:
    d = {}
    for start, end in edges:
        if start not in d:
            d[start] = []
        d[start].append(end)

        if end not in d:
            d[end] = []

    return d


def inbound_degrees(adj_list: dict) -> dict:
    indegrees = {node: 0 for node in adj_list}
    for node in adj_list:
        for neighbor in adj_list[node]:
            indegrees[neighbor] += 1
    return indegrees


def find_sources(inbounnd_degrees: dict) -> deque:
    sources = deque()
    for node in inbounnd_degrees:
        if inbounnd_degrees[node] == 0:
            sources.append(node)
    return sources
