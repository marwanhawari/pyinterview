from typing import Sequence
from random import randint
from pyinterview.graphs import directed_adj_list, inbound_degrees, find_sources


def bubble_sort(nums: list) -> list:
    """Sort an array using the bubble sort algorithm.

    Args:
        nums (list): The unsorted input array.

    Returns:
        list: The sorted output array.
    """
    return []


def quick_sort(nums: list) -> list:
    """Sort an array using the quick sort algorithm.

    Args:
        nums (list): The unsorted input array.

    Returns:
        list: The sorted output array.
    """
    if len(nums) == 0:
        return []

    pivot = nums[randint(0, len(nums) - 1)]

    smaller = [x for x in nums if x < pivot]
    equal = [x for x in nums if x == pivot]
    greater = [x for x in nums if x > pivot]

    return quick_sort(smaller) + equal + quick_sort(greater)


def merge_sort(nums: list) -> list:
    """Sort an array using the merge sort algorithm.

    Args:
        nums (list): The unsorted input array.

    Returns:
        list: The sorted output array.
    """

    def split_array(nums: list) -> list:
        """Recursively split array in half.

        Args:
            nums (list): The unsorted input array.

        Returns:
            list: Returns a sorted array.
        """
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2

        left = split_array(nums[:mid])
        right = split_array(nums[mid:])

        return merge_two(left, right)

    def merge_two(a: list, b: list) -> list:
        """Merges two sorted arrays.

        Args:
            a (list): The first sorted array.
            b (list): The second sorted array.

        Returns:
            list: Returns sorted array containing all elements from a and b.
        """
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


def topological_sort(edges: Sequence[Sequence]) -> list:
    """Produce a topological sorting (if one exists) using a BFS approach.

    Args:
        edges (Sequence[Sequence]): A list of edges pairs, ex: [('A', 'B'), ('A', 'C')].

    Returns:
        list: An array with a non-unique topological order of nodes.
    """

    adj_list = directed_adj_list(edges)

    indegrees = inbound_degrees(adj_list)

    sources = find_sources(indegrees)

    result = []
    while len(sources) > 0:

        source = sources.popleft()
        result.append(source)

        for neighbor in adj_list[source]:
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
                sources.append(neighbor)

    return result[::-1] if len(result) == len(adj_list) else []
