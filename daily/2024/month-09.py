from itertools import pairwise
import math
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TrieNode:
    def __init__(self):
        self.children = {}
        self.counts = 0

    def insert(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            curr.counts += 1

    def search(self, word):
        res = 0
        curr = self
        for c in word:
            curr = curr.children[c]
            res += curr.counts
        return res


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        """
        09.01
        2022. Convert 1D Array Into 2D Array
        https://leetcode.com/problems/convert-1d-array-into-2d-array/description/?envType=daily-question&envId=2024-09-01
        """
        res = []
        # validity check
        if len(original) == m * n:
            for i in range(0, len(original), n):
                res.append(original[i : i + n])
        return res

    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        """
        09.02
        1894. Find the Student that Will Replace the Chalk
        https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/description/?envType=daily-question&envId=2024-09-02
        """
        s = sum(chalk)
        k %= s
        for i, n in enumerate(chalk):
            if k < n:
                return i
            k -= n
        return -1

    def getLucky(self, s: str, k: int) -> int:
        """
        09.03
        1945. Sum of Digits of String After Convert
        https://leetcode.com/problems/sum-of-digits-of-string-after-convert/description/?envType=daily-question&envId=2024-09-03
        def getLucky(self, s: str, k: int) -> int:
            s = "".join(str(ord(x) - ord("a") + 1) for x in s)
            for _ in range(k):
                s = str(sum(int(x) for x in s))
            return int(s)
        """
        # convert from alphabet to number
        base = ord("a") - 1
        k -= 1
        tmp = ""
        for c in s:
            tmp += str(ord(c) - base)
        while k:
            tmp_ = 0
            for c in tmp:
                tmp_ += int(c)
            tmp = str(tmp_)
            k -= 1

        res = 0
        for c in tmp:
            res += int(c)
        return res

    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        """
        09.04
        874. Walking Robot Simulation
        https://leetcode.com/problems/walking-robot-simulation/description/?envType=daily-question&envId=2024-09-04
        """
        x = y = cur_d_index = mx = 0
        st = set(map(tuple, obstacles))
        # URDL
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for c in commands:
            if c == -2:
                cur_d_index = (cur_d_index - 1) % 4
            elif c == -1:
                cur_d_index = (cur_d_index + 1) % 4
            else:
                di, dj = dirs[cur_d_index]
                while c and (x + di, y + dj) not in st:
                    x += di
                    y += dj
                    c -= 1
            mx = max(mx, x**2 + y**2)
        return mx

    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        """
        09.05
        2028. Find Missing Observations
        https://leetcode.com/problems/find-missing-observations/description/?envType=daily-question&envId=2024-09-05
        """
        total = mean * (len(rolls) + n)
        had = sum(rolls)
        need = total - had
        if need > 6 * n or need < n:
            return []
        res = [0 for _ in range(n)]
        i = 0
        while need:
            res[i] += 1
            i = (i + 1) % n
            need -= 1
        return res

    def modifiedList(
        self, nums: List[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        09.06
        3217. Delete Nodes From Linked List Present in Array
        https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/description/?envType=daily-question&envId=2024-09-06
        """
        dummy = ListNode()
        nums = set(nums)
        prev = dummy
        while head:
            if head.val not in nums:
                prev.next = head
                prev = prev.next
            head = head.next
            # cut possible link to next nodes
            prev.next = head
        return dummy.next

    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        """
        09.07
        1367. Linked List in Binary Tree
        https://leetcode.com/problems/linked-list-in-binary-tree/description/?envType=daily-question&envId=2024-09-07
        """

        def dfs(node: Optional[TreeNode], cur: Optional[ListNode]):
            if not cur:
                return True
            if not node:
                return False
            return node.val == cur.val and (
                dfs(node.left, cur.next) or dfs(node.right, cur.next)
            )

        if not head:
            return True
        if not root:
            return False

        return (
            dfs(root, head)
            # call self to deal the case, the head might start at anywhere
            or self.isSubPath(root.left, head)
            or self.isSubPath(root.right, head)
        )

    def splitListToParts(
        self, head: Optional[ListNode], k: int
    ) -> List[Optional[ListNode]]:
        """
        09.08
        725. Split Linked List in Parts
        https://leetcode.com/problems/split-linked-list-in-parts/description/?envType=daily-question&envId=2024-09-08
        """
        # get len
        n = 0
        cur = head
        while cur:
            cur = cur.next
            n += 1
        n, x = divmod(n, k)
        arr = [n for _ in range(k)]
        # how many for each slot
        for i in range(x):
            arr[i] += 1
        res = []
        prev = None
        for x in arr:
            res.append(head)
            while x:
                prev = head
                head = head.next
                x -= 1
            if prev:
                prev.next = None
        return res

    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        """
        09.09
        2326. Spiral Matrix IV
        https://leetcode.com/problems/spiral-matrix-iv/description/?envType=daily-question&envId=2024-09-09
        dx, dy = 1,0
        dx, dy = -dy, dx
        """
        res = [[-1 for _ in range(n)] for _ in range(m)]

        x = y = 0
        dx, dy = 1, 0
        while head:
            res[y][x] = head.val
            # out of boundary or already visited, next direction
            if (
                x + dx < 0
                or x + dx >= n
                or y + dy < 0
                or y + dy >= m
                or res[y + dy][x + dx] != -1
            ):
                dx, dy = -dy, dx
            x = x + dx
            y = y + dy
            head = head.next
        return res

    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        09.10
        2807. Insert Greatest Common Divisors in Linked List
        https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/description/?envType=daily-question&envId=2024-09-10
        """
        if not head:
            return head
        slow = head
        fast = head.next
        while fast:
            x = math.gcd(slow.val, fast.val)
            slow.next = ListNode(x)
            slow.next.next = fast
            slow = fast
            fast = fast.next
        return head

    def minBitFlips(self, start: int, goal: int) -> int:
        """
        09.11
        2220. Minimum Bit Flips to Convert Number
        https://leetcode.com/problems/minimum-bit-flips-to-convert-number/description/?envType=daily-question&envId=2024-09-11
        """
        return (start ^ goal).bit_count()

    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        """
        09.12
        1684. Count the Number of Consistent Strings
        https://leetcode.com/problems/count-the-number-of-consistent-strings/description/?envType=daily-question&envId=2024-09-12
        """
        allowed = set(allowed)
        count = 0

        for word in words:
            for letter in word:
                if letter not in allowed:
                    count += 1
                    break

        return len(words) - count

    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        """
        09.13
        1310. XOR Queries of Subarray
        https://leetcode.com/problems/xor-queries-of-a-subarray/description/?envType=daily-question&envId=2024-09-13
        """
        prefix = [0]
        for a in arr:
            prefix.append(prefix[-1] ^ a)
        return [prefix[i] ^ prefix[j + 1] for i, j in queries]

    def longestSubarray(self, nums: List[int]) -> int:
        """
        09.14
        2419. Longest Subarray With Maximum Bitwise AND
        https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/description/?envType=daily-question&envId=2024-09-14
        """
        x = max(nums)
        n = len(nums)
        res = 0
        cnt = 0
        for i in range(n):
            if nums[i] == x:
                cnt += 1
            else:
                cnt = 0
            res = max(res, cnt)
        return res

    def findTheLongestSubstring(self, s: str) -> int:
        """
        09.15
        1371. Find the Longest Substring Containing Vowels in Even Counts
        https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/description/?envType=daily-question&envId=2024-09-15
        """
        vowels = "aeiou"
        n = len(s)
        # store the state of vowels
        state = {0: -1}
        res = 0
        mask = 0
        for i in range(n):
            if s[i] in vowels:
                mask ^= 1 << vowels.index(s[i])
            if mask not in state:
                state[mask] = i
            res = max(res, i - state[mask])
        return res

    def findMinDifference(self, timePoints: List[str]) -> int:
        """
        09.16
        539. Minimum Time Difference
        https://leetcode.com/problems/minimum-time-difference/description/?envType=daily-question&envId=2024-09-16
        """
        if len(timePoints) > 24 * 60:
            return 0
        mins = sorted(int(t[:2]) * 60 + int(t[3:]) for t in timePoints)
        mins.append(mins[0] + 24 * 60)  # make it a circle, linking 1st and last slot

        return min(abs(a - b) for a, b in pairwise(mins))

    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        """
        09.17
        884. Uncommon Words from Two Sentences
        https://leetcode.com/problems/uncommon-words-from-two-sentences/description/?envType=daily-question&envId=2024-09-17
        """
        from collections import Counter

        c = Counter(s1.split() + s2.split())
        return [k for k, v in c.items() if v == 1]

    def largestNumber(self, nums: List[int]) -> str:
        """
        09.18
        179. Largest Number
        https://leetcode.com/problems/largest-number/description/?envType=daily-question&envId=2024-09-18
        """
        from functools import cmp_to_key

        def compare(x, y):
            # 30, 3 -> 303, 330
            return int(x + y) - int(y + x)

        nums = sorted(map(str, nums), key=cmp_to_key(compare), reverse=True)
        return str(int("".join(nums)))

    def diffWaysToCompute(self, expression: str) -> List[int]:
        """
        09.19
        241. Different Ways to Add Parentheses
        https://leetcode.com/problems/different-ways-to-add-parentheses/description/?envType=daily-question&envId=2024-09-19
        """
        ops = set(list("+-*"))

        def helper(s):
            if s.isdigit():
                return [int(s)]
            res = []
            for i, c in enumerate(s):
                if c in ops:
                    left = helper(s[:i])
                    right = helper(s[i + 1 :])
                    for l in left:
                        for r in right:
                            res.append(
                                l + r if c == "+" else l - r if c == "-" else l * r
                            )
            return res

        return helper(expression)

    def shortestPalindrome(self, s: str) -> str:
        """
        09.20
        214. Shortest Palindrome
        https://leetcode.com/problems/shortest-palindrome/description/?envType=daily-question&envId=2024-09-20
        """
        n = len(s)
        rev = s[::-1]
        for i in range(n):
            if s[: n - i] == rev[i:]:
                return rev[:i] + s
        return ""

    def lexicalOrder(self, n: int) -> List[int]:
        """
        09.21
        386. Lexicographical Numbers
        https://leetcode.com/problems/lexicographical-numbers/description/?envType=daily-question&envId=2024-09-21
        """
        res = []

        def dfs(x):
            if x > n:
                return
            res.append(x)
            for i in range(10):
                dfs(10 * x + i)

        for i in range(1, 10):
            dfs(i)
        return res

    def findKthNumber(self, n: int, k: int) -> int:
        """
        09.22
        440. K-th Smallest in Lexicographical Order
        https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/description/?envType=daily-question&envId=2024-09-22
        """
        result = 1
        k -= 1
        while k > 0:
            count = 0
            interval = [result, result + 1]
            while interval[0] <= n:
                count += min(n + 1, interval[1]) - interval[0]
                interval = [10 * interval[0], 10 * interval[1]]

            if k >= count:
                result += 1
                k -= count
            else:
                result *= 10
                k -= 1
        return result

    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        """
        09.23
        2707. Extra Character in a String
        https://leetcode.com/problems/extra-character-in-a-string/description/?envType=daily-question&envId=2024-09-23
        """
        dp = [0] * 51  # Initialize an array to store the minimum extra characters.
        n = len(s)

        for i in range(n - 1, -1, -1):
            dp[i] = 1 + dp[i + 1]  # Initialize with one extra character.

            for w in dictionary:
                if i + len(w) <= n and s[i : i + len(w)] == w:
                    dp[i] = min(
                        dp[i], dp[i + len(w)]
                    )  # Update if a word in the dictionary is found.

        return dp[0]  # Return the minimum extra characters for the entire string.

    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        """
        09.24
        3043. Find the length of the longest common prefix
        https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/description/?envType=daily-question&envId=2024-09-24
        """
        ret = 0
        st = set()
        for x in arr1:
            sx = str(x)
            for i in range(len(sx)):
                st.add(sx[: i + 1])

        for x in arr2:
            sx = str(x)
            for i in range(len(sx)):
                if sx[: i + 1] in st:
                    ret = max(ret, i + 1)
        return ret

    def sumPrefixScores(self, words: List[str]) -> List[int]:
        """
        09.25
        2416. Sum of Prefix Scores of Strings
        https://leetcode.com/problems/sum-of-prefix-scores-of-strings/description/?envType=daily-question&envId=2024-09-25
        """
        root = TrieNode()
        for word in words:
            root.insert(word)

        res = []
        for word in words:
            res.append(root.search(word))

        return res


class MyCalendar:
    """
    09.26
    729. My Calendar I
    https://leetcode.com/problems/my-calendar-i/description/?envType=daily-question&envId=2024-09-26
        public boolean book(int start, int end) {
            Integer low = map.lowerKey(end);

            if(low == null || map.get(low) <= start) {
                map.put(start, end);
                return true;
            }
            return false;
        }
    """

    def __init__(self):
        pass


class MyCalendarII:
    """
    09.27
    731. My Calendar II
    https://leetcode.com/problems/my-calendar-ii/description/?envType=daily-question&envId=2024-09-27
        public boolean book(int start, int end) {
            map.put(start, map.getOrDefault(start, 0) + 1);
            map.put(end, map.getOrDefault(end, 0) - 1);
            int count = 0;
            for(Map.Entry<Integer, Integer> entry : map.entrySet()) {
                count += entry.getValue();
                if(count > 2) {
                    map.put(start, map.get(start) - 1);
                    map.remove(start, 0);

                    map.put(end, map.get(end) + 1);
                    map.remove(end, 0);
                    return false;
                }
            }
            return true;
        }
    """

    def __init__(self):
        pass


class MyCircularDeque:
    """
    09.28
    641. Design Circular Deque
    https://leetcode.com/problems/design-circular-deque/description/?envType=daily-question&envId=2024-09-28
    """

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self._size = 0
        self._front, self._rear = 0, 0
        self._capacity = k
        self._data = [-1] * k

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        if self.isEmpty():
            self._data[self._front] = value
        else:
            self._front = (self._front - 1) % self._capacity
            self._data[self._front] = value
        self._size += 1
        return True

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        if self.isEmpty():
            self._data[self._rear] = value
        else:
            self._rear = (self._rear + 1) % self._capacity
            self._data[self._rear] = value
        self._size += 1
        return True

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self._data[self._front] = -1
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        if self.isEmpty():
            self._rear = self._front
        return True

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self._data[self._rear] = -1
        self._rear = (self._rear - 1) % self._capacity
        self._size -= 1
        if self.isEmpty():
            self._front = self._rear
        return True

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        return self._data[self._front]

    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        return self._data[self._rear]

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        return self._size == 0

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        return self._size == self._capacity


class Block(object):
    def __init__(self, val=0):
        self.val = val
        self.keys = set()
        self.before = None
        self.after = None

    def remove(self):
        self.before.after = self.after
        self.after.before = self.before
        self.before, self.after = None, None

    def insert_after(self, new_block):
        old_after = self.after
        self.after = new_block
        new_block.before = self
        new_block.after = old_after
        old_after.before = new_block


class AllOne(object):
    """
    09.29
    432. All O`one Data Structure
    https://leetcode.com/problems/all-oone-data-structure/description/?envType=daily-question&envId=2024-09-29
    """

    def __init__(self):
        self.begin = Block()  # sentinel
        self.end = Block()  # sentinel
        self.begin.after = self.end
        self.end.before = self.begin
        self.mapping = {}  # key to block

    def inc(self, key):
        if not key in self.mapping:  # find current block and remove key
            current_block = self.begin
        else:
            current_block = self.mapping[key]
            current_block.keys.remove(key)

        if current_block.val + 1 != current_block.after.val:  # insert new block
            new_block = Block(current_block.val + 1)
            current_block.insert_after(new_block)
        else:
            new_block = current_block.after

        new_block.keys.add(key)  # update new_block
        self.mapping[key] = new_block  # ... and mapping of key to new_block

        if (
            not current_block.keys and current_block.val != 0
        ):  # delete current block if not seninel
            current_block.remove()

    def dec(self, key):
        if not key in self.mapping:
            return

        current_block = self.mapping[key]
        del self.mapping[key]  # could use self.mapping.pop(key)
        current_block.keys.remove(key)

        if current_block.val != 1:
            if current_block.val - 1 != current_block.before.val:  # insert new block
                new_block = Block(current_block.val - 1)
                current_block.before.insert_after(new_block)
            else:
                new_block = current_block.before
            new_block.keys.add(key)
            self.mapping[key] = new_block

        if not current_block.keys:  # delete current block
            current_block.remove()

    def getMaxKey(self):
        if self.end.before.val == 0:
            return ""
        key = (
            self.end.before.keys.pop()
        )  # pop and add back to get arbitrary (but not random) element
        self.end.before.keys.add(key)
        return key

    def getMinKey(self):
        if self.begin.after.val == 0:
            return ""
        key = self.begin.after.keys.pop()
        self.begin.after.keys.add(key)
        return key


class CustomStack:
    """
    09.30
    1381. Design a Stack With Increment Operation
    https://leetcode.com/problems/design-a-stack-with-increment-operation/description/?envType=daily-question&envId=2024-09-30
    """

    def __init__(self, maxSize):
        self.n = maxSize
        self.stack = []
        self.inc = []

    def push(self, x):
        if len(self.inc) < self.n:
            self.stack.append(x)
            self.inc.append(0)

    def pop(self):
        if not self.inc:
            return -1
        if len(self.inc) > 1:
            self.inc[-2] += self.inc[-1]
        return self.stack.pop() + self.inc.pop()

    def increment(self, k, val):
        if self.inc:
            self.inc[min(k, len(self.inc)) - 1] += val
