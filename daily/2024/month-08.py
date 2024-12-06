from bisect import bisect_left
from collections import defaultdict
import copy
from functools import cache
import heapq
import itertools
from math import inf
import math
import re
from typing import Counter, List


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        """
        08.01
        2678. Number of Senior Citizens
        https://leetcode.com/problems/number-of-senior-citizens/description/
        """
        res = 0
        for d in details:
            age = int(d[11:13])
            if age > 60:
                res += 1
        return res

    def minSwaps(self, nums: List[int]) -> int:
        """
        08.02
        2134. Minimum Swaps to Group All 1's Together II
        https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/description/?envType=daily-question&envId=2024-08-02
        """
        # count one as window size
        ones = nums.count(1)
        nums += nums
        cur_one_cnt = max_one_cnt = 0
        for i in range(len(nums)):
            if i >= ones and nums[i - ones]:
                cur_one_cnt -= 1
            if nums[i]:
                cur_one_cnt += 1
            max_one_cnt = max(max_one_cnt, cur_one_cnt)
        return ones - max_one_cnt

    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        """
        08.03
        1460. Make Two Arrays Equal by Reversing Subarrays
        https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/description/?envType=daily-question&envId=2024-08-04
        """
        return sorted(target) == sorted(arr)

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        """
        08.04
        1508. Range Sum of Sorted Subarray Sums
        https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/description/?envType=daily-question&envId=2024-08-04
        """
        arr = []
        for i in range(n):
            s = 0
            for j in range(i, n):
                s += nums[j]
                arr.append(s)
        arr.sort()
        mod = 10**9 + 7
        return sum(arr[left - 1 : right]) % mod

    def kthDistinct(self, arr: List[str], k: int) -> str:
        """
        08.05
        2053. Kth Distinct String in an Array
        https://leetcode.com/problems/kth-distinct-string-in-an-array/description/
        """
        cnt = Counter(arr)
        for i in arr:
            if cnt[i] == 1:
                k -= 1
            if k == 0:
                return i
        return ""

    def minimumPushes(self, word: str) -> int:
        """
        08.06
        3016. Minimum Number of Pushes to Type Word II
        https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/description/?envType=daily-question&envId=2024-08-06
        """
        cnt = Counter(word)
        # only frequency matter
        chr = sorted(cnt.values(), reverse=True)
        """
            res = 0
            for i, w in enumerate(words):
                cost = i//8+1
                res += cost * w
            return res
        """
        return (
            sum(chr[:8]) + 2 * sum(chr[8:16]) + 3 * sum(chr[16:24]) + 4 * sum(chr[24:])
        )

    def numberToWords(self, num: int) -> str:
        """
        08.07
        273. Integer to English Words
        https://leetcode.com/problems/integer-to-english-words/description/?envType=daily-question&envId=2024-08-07
        """
        if num == 0:
            return "Zero"
        ones = [
            "",
            "One",
            "Two",
            "Three",
            "Four",
            "Five",
            "Six",
            "Seven",
            "Eight",
            "Nine",
            "Ten",
            "Eleven",
            "Twelve",
            "Thirteen",
            "Fourteen",
            "Fifteen",
            "Sixteen",
            "Seventeen",
            "Eighteen",
            "Nineteen",
        ]
        tens = [
            "",
            "Ten",
            "Twenty",
            "Thirty",
            "Forty",
            "Fifty",
            "Sixty",
            "Seventy",
            "Eighty",
            "Ninety",
        ]

        def helper(num: int) -> str:
            if num >= 1000000000:
                return (
                    helper(num // 1000000000) + " Billion " + helper(num % 1000000000)
                )

            if num >= 1000000:
                return helper(num // 1000000) + " Million " + helper(num % 1000000)

            if num >= 1000:
                return helper(num // 1000) + " Thousand " + helper(num % 1000)

            if num >= 100:
                return (helper(num // 100) + " Hundred " + helper(num % 100)).strip()

            if num >= 20:
                return (tens[num // 10] + " " + helper(num % 10)).strip()

            return ones[num]

        return helper(num).strip()

    def spiralMatrixIII(
        self, rows: int, cols: int, rStart: int, cStart: int
    ) -> List[List[int]]:
        """
        08.08
        885. Spiral Matrix III
        https://leetcode.com/problems/spiral-matrix-iii/description/?envType=daily-question&envId=2024-08-08
        @credit https://leetcode.ca/2018-03-19-840-Magic-Squares-In-Grid/
        """
        res = [[rStart, cStart]]
        n = rows * cols
        if n == 1:
            return res
        next_round = 1
        while True:
            # right, down -> step
            # left, up -> step + 1
            for r, c, round in [
                [0, 1, next_round],
                [1, 0, next_round],
                [0, -1, next_round + 1],
                [-1, 0, next_round + 1],
            ]:
                for _ in range(round):
                    rStart += r
                    cStart += c
                    if 0 <= rStart < rows and 0 <= cStart < cols:
                        res.append([rStart, cStart])
                        if len(res) == n:
                            return res
            # two more elements for next round
            next_round += 2

    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        """
        08.09
        840. Magic Squares In Grid
        https://leetcode.com/problems/magic-squares-in-grid/description/?envType=daily-question&envId=2024-08-09
        """

        def check(i: int, j: int) -> int:
            if i + 3 > m or j + 3 > n:
                return 0
            s = set()
            row = [0] * 3
            col = [0] * 3
            a = b = 0
            for x in range(i, i + 3):
                for y in range(j, j + 3):
                    v = grid[x][y]
                    if v < 1 or v > 9:
                        return 0
                    s.add(v)
                    row[x - i] += v
                    col[y - j] += v
                    if x - i == y - j:
                        a += v
                    if x - i == 2 - (y - j):
                        b += v
            if len(s) != 9 or a != b:
                return 0
            if any(x != a for x in row) or any(x != a for x in col):
                return 0
            return 1

        m, n = len(grid), len(grid[0])
        return sum(check(i, j) for i in range(m) for j in range(n))

    def regionsBySlashes(self, grid):
        """
        08.10
        959. Regions Cut By Slashes
        https://leetcode.com/problems/regions-cut-by-slashes
        """
        f = {}

        def find(x):
            f.setdefault(x, x)
            if x != f[x]:
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            f[find(x)] = find(y)

        for i in range(len(grid)):
            for j in range(len(grid)):
                if i:
                    union((i - 1, j, 2), (i, j, 0))
                if j:
                    union((i, j - 1, 1), (i, j, 3))
                if grid[i][j] != "/":
                    union((i, j, 0), (i, j, 1))
                    union((i, j, 2), (i, j, 3))
                if grid[i][j] != "\\":
                    union((i, j, 3), (i, j, 0))
                    union((i, j, 1), (i, j, 2))
        return len(set(map(find, f)))

    # this is just a helper function for the no_islands function below
    def no_islands_recur(self, grid, i, j, m, n):
        if grid[i][j] == 0:
            return
        grid[i][j] = 0
        if i - 1 >= 0:
            self.no_islands_recur(grid, i - 1, j, m, n)
        if i + 1 < m:
            self.no_islands_recur(grid, i + 1, j, m, n)
        if j - 1 >= 0:
            self.no_islands_recur(grid, i, j - 1, m, n)
        if j + 1 < n:
            self.no_islands_recur(grid, i, j + 1, m, n)

    # find how many islands the given grid has
    def no_islands(self, grid):
        ret = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ret += 1
                    self.no_islands_recur(grid, i, j, m, n)
        return ret

    def minDays(self, grid: List[List[int]]) -> int:
        """
        08.11
        1568. Minimum Number of Days to Disconnect Island
        https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island
        """
        # if we have 0 or more than 1 islands at day 0, return day 0
        time = 0
        grid_copy = copy.deepcopy(grid)
        n = self.no_islands(grid_copy)
        if n != 1:
            return time

        # try to remove any land any see if it works
        time = 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid_copy = copy.deepcopy(grid)
                grid_copy[i][j] = 0
                n = self.no_islands(grid_copy)
                if n != 1:
                    return time

        # well then just return 2
        time = 2
        return time

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        08.13
        40. Combination Sum II
        https://leetcode.com/problems/combination-sum-ii/description/?envType=daily-question&envId=2024-08-13
        """
        candidates.sort()
        res = []
        tmp = []
        n = len(candidates)

        def backtrack(i, s):
            if s > target:
                return
            if s == target:
                res.append(tmp[:])
                return
            for j in range(n):
                # remove duplicates
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                tmp.append(candidates[j])
                backtrack(j + 1, s + candidates[j])
                tmp.pop()

        backtrack(0, 0)
        return res

    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        """
        08.14
        719. Find K-th Smallest Pair Distance
        https://leetcode.com/problems/find-k-th-smallest-pair-distance/description/?envType=daily-question&envId=2024-08-14
        """

        # return sorted(abs(x - y) for x, y in itertools.combinations(nums, 2))[k - 1]
        def count(dist):
            cnt = 0
            for i, b in enumerate(nums):
                a = b - dist
                j = bisect_left(nums, a, 0, i)
                cnt += i - j
            return cnt

        nums.sort()
        return bisect_left(range(nums[-1] - nums[0]), k, key=count)

    def lemonadeChange(self, bills: List[int]) -> bool:
        """
        08.15
        860. Lemonade Change
        https://leetcode.com/problems/lemonade-change/description/?envType=daily-question&envId=2024-08-15
        """
        five = ten = 0
        for b in bills:
            if b == 5:
                five += 1
            elif b == 10:
                if five < 1:
                    return False
                five -= 1
                ten += 1
            else:
                if (ten < 1 and five < 3) or (ten > 0 and five < 1):
                    return False
                if ten > 0:
                    ten -= 1
                    five -= 1
                else:
                    five -= 3
        return True

    def maxDistance(self, arrays: List[List[int]]) -> int:
        """
        08.16
        624. Maximum Distance in Arrays
        https://leetcode.com/problems/maximum-distance-in-arrays/description/?envType=daily-question&envId=2024-08-16
        """
        ans = 0
        mi, mx = arrays[0][0], arrays[0][-1]
        for arr in arrays[1:]:
            a, b = abs(arr[0] - mx), abs(arr[-1] - mi)
            ans = max(ans, a, b)
            mi = min(mi, arr[0])
            mx = max(mx, arr[-1])
        return ans

    def maxPoints(self, P: List[List[int]]) -> int:
        """
        08.17
        1937. Maximum Number of Points with Cost
        https://leetcode.com/problems/maximum-number-of-points-with-cost/description/?envType=daily-question&envId=2024-08-17
        """
        m, n = len(P), len(P[0])
        if m == 1:
            return max(P[0])
        if n == 1:
            return sum(sum(x) for x in P)

        def left(arr):
            lft = [arr[0]] + [0] * (n - 1)
            for i in range(1, n):
                lft[i] = max(lft[i - 1] - 1, arr[i])
            return lft

        def right(arr):
            rgt = [0] * (n - 1) + [arr[-1]]
            for i in range(n - 2, -1, -1):
                rgt[i] = max(rgt[i + 1] - 1, arr[i])
            return rgt

        pre = P[0]
        for i in range(m - 1):
            lft, rgt, cur = left(pre), right(pre), [0] * n
            for j in range(n):
                cur[j] = P[i + 1][j] + max(lft[j], rgt[j])
            pre = cur[:]

        return max(pre)

    def nthUglyNumber(self, n):
        """
        08.18
        264. Ugly Number II
        https://leetcode.com/problems/ugly-number-ii/description/?envType=daily-question&envId=2024-08-18
        """
        ugly = [1]
        i2, i3, i5 = 0, 0, 0
        while n > 1:
            u2, u3, u5 = 2 * ugly[i2], 3 * ugly[i3], 5 * ugly[i5]
            umin = min((u2, u3, u5))
            if umin == u2:
                i2 += 1
            if umin == u3:
                i3 += 1
            if umin == u5:
                i5 += 1
            ugly.append(umin)
            n -= 1
        return ugly[-1]

    def minSteps(self, n: int) -> int:
        """
        08.19
        650. 2 Keys Keyboard
        https://leetcode.com/problems/2-keys-keyboard/description/?envType=daily-question&envId=2024-08-19
            dp = [0] * (n + 1)

            # variation start from 2
            for i in range(2, n + 1):
                # worst case for every n
                dp[i] = i
                for j in range(i // 2, 1, -1):
                    # when pasting is better operation
                    if i % j == 0:
                        dp[i] = dp[j] + (i // j)
                        break
            return dp[n]
        """
        res = 0
        i = 2
        while n > 1:
            while n % i == 0:
                res += i
                n //= i
            i += 1
        return res

    def stoneGameII(self, piles: List[int]) -> int:
        """
        08.20
        1140. Stone Game II
        https://leetcode.com/problems/stone-game-ii/description/
        """

        @cache
        def dfs(i, m):
            # capable of taking all rest
            if m * 2 >= n - i:
                return s[n] - s[i]
            return max(
                s[n] - s[i] - dfs(i + x, max(m, x)) for x in range(1, m << 1 | 1)
            )

        n = len(piles)
        s = list(itertools.accumulate(piles, initial=0))
        return dfs(0, 1)

    def strangePrinter(self, s: str) -> int:
        """
        08.21
        664. Strange Printer
        https://leetcode.com/problems/strange-printer/description/
        @credit https://leetcode.ca/2017-09-24-664-Strange-Printer/
        """
        n = len(s)
        dp = [[inf] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i][j - 1]
                else:
                    for k in range(i, j):
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j])
        return dp[0][n - 1]

    def findComplement(self, num: int) -> int:
        """
        08.22
        476. Number Complement
        https://leetcode.com/problems/number-complement/description/?envType=daily-question&envId=2024-08-22
        """
        return num ^ (2 ** (int(math.log(num, 2)) + 1) - 1)

    def fractionAddition(self, expression: str) -> str:
        """
        08.23
        592. Fraction Addition and Subtraction
        https://leetcode.com/problems/fraction-addition-and-subtraction/description/?envType=daily-question&envId=2024-08-23
        @credit https://leetcode.com/problems/fraction-addition-and-subtraction/solutions/103384/small-simple-c-java-python/?envType=daily-question&envId=2024-08-23
        Split by + and -, and sum up all fractions.
            def fractionAddition(self, exp):
                res = sum(map(f, re.findall('[+-]?\d+/\d+', exp)))
                return '%s/%s' % (res.numerator, res.denominator)
        """
        ints = map(int, re.findall("[+-]?\d+", expression))
        A, B = 0, 1
        for a in ints:
            b = next(ints)
            A = A * b + a * B
            B *= b
            g = math.gcd(A, B)
            A //= g
            B //= g
        return "%d/%d" % (A, B)

    def nearestPalindromic(self, n):
        """
        08.24
        564. Find the Closest Palindrome
        https://leetcode.com/problems/find-the-closest-palindrome/description/?envType=daily-question&envId=2024-08-24
        """
        # based on @awice and @o_sharp
        l = len(n)
        # with different digits width, it must be either 10...01 or 9...9
        candidates = set((str(10**l + 1), str(10 ** (l - 1) - 1)))
        # the closest must be in middle digit +1, 0, -1, then flip left to right
        prefix = int(n[: (l + 1) // 2])
        for i in map(str, (prefix - 1, prefix, prefix + 1)):
            candidates.add(i + [i, i[:-1]][l & 1][::-1])
        candidates.discard(n)
        return min(candidates, key=lambda x: (abs(int(x) - int(n)), int(x)))

    def postorderTraversal(self, root):
        """
        08.25
        145. Binary Tree Postorder Traversal
        https://leetcode.com/problems/binary-tree-postorder-traversal/description/?envType=daily-question&envId=2024-08-25
        """
        traversal, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                # pre-order, right first
                traversal.append(node.val)
                stack.append(node.left)
                stack.append(node.right)

        # reverse result
        return traversal[::-1]

    def postorder(self, root) -> List[int]:
        """
        08.26
        590. N-ary Tree Postorder Traversal
        https://leetcode.com/problems/n-ary-tree-postorder-traversal/description/?envType=daily-question&envId=2024-08-26
        def postorder(self, root):
            res = []
            if root == None: return res

            stack = [root]
            while stack:
                curr = stack.pop()
                res.append(curr.val)
                stack.extend(curr.children)

            return res[::-1]
        """
        res = []

        def dfs(node):
            if node:
                if node.children:
                    for x in node.children:
                        dfs(x)
                res.append(node.val)

        dfs(root)
        return res

    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start_node: int,
        end_node: int,
    ) -> float:
        """
        08.27, 31
        1514. Path with Maximum Probability
        https://leetcode.com/problems/path-with-maximum-probability/description/?envType=daily-question&envId=2024-08-27
        """
        g = defaultdict(list)
        for (x, y), p in zip(edges, succProb):
            g[x].append((y, p))
            g[y].append((x, p))

        # node, distance
        q = [(-1.0, start_node)]
        seen = set()
        while q:
            sz = len(q)
            for _ in range(sz):
                d, cur = heapq.heappop(q)
                if cur == end_node:
                    return -d
                for nxt, p in g[cur]:
                    if nxt not in seen:
                        heapq.heappush(q, (d * p, nxt))
                seen.add(cur)
        return 0.0

    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        """
        08.28
        1905. Count Sub Islands
        https://leetcode.com/problems/count-sub-islands/description/?envType=daily-question&envId=2024-08-28
        """
        m, n = len(grid1), len(grid1[0])
        dirs = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        res = 0

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid2[i][j] == 0:
                return True
            if grid1[i][j] == 0:
                return False
            grid2[i][j] = 0

            tmp = True
            for x, y in dirs:
                tmp &= dfs(i + x, j + y)
            return tmp

        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    if dfs(i, j):
                        res += 1

        return res

    def removeStones(self, stones: List[List[int]]) -> int:
        """
        08.29
        947. Most Stones Removed with Same Row or Column
        https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/description/?envType=daily-question&envId=2024-08-29
        """
        uf = {}

        def find(x):
            if x != uf.setdefault(x, x):
                uf[x] = find(uf[x])
            return uf[x]

        for i, j in stones:
            uf[find(i)] = find(~j)
        return len(stones) - len({find(x) for x in uf})

    def modifiedGraphEdges(
        self, n: int, edges: List[List[int]], source: int, destination: int, target: int
    ) -> List[List[int]]:
        """
        08.30
        2699. Modify Graph Edge Weights
        https://leetcode.com/problems/modify-graph-edge-weights/description/?envType=daily-question&envId=2024-08-30
        @credit https://leetcode.com/problems/modify-graph-edge-weights/solutions/3546759/python3-dijkstra
        """
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append([v, w])
            adj[v].append([u, w])

        def dijkstra(source, adj, skip_negative):
            pq = [[0, source]]
            dist = defaultdict(lambda: inf)
            dist[source] = 0
            parent = {}
            while pq:
                d, node = heapq.heappop(pq)
                if d > dist[node]:
                    continue
                for nei, w in adj[node]:
                    if w == -1:
                        if skip_negative:
                            continue
                        w = 1

                    d2 = d + w
                    if d2 < dist[nei]:
                        dist[nei] = d2
                        parent[nei] = node
                        heapq.heappush(pq, [d2, nei])

            return dist, parent

        distR, parentR = dijkstra(destination, adj, skip_negative=True)
        if distR.get(source, inf) < target:
            return []
        dist, parent = dijkstra(source, adj, skip_negative=False)
        if dist[destination] > target:
            return []

        path = [destination]
        while path[-1] != source:
            path.append(parent[path[-1]])
        path = path[::-1]

        edges = {(min(u, v), max(u, v)): w for u, v, w in edges}


"""
08.12
703. Kth Largest Element in a Stream
https://leetcode.com/problems/kth-largest-element-in-a-stream/description
"""


class KthLargest(object):

    def __init__(self, k, nums):
        self.pool = nums
        self.k = k
        heapq.heapify(self.pool)
        while len(self.pool) > k:
            heapq.heappop(self.pool)

    def add(self, val):
        if len(self.pool) < self.k:
            heapq.heappush(self.pool, val)
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool, val)
        return self.pool[0]
