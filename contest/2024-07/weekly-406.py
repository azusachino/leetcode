from itertools import product
from typing import List, Optional

from linklist.list import ListNode


class Solution:
    """
    3216. Lexicographically Smallest String After a Swap
        https://leetcode.com/problems/lexicographically-smallest-string-after-a-swap/description/
    3217. Delete Nodes From Linked List Present in Array
        https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/description/
    3218. Minimum Cost for Cutting Cake I
        https://leetcode.com/problems/minimum-cost-for-cutting-cake-i/
    3219. Minimum Cost for Cutting Cake II
        https://leetcode.com/problems/minimum-cost-for-cutting-cake-ii/
    """

    def getSmallestString(self, s: str) -> str:
        n = len(s)
        l = list(s)
        for i in range(n - 1):
            a = int(l[i])
            b = int(l[i + 1])
            if a % 2 == b % 2 and a > b:
                l[i], l[i + 1] = l[i + 1], l[i]
                break
        return "".join(l)

    def modifiedList(
        self, nums: List[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        st = set(nums)
        prev = dummy
        while head:
            if head.val not in st:
                prev.next = head
                prev = prev.next
            head = head.next
            prev.next = head
        return dummy.next

    def minimumCost(self, m: int, n: int, h: List[int], v: List[int]) -> int:
        h.sort()
        v.sort()
        sumh = sum(h)
        sumv = sum(v)
        res = 0
        while h and v:
            if h[-1] > v[-1]:
                res += h[-1] + sumv
                sumh -= h.pop()
            else:
                res += v[-1] + sumh
                sumv -= v.pop()
        return res + sumh + sumv

    def minimumCost(self, m, n, h, v):
        # @credit https://leetcode.com/problems/minimum-cost-for-cutting-cake-i/solutions/5473151/java-c-python-greedy/
        return sum(h) + sum(v) + sum(map(min, product(h, v)))
