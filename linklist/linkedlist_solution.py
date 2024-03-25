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

    def mergeInBetween(
        self, list1: ListNode, a: int, b: int, list2: ListNode
    ) -> ListNode:
        dummy = ListNode()
        dummy.next = list1
        prev = None
        cur = dummy
        for _ in range(a + 1):
            prev = cur
            cur = cur.next
        prev.next = list2
        for _ in range(a, b + 1):
            cur = cur.next
        while list2.next:
            list2 = list2.next
        list2.next = cur
        return dummy.next

    def checkPalindrome(self, head: ListNode) -> bool:
        slow = fast = head
        prev = None
        # find median, and reverse the first half
        while fast and fast.next:
            fast = fast.next.next
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        # deal with odd counts
        if fast:
            slow = slow.next

        # simply check equality
        while slow and prev:
            if slow.val != prev.val:
                return False
            slow = slow.next
            prev = prev.next
        return True

    def aaa(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev, cur = None, slow.next
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        slow.next = None
        h1, h2 = head, prev
        while h2:
            nxt = h1.nxt
            h1.next = h2
            h2 = h1
            h1 = nxt


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
