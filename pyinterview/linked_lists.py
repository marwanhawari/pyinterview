from typing import Union


class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def LL_to_array(head: ListNode) -> list:
    """Convert a linked list into an array.

    Args:
        head (ListNode): The head node of the linked list.

    Returns:
        list: A new array containing the values from the linked list in order.
    """
    return []


def array_to_LL(array: list) -> ListNode:
    """Convert an array into a linked list.

    Args:
        array (list): The array which will be converted.

    Returns:
        ListNode: The head node of the new linked list.
    """
    return ListNode(0)


def reverse_LL(head: ListNode) -> ListNode:
    """Reverse a linked list in place.

    Args:
        head (ListNode): The head node of the linked list.

    Returns:
        ListNode: The head node of the reversed linked list.
    """
    itr = head
    prev = None

    while itr:
        next = itr.next
        itr.next = prev
        prev = itr
        itr = next

    return prev


def pop_LL(head: ListNode) -> ListNode:
    """Pop the last element from a linked list.

    Args:
        head (ListNode): The head node of the linked list.

    Returns:
        ListNode: The element that used to be the last element of the linked list.
    """
    return ListNode(0)


def append_LL(head: ListNode, element: Union[int, float, str]) -> ListNode:
    """Append an element to the end of a linked list.

    Args:
        head (ListNode): The head node of the linked list.
        element (Union[int, float, str]): The value of the ListNode element
        to be appended.

    Returns:
        ListNode: The head node of the linked list.
    """
    return ListNode(0)


def remove_LL(head: ListNode, element: Union[int, float, str]) -> ListNode:
    """Removes the first node in the linked list that has a given value.

    Args:
        head (ListNode): The head node of the linked list.
        element (Union[int, float, str]): The value of the ListNode element
        to be removed.

    Returns:
        ListNode: The head node of the linked list.
    """
    return ListNode(0)
