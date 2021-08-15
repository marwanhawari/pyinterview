from collections import deque
from typing import Sequence

def topological_sort(edges: list[Sequence]) -> list:
    def create_adj_list(edges: list[Sequence]) -> dict:
        d = {}
        for start, end in edges:
            if start not in d:
                d[start] = []
            d[start].append(end)

            if end not in d:
                d[end] = []

        return d

    adj_list = create_adj_list(edges)
    
    def calculate_inbound_degrees(adj_list: dict) -> dict:
        inbound_degrees = {node: 0 for node in adj_list}
        for node in adj_list:
            for neighbor in adj_list[node]:
                inbound_degrees[neighbor] += 1
        return inbound_degrees
    
    inbound_degrees = calculate_inbound_degrees(adj_list)

    def find_sources(inbounnd_degrees: dict) -> deque:
        sources = deque()
        for node in inbounnd_degrees:
            if inbounnd_degrees[node] == 0:
                sources.append(node)
        return sources

    sources = find_sources(inbound_degrees)

    result = []
    while len(sources) > 0:

        source = sources.popleft()
        result.append(source)

        for neighbor in adj_list[source]:
            inbound_degrees[neighbor] -= 1
            if inbound_degrees[neighbor] == 0:
                sources.append(neighbor)

    return result[::-1] if len(result) == len(adj_list) else []
