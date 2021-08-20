from collections import deque
from typing import Sequence
from random import randint


def quick_sort(nums: list) -> list:
    if len(nums) == 0:
        return []

    pivot = nums[randint(0, len(nums) - 1)]

    smaller = [x for x in nums if x < pivot]
    equal = [x for x in nums if x == pivot]
    greater = [x for x in nums if x > pivot]

    return quick_sort(smaller) + equal + quick_sort(greater)


def merge_sort(nums: list) -> list:
    def split_array(nums):
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2

        left = split_array(nums[:mid])
        right = split_array(nums[mid:])

        return merge_two(left, right)

    def merge_two(a, b):
        result = []
        i = j = 0
        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                result.append(a[i])
                i += 1
            else:
                result.append(b[j])
                j += 1
        while i < len(a):
            result.append(a[i])
            i += 1
        while j < len(b):
            result.append(b[j])
            j += 1
        return result

    return split_array(nums)


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
