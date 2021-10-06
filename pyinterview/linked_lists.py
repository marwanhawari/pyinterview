from typing import Union, Optional


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

    if head is None:
        return []

    itr = head
    result = []
    while itr:
        result.append(itr.val)
        itr = itr.next

    return result


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


def pop_LL(head: ListNode) -> Optional[ListNode]:
    """Pop the last element from a linked list.

    Args:
        head (Optional[ListNode]): The head node of the linked list.

    Returns:
        ListNode: The element that used to be the last element of the linked list.
    """
    if head is None:
        print("Linked List is empty!")
    elif head.next is None:
        print("Linked List only contains one node!")
    else:
        itr = head
        while itr.next.next:
            itr = itr.next
        popped = itr.next
        itr.next = None

        return popped


def append_LL(head: ListNode, element: Union[int, float, str]) -> ListNode:
    """Append an element to the end of a linked list.

    Args:
        head (ListNode): The head node of the linked list.
        element (Union[int, float, str]): The value of the ListNode element \
        to be appended.

    Returns:
        ListNode: The head node of the linked list.
    """
    if head is None:
        print("Linked List is empty!")
    else:
        itr = head
        while itr.next:
            itr = itr.next
        last = itr
        last.next = ListNode(element)

    return ListNode(0)


def remove_LL(head: ListNode, element: Union[int, float, str]) -> ListNode:
    """Removes the first node in the linked list that has a given value.

    Args:
        head (ListNode): The head node of the linked list.
        element (Union[int, float, str]): The value of the ListNode element \
        to be removed.

    Returns:
        ListNode: The head node of the linked list.
    """
    return ListNode(0)
