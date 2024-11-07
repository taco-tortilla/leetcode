from solution import ListNode


def main():
    head = createListNode([1, 1, 1])
    current = head
    while current and current.next:
        while current.next and current.val == current.next.val:
            current.next = current.next.next
        current = current.next
    return head


def createListNode(value):
    head = ListNode(value[0])
    current = head

    for i in range(1, len(value)):
        current.next = ListNode(value[i])
        current = current.next

    return head


if __name__ == "__main__":
    main()
