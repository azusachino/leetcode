from bisect import bisect_right
from collections import defaultdict
import heapq
from string import ascii_lowercase
from typing import Counter, List

from linklist.list import ListNode


class Solution:
    """
    1169. Invalid Transactions
        https://leetcode.com/problems/invalid-transactions/description/
        https://leetcode.ca/2019-02-11-1169-Invalid-Transactions/
        String
    1170. Compare Strings by Frequency of the Smallest Character
        https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/description/
        https://leetcode.ca/2019-02-12-1170-Compare-Strings-by-Frequency-of-the-Smallest-Character/
        String
    1171. Remove Zero Sum Consecutive Nodes from Linked List
        https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/
        https://leetcode.ca/2019-02-13-1171-Remove-Zero-Sum-Consecutive-Nodes-from-Linked-List/
        LinkedList
    1172. Dinner Plate Stacks
        https://leetcode.com/problems/dinner-plate-stacks/
        https://leetcode.ca/2019-02-14-1172-Dinner-Plate-Stacks/
        system design, stack
    """

    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        """
        simulation
        """
        d = defaultdict(list)
        idx = set()
        for i, x in enumerate(transactions):
            name, time, amount, city = x.split(",")
            time, amount = int(time), int(amount)
            d[name].append((time, city, i))
            if amount > 1000:
                idx.add(i)
            for t, c, j in d[name]:
                if c != city and abs(time - t) <= 60:
                    idx.add(i)
                    idx.add(j)
        return [transactions[i] for i in idx]

    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s: str) -> int:
            cnt = Counter(s)
            return next(cnt[c] for c in ascii_lowercase if cnt[c])

        n = len(words)
        nums = sorted(f(w) for w in words)
        return [n - bisect_right(nums, f(q)) for q in queries]

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


class DinnerPlates:
    def __init__(self, capacity):
        self.c = capacity
        self.q = (
            []
        )  # record the available stack, will use heap to quickly find the smallest available stack
        # if you are Java or C++ users, tree map is another good option.
        self.stacks = (
            []
        )  # record values of all stack of plates, its last nonempty stack are the rightmost position

    def push(self, val):
        # To push, we need to find the leftmost available position
        # first, let's remove any stacks on the left that are full
        # 1) self.q: if there is still available stack to insert plate
        # 2) self.q[0] < len(self.stacks): the leftmost available index self.q[0] is smaller than the current size of the stacks
        # 3) len(self.stacks[self.q[0]]) == self.c: the stack has reached full capacity
        while (
            self.q
            and self.q[0] < len(self.stacks)
            and len(self.stacks[self.q[0]]) == self.c
        ):
            # we remove the filled stack from the queue of available stacks
            heapq.heappop(self.q)

        # now we reach the leftmost available stack to insert

        # if the q is empty, meaning there are no more available stacks
        if not self.q:
            # open up a new stack to insert
            heapq.heappush(self.q, len(self.stacks))

        # for the newly added stack, add a new stack to self.stacks accordingly
        if self.q[0] == len(self.stacks):
            self.stacks.append([])

        # append the value to the leftmost available stack
        self.stacks[self.q[0]].append(val)

    def pop(self):
        # To pop, we need to find the rightmost nonempty stack
        # 1) stacks is not empty (self.stacks) and
        # 2) the last stack is empty
        while self.stacks and not self.stacks[-1]:
            # we throw away the last empty stack, because we can't pop from it
            self.stacks.pop()

        # now we reach the rightmost nonempty stack

        # we pop the plate from the last nonempty stack of self.stacks by using popAtStack function
        return self.popAtStack(len(self.stacks) - 1)

    def popAtStack(self, index):
        # To pop from an stack of given index, we need to make sure that it is not empty
        # 1) the index for inserting is valid and，
        # 2) the stack of interest is not empty
        if 0 <= index < len(self.stacks) and self.stacks[index]:
            # we add the index into the available stack
            heapq.heappush(self.q, index)
            # take the top plate, pop it and return its value
            return self.stacks[index].pop()

        # otherwise, return -1 because we can't pop any plate
        return -1
