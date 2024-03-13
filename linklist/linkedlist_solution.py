import collections
from typing import Optional
from list import ListNode


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        start = pointer = dummy
        for _ in range(n + 1):
            pointer = pointer.next

        while pointer:
            start = start.next
            pointer = pointer.next

        start.next = start.next.next

        return dummy.next

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        s = f = head
        while f and f.next:
            s = s.next
            f = f.next.next
            # compare address
            if s is f:
                return True
        return False

    def middle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = f = head
        while f and f.next:
            s = s.next
            f = f.next.next
        return s

    def removeZeroSumSublists(self, head):
        prefix = 0
        seen = {}
        seen[0] = dummy = ListNode(0)
        dummy.next = head
        while head:
            prefix += head.val
            seen[prefix] = head
            head = head.next
        head = dummy
        prefix = 0
        while head:
            prefix += head.val
            head.next = seen[prefix].next
            head = head.next
        return dummy.next


if __name__ == "__main__":
    s = Solution()
    r = s.removeNthFromEnd(None, 0)
    print("removeNthFromEnd", r)


class AnotherSolution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow, fast = head, head
        for _ in range(n):
            fast = fast.next
        # [1], 1
        if not fast:
            return head.next
        # [1,2], 1
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head
