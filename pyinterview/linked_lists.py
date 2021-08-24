class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def LL_to_list(head: ListNode) -> list:
    return []


def list_to_LL(array: list) -> ListNode:
    return ListNode(0)


def reverse_LL(head: ListNode) -> ListNode:
    itr = head
    prev = None

    while itr:
        next = itr.next
        itr.next = prev
        prev = itr
        itr = next

    return prev


def pop_LL(head: ListNode) -> ListNode:
    return ListNode(0)


def append_LL(head: ListNode) -> ListNode:
    return ListNode(0)


def remove_LL(head: ListNode) -> ListNode:
    return ListNode(0)
