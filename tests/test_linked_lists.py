from pyinterview.linked_lists import ListNode, reverse_LL

head = ListNode(0)
second = head.next = ListNode(1)
third = head.next.next = ListNode(2)
fourth = head.next.next.next = ListNode(3)
fifth = head.next.next.next.next = ListNode(4)


def test_LL_to_list():
    return


def test_list_to_LL():
    return


def test_reverse_LL():
    reversed_LL = reverse_LL(head)
    assert reversed_LL == fifth
    assert reversed_LL.next == fourth
    assert reversed_LL.next.next == third
    assert reversed_LL.next.next.next == second
    assert reversed_LL.next.next.next.next == head
