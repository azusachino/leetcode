import bisect
from collections import deque
from functools import cache
import heapq
import math
import sys
from typing import Counter, List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        """
        10.01
        1497. Check If Array Pairs Are Divisible by k
        https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/?envType=daily-question&envId=2024-10-01
        """
        if len(arr) % 2 != 0:
            return False

        arr = [i % k for i in arr]
        count = Counter(arr)

        for key in count:
            if key == 0:
                if count[key] % 2 != 0:
                    return False
            elif k - key in count:
                if count[key] != count[k - key]:
                    return False
            else:
                return False

        return True

    def arrayRankTransform(self, A):
        """
        10.02
        1331. Rank Transform of an Array
        https://leetcode.com/problems/rank-transform-of-an-array/?envType=daily-question&envId=2024-10-02
        """
        rank = {}
        for a in sorted(A):
            rank.setdefault(a, len(rank) + 1)
        return map(rank.get, A)

    def minSubarray(self, nums: List[int], p: int) -> int:
        """
        10.03
        1590. Make Sum Divisible by P
        https://leetcode.com/problems/make-sum-divisible-by-p/?envType=daily-question&envId=2024-10-03
        """
        need = sum(nums) % p
        if need == 0:
            return 0

        d = {0: -1}
        cur = 0
        res = n = len(nums)
        for i, a in enumerate(nums):
            cur = (cur + a) % p
            d[cur] = i
            if (cur - need) % p in d:
                res = min(res, i - d[(cur - need) % p])
        return res if res < n else -1

    def dividePlayers(self, ss: List[int]) -> int:
        """
        10.04
        2491. Divide Players into Teams of Equal Skill
        https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/?envType=daily-question&envId=2024-10-04
        """
        ss.sort()
        chemistry, s = 0, ss[0] + ss[-1]

        for i in range(len(ss) // 2):
            if ss[i] + ss[-i - 1] == s:
                chemistry += ss[i] * ss[-i - 1]
            else:
                return -1
        return chemistry

    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        10.05
        567. Permutation in String
        https://leetcode.com/problems/permutation-in-string/?envType=daily-question&envId=2024-10-05
        """
        cntr, w = Counter(s1), len(s1)

        for i in range(len(s2)):
            if s2[i] in cntr:
                cntr[s2[i]] -= 1
            # fixed size window
            if i >= w and s2[i - w] in cntr:
                cntr[s2[i - w]] += 1

            if all([cntr[i] == 0 for i in cntr]):  # see optimized code below
                return True

        return False

    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        """
        10.06
        1813. Sentence Similarity III
        https://leetcode.com/problems/sentence-similarity-iii/?envType=daily-question&envId=2024-10-06
        """
        dq1, dq2 = map(deque, (sentence1.split(), sentence2.split()))
        while dq1 and dq2 and dq1[0] == dq2[0]:
            dq1.popleft()
            dq2.popleft()
        while dq1 and dq2 and dq1[-1] == dq2[-1]:
            dq1.pop()
            dq2.pop()
        return not dq1 or not dq2

    def minLength(self, s: str) -> int:
        """
        10.07
        2696. Minimum String Length After Removing Substrings
        https://leetcode.com/problems/minimum-string-length-after-removing-substrings/?envType=daily-question&envId=2024-10-07
        """
        check = set(["AB", "CD"])
        st = []
        for x in s:
            if st and (st[-1] + x) in check:
                st.pop()
            else:
                st.append(x)
        return len(st)

    def minSwaps(self, s: str) -> int:
        """
        10.08
        1963. Minimum Number of Swaps to Make the String Balanced
        https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/?envType=daily-question&envId=2024-10-08
        ]]][]]][[[[[ -> -1, -2, -3, -2, -3, -4, -5, -4, -3, -2, -1, 0
        the optimal approach is to balance 2 sets of brackets at a time using 1 swap (hinting at result = total unbalanced / 2, which we will handle for even and odd lengths together)
        """
        cnt = 0
        ans = 0
        for c in s:
            if c == "[":
                cnt += 1
            else:
                cnt -= 1
            ans = min(ans, cnt)
        return (-ans + 1) // 2

    def minAddToMakeValid(self, s: str) -> int:
        """
        10.09
        921. Minimum Add to Make Parentheses Valid
        https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/?envType=daily-question&envId=2024-10-09
        """
        stack_size = 0
        miss_match = 0
        for c in s:
            if c == "(":
                stack_size += 1
            elif c == ")" and stack_size > 0:
                stack_size -= 1
            else:
                miss_match += 1
        return stack_size + miss_match

    def maxWidthRamp(self, nums: List[int]) -> int:
        """
        10.10
        962. Maximum Width Ramp
        https://leetcode.com/problems/maximum-width-ramp/?envType=daily-question&envId=2024-10-10
        @nums = [6,0,8,2,1,5]
        @stack = [6, 0]
        """
        stack = []
        res = 0
        for i, n in enumerate(nums):
            # keep a decreasing stack
            if not stack or nums[stack[-1]] > n:
                stack.append(i)
        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                res = max(res, i - stack.pop())
        return res

    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        """
        10.11
        1942. The Number of the Smallest Unoccupied Chair
        https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/?envType=daily-question&envId=2024-10-11
        """
        n = len(times)
        # all chairs
        h = list(range(n))
        # retain the index
        for i in range(n):
            times[i].append(i)
        times.sort()
        busy = []
        for a, b, i in times:
            while busy and busy[0][0] <= a:
                heapq.heappush(h, heapq.heappop(busy)[1])
            c = heapq.heappop(h)
            if i == targetFriend:
                return c
            heapq.heappush(busy, (b, c))
        return -1

    def minGroups(self, intervals):
        """
        10.12
        2406. Divide Intervals Into Minimum Number of Groups
        https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/?envType=daily-question&envId=2024-10-12
        """
        A = []
        for a, b in intervals:
            A.append([a, 1])
            A.append([b + 1, -1])
        res = cur = 0
        for a, diff in sorted(A):
            cur += diff
            res = max(res, cur)
        return res

    def smallestRange(self, A):
        """
        10.13
        632. Smallest Range Covering Elements from K Lists
        https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/?envType=daily-question&envId=2024-10-13
        """
        pq = [(row[0], i, 0) for i, row in enumerate(A)]
        heapq.heapify(pq)

        ans = -1e9, 1e9
        right = max(row[0] for row in A)
        while pq:
            left, i, j = heapq.heappop(pq)
            if right - left < ans[1] - ans[0]:
                ans = left, right
            if j + 1 == len(A[i]):
                return ans
            v = A[i][j + 1]
            right = max(right, v)
            heapq.heappush(pq, (v, i, j + 1))

    def maxKelements(self, nums: List[int], k: int) -> int:
        """
        10.14
        2530. Maximal Score After Applying K Operations
        https://leetcode.com/problems/maximal-score-after-applying-k-operations/?envType=daily-question&envId=2024-10-14
        """
        pq = [-x for x in nums]
        heapq.heapify(pq)
        ans = 0
        for _ in range(k):
            ans -= pq[0]
            heapq.heapreplace(pq, pq[0] // 3)
        return ans

    def minimumSteps(self, s: str) -> int:
        """
        10.15
        2938. Separate Black and White Balls
        https://leetcode.com/problems/separate-black-and-white-balls/?envType=daily-question&envId=2024-10-15
        """
        res = 0
        r = 0
        for i in range(len(s)):
            if s[i] == "0":
                res += i - r
                r += 1
        return res

    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        """
        10.16
        1405. Longest Happy String
        https://leetcode.com/problems/longest-happy-string/?envType=daily-question&envId=2024-10-16
        """
        max_heap = []
        for count, token in (-a, "a"), (-b, "b"), (-c, "c"):
            if count:
                heapq.heappush(max_heap, (count, token))
        result = ""
        while max_heap:
            count, token = heapq.heappop(max_heap)
            if len(result) > 1 and result[-2] == result[-1] == token:
                if not max_heap:
                    break
                count, token = heapq.heapreplace(max_heap, (count, token))
            result += token
            if count + 1:
                heapq.heappush(max_heap, (count + 1, token))
        return result

    def maximumSwap(self, num: int) -> int:
        """
        10.17
        670. Maximum Swap
        https://leetcode.com/problems/maximum-swap/?envType=daily-question&envId=2024-10-17
        """
        A = list(str(num))
        # dict to store the last index of each digit
        last = {int(x): i for i, x in enumerate(A)}
        for i, x in enumerate(A):
            # find the largest digit that is smaller than the current digit
            for d in range(9, int(x), -1):
                if d in last and last[d] > i:
                    A[i], A[last[d]] = A[last[d]], A[i]
                    return int("".join(A))
        return num

    def countMaxOrSubsets(self, A: List[int]) -> int:
        """
        10.18
        2044. Count Number of Maximum Bitwise-OR Subsets
        https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/?envType=daily-question&envId=2024-10-18
        sack dp
        """
        dp = Counter([0])
        for a in A:
            for k, v in list(dp.items()):
                dp[k | a] += v
        return dp[max(dp)]

    def findKthBit(self, n: int, k: int) -> str:
        """
        10.19
        1545. Find Kth Bit in Nth Binary String
        https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/?envType=daily-question&envId=2024-10-19
        """
        return str(k // (k & -k) >> 1 & 1 ^ k & 1 ^ 1)

    def findKthBit1(self, n, k):
        flip = 0
        l = 2**n - 1
        while k > 1:
            if k == l // 2 + 1:
                return str(1 ^ flip)
            if k > l // 2:
                k = l + 1 - k
                flip = 1 - flip
            l //= 2
        return str(flip)

    def parseBoolExpr(self, expression: str) -> bool:
        """
        10.20
        1106. Parsing A Boolean Expression
        https://leetcode.com/problems/parsing-a-boolean-expression/?envType=daily-question&envId=2024-10-20
        """
        stack = []
        for c in expression:
            if c == ")":
                seen = set()
                while stack[-1] != "(":
                    seen.add(stack.pop())
                stack.pop()
                operator = stack.pop()
                stack.append(
                    all(seen)
                    if operator == "&"
                    else any(seen) if operator == "|" else not seen.pop()
                )
            elif c != ",":
                stack.append(True if c == "t" else False if c == "f" else c)
        return stack.pop()

    def maxUniqueSplit(self, s: str) -> int:
        """
        10.21
        1593. Split a String Into the Max Number of Unique Substrings
        https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/?envType=daily-question&envId=2024-10-21
        """

        def dfs(s, seen):
            if not s:
                return 0
            res = 0
            for i in range(1, len(s) + 1):
                if s[:i] not in seen:
                    seen.add(s[:i])
                    res = max(res, 1 + dfs(s[i:], seen))
                    seen.remove(s[:i])
            return res

        return dfs(s, set())

    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        """
        10.22
        2583. Kth Largest Level Sum in Binary Tree
        https://leetcode.com/problems/kth-largest-level-sum-in-binary-tree/?envType=daily-question&envId=2024-10-22
        """
        level_sum = {}

        def dfs(node, level):
            if not node:
                return
            level_sum[level] = level_sum.get(level, 0) + node.val
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)
        if k > len(level_sum):
            return -1
        return sorted(level_sum.values(), reverse=True)[k - 1]

    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        10.23
        2641. Cousins in Binary Tree II
        https://leetcode.com/problems/cousins-in-binary-tree-ii/?envType=daily-question&envId=2024-10-23
        use TreeNode as mapKey (aka memory address)
        """
        q = deque([root])
        child_sum = {}
        level_sum = {}
        level = 0
        while q:
            level += 1
            sz = len(q)
            sm = 0
            for _ in range(sz):
                node = q.popleft()
                sm += node.val

                l = node.left.val if node.left else 0
                r = node.right.val if node.right else 0

                child_sum[node] = l + r

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level_sum[level] = sm

        def helper(root, parent, level, child_sum, level_sum):
            if not root:
                return
            p_sum = child_sum.get(parent, 0)
            lv_sum = level_sum.get(level)
            root.val = lv_sum - p_sum
            helper(root.left, root, level + 1, child_sum, level_sum)
            helper(root.right, root, level + 1, child_sum, level_sum)

        helper(root, None, 1, child_sum, level_sum)
        root.val = 0
        return root

    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        """
        10.24
        951. Flip Equivalent Binary Trees
        https://leetcode.com/problems/flip-equivalent-binary-trees/?envType=daily-question&envId=2024-10-24
        """
        if not root1 and not root2:
            return True
        # check equality
        if not root1 or not root2 or root1.val != root2.val:
            return False
        # did not flip
        return (
            self.flipEquiv(root1.left, root2.left)
            and self.flipEquiv(root1.right, root2.right)
            # did flip
        ) or (
            self.flipEquiv(root1.left, root2.right)
            and self.flipEquiv(root1.right, root2.left)
        )

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        """
        10.25
        1233. Remove Sub-Folders from the Filesystem
        https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/?envType=daily-question&envId=2024-10-25
        """
        folder.sort()
        res = [folder[0]]
        for f in folder[1:]:
            if not f.startswith(res[-1] + "/"):
                res.append(f)
        return res

    def treeQueries(self, root, queries, ans={}) -> List[int]:
        """
        10.26
        2458. Height of Binary Tree After Subtree Removal Queries
        https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/description/?envType=daily-question&envId=2024-10-26
        """

        @cache
        def height(r):
            return 1 + max(height(r.left), height(r.right)) if r else 0

        def dfs(r, depth, mx):
            if not r:
                return
            ans[r.val] = mx
            dfs(r.left, depth + 1, max(mx, depth + height(r.right)))
            dfs(r.right, depth + 1, max(mx, depth + height(r.left)))

        dfs(root, 0, 0)
        return [ans[v] for v in queries]

    def countSquares(self, A):
        """
        10.27
        1277. Count Square Submatrices with All Ones
        https://leetcode.com/problems/count-square-submatrices-with-all-ones/?envType=daily-question&envId=2024-10-27
        """
        for i in range(1, len(A)):
            for j in range(1, len(A[0])):
                A[i][j] *= min(A[i - 1][j], A[i][j - 1], A[i - 1][j - 1]) + 1
        return sum(map(sum, A))

    def longestSquareStreak(self, nums: List[int]) -> int:
        """
        10.28
        2501. Longest Square Streak in an Array
        https://leetcode.com/problems/longest-square-streak-in-an-array/?envType=daily-question&envId=2024-10-28
        """

        sqr = Counter(sorted(set(nums)))

        for n in sqr:
            while (s := math.isqrt(n)) ** 2 == n and s in sqr:
                sqr[s] += 1
                n = s

        return c if (c := max(sqr.values())) >= 2 else -1

    def maxMoves(self, grid: List[List[int]]) -> int:
        """
        10.29
        2684. Maximum Number of Moves in a Grid
        https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/?envType=daily-question&envId=2024-10-29
        """
        m, n = len(grid), len(grid[0])
        dirs = [(0, 1), (-1, 1), (1, 1)]

        @cache
        def dp(i, j):
            res = 0
            for dx, dy in dirs:
                x, y = i + dx, j + dy
                if 0 <= x < m and y < n and grid[x][y] > grid[i][j]:
                    res = max(res, 1 + dp(x, y))
            return res

        return max(dp(i, 0) for i in range(m))

    def minimumMountainRemovals(self, A: List[int]) -> int:
        """
        10.30
        1671. Minimum Number of Removals to Make Mountain Array
        https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/?envType=daily-question&envId=2024-10-30
        """
        n = len(A)
        dp = [0] * n
        mono = [10**9] * n
        for i in range(n):
            j = bisect.bisect_left(mono, A[i])
            mono[j] = A[i]
            dp[i] += j + 1 if j else -n
        mono = [10**9] * n
        for i in range(n - 1, -1, -1):
            j = bisect.bisect_left(mono, A[i])
            mono[j] = A[i]
            dp[i] += j if j else -n
        return n - max(dp[1:-1])

    def minimumTotalDistance(self, A: List[int], B: List[List[int]]) -> int:
        """
        10.31
        24630. Minimum Total Distance Traveled
        https://leetcode.com/problems/minimum-total-distance-traveled/?envType=daily-question&envId=2024-10-31
        """
        A.sort()
        B.sort()

        @cache
        def dp(i, j, k):
            """
            dp(i,j,k), to fix robit[i] and its following robots with factory[j] which already fix k robots
            """
            # already fixed all robots
            if i == len(A):
                return 0
            # no more factories left to choose from
            if j == len(B):
                return sys.maxsize
            # option1: skip the current factory
            x = dp(i, j + 1, 0)
            # option2: choose the current factory with fix cost
            y = (
                dp(i + 1, j, k + 1) + abs(A[i] - B[j][0])
                if B[j][1] > k
                else sys.maxsize
            )
            return min(x, y)

        return dp(0, 0, 0)
