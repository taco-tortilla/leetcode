import pytest
from solution import Solution, ListNode


@pytest.mark.parametrize(
    "value, pos, expected",
    [
        ([3, 2, 0, -4], 1, True),
        ([1, 2], 0, True),
        ([1], -1, False),
    ],
)
def test_hasCycle(value, pos, expected):
    head = makeLinkedList(value, pos)
    solution = Solution()
    result = solution.hasCycle(head)
    assert result == expected, f"Expected {expected}, got {result}"


def makeLinkedList(value, pos):
    head = ListNode(value[0])
    current = head
    cycle_node = None

    for i in range(len(value)):
        current.next = ListNode(value[i])
        current = current.next
        if i == pos:
            cycle_node = current

    if pos != -1:
        current.next = cycle_node

    return head
