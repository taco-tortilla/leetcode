from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    # def hasCycle(self, head: Optional[ListNode]) -> bool:
    #     visited = set()
    #     current = head
    #     while current:
    #         if current in visited:
    #             return True
    #         visited.add(current)
    #         current = current.next
    #     return False
