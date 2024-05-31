from collections import deque
import heapq
import sys
from typing import Counter, List, Optional

from tree.local_tree import TreeNode


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    2024-05
    """

    def reversePrefix(self, word: str, ch: str) -> str:
        """
        05.01
        2000. Reverse Prefix of Word
        https://leetcode.com/problems/reverse-prefix-of-word/description/
        string, array
        """
        i = word.find(ch)
        return word[: i + 1][::-1] + word[i + 1 :]

    def findMaxK(self, nums: List[int]) -> int:
        """
        05.02
        2441. Largest Positive Integer That Exists With Its Negative
        https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/description
        array, frequency
        """
        cnt = Counter(nums)
        arr = [k for k in cnt.keys() if -k in cnt]
        if arr:
            return max(arr)
        return -1

    def compareVersion(self, version1: str, version2: str) -> int:
        """
        05.03
        165. Compare Version Numbers
        https://leetcode.com/problems/compare-version-numbers/description/?envType=daily-question&envId=2024-05-03
        string, array
        """
        arr1, arr2 = version1.split("."), version2.split(".")
        m, n = len(arr1), len(arr2)
        i = j = 0
        while i < m and j < n:
            x, y = int(arr1[i]), int(arr2[j])
            if x > y:
                return 1
            elif x < y:
                return -1
            i += 1
            j += 1
        while i < m:
            if int(arr1[i]) > 0:
                return 1
            i += 1
        while j < n:
            if int(arr2[j]) > 0:
                return -1
            j += 1
        return 0

    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
        05.04
        881. Boats to Save People
        https://leetcode.com/problems/boats-to-save-people/
        array, two-pointer
        """
        n = len(people)
        people.sort(reverse=True)
        i, j = 0, n - 1
        while i <= j:
            if people[i] + people[j] <= limit:
                j -= 1
            i += 1
        return i

    def deleteNode(self, node):
        """
        05.05
        237. Delete Node in a Linked List
        https://leetcode.com/problems/delete-node-in-a-linked-list/description/?envType=daily-question&envId=2024-05-05
        linkedlist
        """
        if node.next:
            node.val = node.next.val
            node.next = node.next.next
        else:
            node.next = None

    def removeNodes(self, head):
        """
        05.06
        2487. Remove Nodes From Linked List
        https://leetcode.com/problems/remove-nodes-from-linked-list/?envType=daily-question&envId=2024-05-06
        linkedlist
        """
        if not head:
            return None
        head.next = self.removeNodes(head.next)
        if head.next and head.val < head.next.val:
            return head.next
        return head

    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        05.07
        2816. Double a Number Represented as a Linked List
        https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/description/?envType=daily-question&envId=2024-05-07
        linkedlist
        ```python
        def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
            def reverseList(head):
                prev = None
                while head:
                    nxt = head.next
                    head.next = prev
                    prev = head
                    head = nxt
                return prev
            head = reverseList(head)
            carry = 0
            cur = head
            while cur:
                v = cur.val * 2 + carry
                cur.val = v % 10
                carry = v // 10
                cur = cur.next
            if carry:
                return ListNode(carry, reverseList(head))
            return reverseList(head)
        ```
        """
        if head.val > 4:
            head = ListNode(0, head)
        node = head
        while node:
            node.val = (node.val * 2) % 10
            if node.next and node.next.val > 4:
                node.val += 1
            node = node.next
        return head

    def findRelativeRanks(self, nums):
        """
        05.08
        506. Relative Ranks
        https://leetcode.com/problems/relative-ranks/description/?envType=daily-question&envId=2024-05-08
        array
        """
        sort = sorted(nums)[::-1]
        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"] + list(
            map(str, range(4, len(nums) + 1))
        )
        return map(dict(zip(sort, rank)).get, nums)

    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        """
        05.09
        3075. Maximize Happiness of Selected Children
        https://leetcode.com/problems/maximize-happiness-of-selected-children/description/?envType=daily-question&envId=2024-05-09
        array, sort, pq
        """
        happiness.sort(reverse=True)
        # [(0, 3), (1, 2)]
        arr = list(enumerate(happiness[:k]))
        return sum(map(lambda x: max(x[1] - x[0], 0), arr))

    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        """
        05.10
        786. K-th Smallest Prime Fraction
        https://leetcode.com/problems/k-th-smallest-prime-fraction/description/?envType=daily-question&envId=2024-05-10
        pq
        """
        h = [(1 / y, 0, j + 1) for j, y in enumerate(arr[1:])]
        heapq.heapify(h)
        for _ in range(k - 1):
            _, i, j = heapq.heappop(h)
            if i + 1 < j:
                heapq.heappush(h, (arr[i + 1] / arr[j], i + 1, j))
        return [arr[h[0][1]], arr[h[0][2]]]

    def mincostToHireWorkers(self, quality, wage, K):
        """
        05.11
        857. Minimum Cost to Hire K Workers
        https://leetcode.com/problems/minimum-cost-to-hire-k-workers/?envType=daily-question&envId=2024-05-11
        pq
        """
        workers = sorted([w / q, q] for w, q in zip(wage, quality))
        res = sys.maxsize
        qsum = 0
        heap = []
        for r, q in workers:
            heapq.heappush(heap, -q)
            qsum += q
            if len(heap) > K:
                qsum += heapq.heappop(heap)
            if len(heap) == K:
                res = min(res, qsum * r)
        return res

    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        """
        05.12
        2373. Largest Local Values in a Matrix
        https://leetcode.com/problems/largest-local-values-in-a-matrix
        array
        """
        n = len(grid)
        res = [[0] * (n - 2) for _ in range(n - 2)]

        for i in range(n - 2):
            for j in range(n - 2):
                res[i][j] = max(
                    grid[m][n] for m in range(i, i + 3) for n in range(j, j + 3)
                )

        return res

    def matrixScore(self, grid: List[List[int]]) -> int:
        """
        05.13
        861. Score After Flipping Matrix
        https://leetcode.com/problems/score-after-flipping-matrix/description/?envType=daily-question&envId=2024-05-13
        bitwise
        A[i][0] is worth 1 << (N - 1) points, more than the sum of (A[i][1] + .. + A[i][N-1]).
        We need to toggle all A[i][0] to 1, here I toggle all lines for A[i][0] = 0.

        A[i][j] is worth 1 << (N - 1 - j)
        For every col, I count the current number of 1s.
        After step 1, A[i][j] becomes 1 if A[i][j] == A[i][0].
        if M - cur > cur, we can toggle this column to get more 1s.
        max(cur, M - cur) will be the maximum number of 1s that we can get.
        """
        m, n = len(grid), len(grid[0])
        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] ^= 1
        ans = 0
        for j in range(n):
            cnt = sum(grid[i][j] for i in range(m))
            ans += max(cnt, m - cnt) * (1 << (n - j - 1))
        return ans

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        """
        05.14
        1219. Path with Maximum Gold
        https://leetcode.com/problems/path-with-maximum-gold/description/?envType=daily-question&envId=2024-05-14
        graph, dfs
        class Solution:
            def getMaximumGold(self, grid: List[List[int]]) -> int:
                def dfs(i: int, j: int) -> int:
                    if not (0 <= i < m and 0 <= j < n and grid[i][j]):
                        return 0
                    v = grid[i][j]
                    grid[i][j] = 0
                    ans = max(dfs(i + a, j + b) for a, b in pairwise(dirs)) + v
                    grid[i][j] = v
                    return ans

                m, n = len(grid), len(grid[0])
                dirs = (-1, 0, 1, 0, -1)
                return max(dfs(i, j) for i in range(m) for j in range(n))
        """
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        m, n = len(grid), len(grid[0])
        self.res = 0
        path = deque()
        seen = set()

        def dfs(grid, i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return
            path.append(grid[i][j])
            self.res = max(self.res, sum(path))
            seen.add((i, j))
            grid[i][j] = 0
            for di, dj in dirs:
                dfs(grid, i + di, j + dj)
            grid[i][j] = path.pop()
            seen.remove((i, j))

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    dfs(grid, i, j)

        return self.res

    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        """
        05.15
        2812. Find the Safest Path in a Grid
        https://leetcode.com/problems/find-the-safest-path-in-a-grid/description/?envType=daily-question&envId=2024-05-15
        graph, dfs, bfs
        """
        A = []  # thieves
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    A.append([i, j])

        visited = set()
        distance = [[0 for j in range(n)] for i in range(m)]

        # find the minimum manhattan distance of each cell to theives
        depth = 0
        while A:
            B = []
            for i, j in A:
                if (i, j) not in visited:
                    visited.add((i, j))
                    distance[i][j] = depth
                    for x, y in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
                        if 0 <= x < m and 0 <= y < n:
                            B.append([x, y])
            A = B
            depth += 1

        # start from 0,0 and use dijkstra
        visited = set()
        pq = [[-distance[0][0], 0, 0]]
        while pq:
            dis, i, j = heapq.heappop(pq)
            if (i, j) in visited:
                continue
            visited.add((i, j))
            if i == m - 1 and j == n - 1:
                return -dis

            for x, y in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
                if 0 <= x < m and 0 <= y < n:
                    heapq.heappush(pq, [-min(-dis, distance[x][y]), x, y])

        return -1

    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        """
        05.16
        2331. Evaluate Boolean Binary Tree
        https://leetcode.com/problems/evaluate-boolean-binary-tree/description/?envType=daily-question&envId=2024-05-16
        tree, dfs
        """

        def dfs(node, pv):
            if not node:
                return pv
            if node.val == 0:
                return False
            elif node.val == 1:
                return True
            elif node.val == 2:
                # preserve previous value
                return dfs(node.left, node.val) or dfs(node.right, node.val)
            elif node.val == 3:
                return dfs(node.left, node.val) and dfs(node.right, node.val)

        return dfs(root, None)

    def removeLeafNodes(
        self, root: Optional[TreeNode], target: int
    ) -> Optional[TreeNode]:
        """
        05.17
        1325. Delete Leaves With a Given Value
        https://leetcode.com/problems/delete-leaves-with-a-given-value/description/?envType=daily-question&envId=2024-05-17
        tree, dfs, post_order
        """
        if not root:
            return root
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        if root.val == target and not root.left and not root.right:
            return None
        return root

    def distributeCoins(self, root):
        self.res = 0
        """
        05.18
        979. Distribute Coins in Binary Tree
        https://leetcode.com/problems/distribute-coins-in-binary-tree/description/?envType=daily-question&envId=2024-05-18
        tree, dfs
        """

        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.res += abs(left) + abs(right)
            return root.val + left + right - 1

        dfs(root)
        return self.res

    def maximumValueSum(self, A: List[int], k: int, edges: List[List[int]]) -> int:
        """
        05.19
        3068. Find the Maximum Sum of Node Values
        https://leetcode.com/problems/find-the-maximum-sum-of-node-values/description/
        tree, dp
        """
        res = c = 0
        d = 1 << 30
        for a in A:
            res += max(a, b := a ^ k)
            c ^= a < b
            d = min(d, abs(a - b))
        return res - d * c

    def subsetXORSum(self, nums: List[int]) -> int:
        """
        05.20
        1863. Sum of All Subset XOR Totals
        https://leetcode.com/problems/sum-of-all-subset-xor-totals/description/?envType=daily-question&envId=2024-05-20
        dfs, bitmask
        """

        def dfs(nums, i, cur):
            if i == len(nums):
                return cur
            with_ele = dfs(nums, i + 1, cur ^ nums[i])
            without = dfs(nums, i + 1, cur)
            return with_ele + without

        return dfs(nums, 0, 0)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        05.21
        78. Subsets
        https://leetcode.com/problems/subsets/description/?envType=daily-question&envId=2024-05-21
        backtrack
        """
        res = []

        def helper(i, cur):
            res.append(cur[:])
            for j in range(i, len(nums)):
                cur.append(nums[j])
                helper(j + 1, cur)
                cur.pop()

        helper(0, [])
        return res

    def partition(self, s: str) -> List[List[str]]:
        """
        05.22
        131. Palindrome Partitioning
        https://leetcode.com/problems/palindrome-partitioning/description/?envType=daily-question&envId=2024-05-22
        backtrack
        """
        res = []

        def backtrack(s, step, cur):
            if step == len(s):
                res.append(cur[:])
            for i in range(step, len(s)):
                if not is_palidrome(s, step, i):
                    continue
                cur.append(s[step : i + 1])
                backtrack(s, i + 1, cur)
                cur.pop()

        def is_palidrome(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        backtrack(s, 0, [])
        return res

    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        """
        05.23
        2597. The Number of Beautiful Subsets
        https://leetcode.com/problems/the-number-of-beautiful-subsets/description/?envType=daily-question&envId=2024-05-23
        backtrack
        """
        self.res = 0
        cnt = Counter()

        def dfs(i: int) -> None:
            # reached the end of the list, count this unique subset
            if i >= len(nums):
                self.res += 1
                return
            # if possible, take this element
            if cnt[nums[i] + k] == 0 and cnt[nums[i] - k] == 0:
                cnt[nums[i]] += 1
                dfs(i + 1)
                cnt[nums[i]] -= 1
            # recurse without taking this element
            dfs(i + 1)

        dfs(0)
        # -1 for the empty set
        return self.res - 1

    def maxScoreWords(
        self, words: List[str], letters: List[str], score: List[int]
    ) -> int:
        """
        05.24
        1255. Maximum Score Words Formed by Letters
        https://leetcode.com/problems/maximum-score-words-formed-by-letters/description/?envType=daily-question&envId=2024-05-24
        """
        cnt = Counter(letters)
        n = len(words)
        ans = 0
        for i in range(1 << n):
            cur = Counter("".join([words[j] for j in range(n) if i >> j & 1]))
            if all(v <= cnt[c] for c, v in cur.items()):
                t = sum(v * score[ord(c) - ord("a")] for c, v in cur.items())
                ans = max(ans, t)
        return ans

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """
        05.25
        140. Word Break II
        https://leetcode.com/problems/word-break-ii/description/?envType=daily-question&envId=2024-05-25
        trie, backtrack
        """
        dic = dict(zip(wordDict, [True] * len(wordDict)))
        self.res = []

        def dfs(string, sentence):
            if not string:
                self.res.append(sentence.strip())
                return
            for i in range(1, len(string) + 1):
                if string[:i] in dic:
                    dfs(string[i:], sentence + " " + string[:i])

        dfs(s, "")
        return self.res

    def checkRecord(self, n: int) -> int:
        """
        05.26
        552. Student Attendance Record II
        https://leetcode.com/problems/student-attendance-record-ii/description/?envType=daily-question&envId=2024-05-26
        dp
        """
        mod = int(1e9 + 7)
        dp = [[[0, 0, 0], [0, 0, 0]] for _ in range(n)]

        # base case
        dp[0][0][0] = dp[0][0][1] = dp[0][1][0] = 1

        for i in range(1, n):
            # A
            dp[i][1][0] = (dp[i - 1][0][0] + dp[i - 1][0][1] + dp[i - 1][0][2]) % mod
            # L
            dp[i][0][1] = dp[i - 1][0][0]
            dp[i][0][2] = dp[i - 1][0][1]
            dp[i][1][1] = dp[i - 1][1][0]
            dp[i][1][2] = dp[i - 1][1][1]
            # P
            dp[i][0][0] = (dp[i - 1][0][0] + dp[i - 1][0][1] + dp[i - 1][0][2]) % mod
            dp[i][1][0] = (
                dp[i][1][0] + dp[i - 1][1][0] + dp[i - 1][1][1] + dp[i - 1][1][2]
            ) % mod

        ans = 0
        for j in range(2):
            for k in range(3):
                ans = (ans + dp[n - 1][j][k]) % mod
        return ans

    def specialArray(self, nums: List[int]) -> int:
        """
        5.27
        1608. Special Array With X Elements Greater Than or Equal X
        https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/?envType=daily-question&envId=2024-05-27
        array
        """
        for x in range(1, len(nums) + 1):
            cnt = sum(v >= x for v in nums)
            if cnt == x:
                return x
        return -1

    def equalSubstring(self, s: str, t: str, cost: int) -> int:
        """
        05.28
        1208. Get Equal Substrings Within Budget
        https://leetcode.com/problems/get-equal-substrings-within-budget/description/?envType=daily-question&envId=2024-05-28
        sliding window
        """
        i = 0
        n = len(s)
        for j in range(n):
            cost -= abs(ord(s[j]) - ord(t[j]))
            if cost < 0:
                cost += abs(ord(s[i]) - ord(t[i]))
                i += 1
        return j - i + 1

    def numSteps(self, s: str) -> int:
        """
        05.29
        1404. Number of Steps to Reduce a Number in Binary Representation to One
        https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/description/?envType=daily-question&envId=2024-05-29
        bitwise/array
        """
        n = int(s, 2)
        c = 0
        while n > 1:
            if n % 2:
                n += 1
            else:
                n //= 2
            c += 1
        return c

    def countTriplets(self, arr: List[int]) -> int:
        """
        05.30
        1442. Count Triplets That Can Form Two Arrays of Equal XOR
        https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/description/?envType=daily-question&envId=2024-05-30
        Assume a == b, thus
        a ^ a = b ^ a, thus
        0 = b ^ a, thus
        arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1] ^ arr[j] ^ arr[j + 1] ^ ... ^ arr[k] = 0 thus
        prefix[k+1] = prefix[i]
        """
        arr.insert(0, 0)
        n = len(arr)
        for i in range(n - 1):
            arr[i + 1] ^= arr[i]
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                if arr[i] == arr[j]:
                    res += j - i - 1
        return res

    def singleNumber(self, nums: List[int]) -> List[int]:
        """
        05.31
        260. Single Number III
        https://leetcode.com/problems/single-number-iii/description/?envType=daily-question&envId=2024-05-31
        bitwise
        """
        xor_all = 0
        for num in nums:
            xor_all ^= num

        rightmost_set_bit = xor_all & -xor_all

        num1, num2 = 0, 0
        for num in nums:
            if num & rightmost_set_bit:
                num1 ^= num
            else:
                num2 ^= num
        return [num1, num2]


if __name__ == "__main__":
    solution = Solution()
    grid = [[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]]
    print(solution.getMaximumGold(grid))
