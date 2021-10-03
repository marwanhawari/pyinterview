from pyinterview.linked_lists import ListNode, reverse_LL, LL_to_array, pop_LL

head = ListNode(0)
second = head.next = ListNode(1)
third = head.next.next = ListNode(2)
fourth = head.next.next.next = ListNode(3)
fifth = head.next.next.next.next = ListNode(4)


def test_LL_to_array():
    assert LL_to_array(head) == [0, 1, 2, 3, 4]


def test_array_to_LL():
    return


def test_pop_LL():
    head_node = ListNode(0)
    head_node.next = ListNode(1)
    head_node.next.next = ListNode(2)

    first_pop = pop_LL(head_node)
    second_pop = pop_LL(head_node)
    third_pop = pop_LL(head_node)

    assert first_pop.val == 2
    assert second_pop.val == 1
    assert third_pop is None


def test_reverse_LL():
    reversed_LL = reverse_LL(head)
    assert reversed_LL == fifth
    assert reversed_LL.next == fourth
    assert reversed_LL.next.next == third
    assert reversed_LL.next.next.next == second
    assert reversed_LL.next.next.next.next == head
