from typing import Union


def binary_search(array: list[int], target: int) -> int:
    """Perform a binary search.

    Args:
        array (list[int]): The array in which to search.
        target (int): The number to search for.

    Returns:
        int: The index of the target in the array. If target not found, return -1.
    """
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2

        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        elif array[mid] > target:
            right = mid - 1

    return -1


def quick_select(nums: list[Union[int, float]], k: int) -> Union[int, float]:
    return 0


def dfs(adj_list: dict) -> list:
    return []


def bfs(adj_list: dict) -> list:
    return []
