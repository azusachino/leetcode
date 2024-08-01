from collections import defaultdict, deque
from functools import reduce
import heapq
from heapq import heapify, heappush, heappop
from math import sqrt
from typing import Counter, List

from tree.local_tree import TreeNode


class Solution:
    def scoreOfString(self, s: str) -> int:
        """
        06.01
        3110. Score of a String
        https://leetcode.com/problems/score-of-a-string/description/?envType=daily-question&envId=2024-06-01
        class Solution {
            public:
                int scoreOfString(string s) {
                    int res = 0;
                    for (int i = 0; i < s.size() - 1; i++) {
                        int cur = s[i] - s[i+1];
                        if (cur > 0) {
                            res += cur;
                        } else {
                            res -= cur;
                        }
                    }
                    return res;

                }
            };
        """
        return sum(abs(ord(s[i]) - ord(s[i + 1])) for i in range(len(s) - 1))

    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        06.02
        344. Reverse String
        https://leetcode.com/problems/reverse-string/description/?envType=daily-question&envId=2024-06-02
        """
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

    def appendCharacters(self, s: str, t: str) -> int:
        """
        06.03
        2486. Append Characters to String to Make Subsequence
        https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/description/?envType=daily-question&envId=2024-06-03
        two pointers
        """
        x, y = len(s), len(t)
        i = j = 0
        while i < x and j < y:
            if s[i] == t[j]:
                j += 1
            i += 1
        return y - j

    def longestPalindrome(self, s: str) -> int:
        """
        06.04
        409. Longest Palindrome
        https://leetcode.com/problems/longest-palindrome/description/?envType=daily-question&envId=2024-06-04
        """
        cnt = Counter(s)
        res = 0
        c = 0
        for x in cnt.values():
            odd = x % 2
            if odd:
                c += 1
                x -= 1
            res += x
        if c:
            res += 1
        return res

    def commonChars(self, words: List[str]) -> List[str]:
        """
        06.05
        1002. Find Common Characters
        https://leetcode.com/problems/find-common-characters/description/?envType=daily-question&envId=2024-06-05
        """
        return list(
            reduce(lambda x, y: x & y, map(lambda x: Counter(x), words)).elements()
        )

    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """
        06.06
        846. Hand of Straights
        https://leetcode.com/problems/hand-of-straights/description/?envType=daily-question&envId=2024-06-06
        Counter
        """
        n = len(hand)
        if n % groupSize:
            return False
        cnt = Counter(hand)
        ks = sorted(list(cnt.keys()))
        for k in ks:
            while cnt[k]:
                for i in range(groupSize):
                    kk = k + i
                    if kk not in cnt or cnt[kk] - 1 < 0:
                        return False
                    cnt[kk] -= 1
        return True

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        """
        06.07
        648. Replace Words
        https://leetcode.com/problems/replace-words/description/?envType=daily-question&envId=2024-06-07
        class Trie:
            def __init__(self):
                self.children: List[Trie | None] = [None] * 26
                self.ref: int = -1

            def insert(self, w: str, i: int):
                node = self
                for c in w:
                    idx = ord(c) - ord("a")
                    if node.children[idx] is None:
                        node.children[idx] = Trie()
                    node = node.children[idx]
                node.ref = i

            def search(self, w: str) -> int:
                node = self
                for c in w:
                    idx = ord(c) - ord("a")
                    if node.children[idx] is None:
                        return -1
                    node = node.children[idx]
                    if node.ref != -1:
                        return node.ref
                return -1


        class Solution:
            def replaceWords(self, dictionary: List[str], sentence: str) -> str:
                trie = Trie()
                for i, w in enumerate(dictionary):
                    trie.insert(w, i)
                ans = []
                for w in sentence.split():
                    idx = trie.search(w)
                    ans.append(dictionary[idx] if idx != -1 else w)
                return " ".join(ans)
        """
        res = []
        # sort with length
        dictionary.sort(key=lambda x: len(x))
        ss = sentence.split(" ")
        for s in ss:
            for d in dictionary:
                if len(d) <= len(s) and s[: len(d)] == d:
                    res.append(d)
                    break
            else:
                res.append(s)
        return " ".join(res)

    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
        06.08
        523. Continuous Subarray Sum
        https://leetcode.com/problems/continuous-subarray-sum/description/?envType=daily-question&envId=2024-06-08
        sub_array sum
        """
        dic = {0: -1}
        summ = 0
        for i, n in enumerate(nums):
            if k != 0:
                summ = (summ + n) % k
            else:
                summ += n
            if summ not in dic:
                dic[summ] = i
            else:
                if i - dic[summ] >= 2:
                    return True
        return False

    def subarraysDivByK(self, A, K):
        """
        06.09
        974. Subarray Sums Divisible by K
        https://leetcode.com/problems/subarray-sums-divisible-by-k/submissions/1282917067/?envType=daily-question&envId=2024-06-09
        prefix sum
        """
        res = 0
        prefix = 0
        count = [1] + [0] * K
        for a in A:
            prefix = (prefix + a) % K
            res += count[prefix]
            count[prefix] += 1
        return res

    def heightChecker(self, heights: List[int]) -> int:
        """
        06.10
        1051. Height Checker
        https://leetcode.com/problems/height-checker/submissions/1283306329/?envType=daily-question&envId=2024-06-10
        """
        return sum(h1 != h2 for h1, h2 in zip(heights, sorted(heights)))

    def relativeSortArray(self, A: List[int], B: List[int]) -> List[int]:
        """
        06.11
        1122. Relative Sort Array
        https://leetcode.com/problems/relative-sort-array/description/?envType=daily-question&envId=2024-06-11
        """
        k = {b: i for i, b in enumerate(B)}
        return sorted(A, key=lambda a: k.get(a, 1000 + a))

    def sortColors(self, nums):
        """
        06.12
        75. Sort Colors
        https://leetcode.com/problems/sort-colors/description/?envType=daily-question&envId=2024-06-12
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        p1, p2 = 0, len(nums) - 1
        p = 0
        while p <= p2:
            if nums[p] < 1:
                nums[p], nums[p1] = nums[p1], nums[p]
                p1 += 1
                p += 1
            elif nums[p] > 1:
                nums[p], nums[p2] = nums[p2], nums[p]
                p2 -= 1
            else:
                p += 1

    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        """
        06.13
        2037. Minimum Number of Moves to Seat Everyone
        https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/?envType=daily-question&envId=2024-06-13
        """
        return sum(abs(x - y) for (x, y) in zip(sorted(seats), sorted(students)))

    def minIncrementForUnique(self, nums: List[int]) -> int:
        """
        06.14
        945. Minimum Increment to Make Array Unique
        https://leetcode.com/problems/minimum-increment-to-make-array-unique/description/?envType=daily-question&envId=2024-06-14
        """
        res = need = 0
        for n in sorted(nums):
            res += max(need - n, 0)
            need = max(need + 1, n + 1)
        return res

    def findMaximizedCapital(self, k, W, Profits, Capital):
        """
        06.15
        502. IPO
        https://leetcode.com/problems/ipo/description/?envType=daily-question&envId=2024-06-15
        """
        heap = []
        projects = sorted(zip(Profits, Capital), key=lambda l: l[1])
        i = 0
        for _ in range(k):
            while i < len(projects) and projects[i][1] <= W:
                heapq.heappush(heap, -projects[i][0])
                i += 1
            if heap:
                W -= heapq.heappop(heap)
        return W

    def minPatches(self, nums, n):
        """
        06.16
        330. Patching Array
        https://leetcode.com/problems/patching-array/description/?envType=daily-question&envId=2024-06-16
        """
        ints, patches = [[0, 0]], 0
        for num in nums:
            ints = self.merge(ints + [[i + num, j + num] for i, j in ints])

        while ints[0][1] < n:
            ints = self.merge(
                ints + [[i + ints[0][1] + 1, j + ints[0][1] + 1] for i, j in ints]
            )
            patches += 1

        return patches

    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        merged = []

        for interval in intervals:
            if not merged or merged[-1][1] < interval[0] - 1:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

    def judgeSquareSum(self, c: int) -> bool:
        """
        06.17
        633. Sum of Square Numbers
        https://leetcode.com/problems/sum-of-square-numbers/description/?envType=daily-question&envId=2024-06-17
        """
        for a in range(int(sqrt(c)) + 1):
            b = sqrt(c - a * a)
            if b == int(b):
                return True
        return False

    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        06.18
        826. Most Profit Assigning Work
        https://leetcode.com/problems/most-profit-assigning-work/description/?envType=daily-question&envId=2024-06-18
        """
        jobs = sorted(zip(difficulty, profit))
        res = i = best = 0
        for ability in sorted(worker):
            while i < len(jobs) and ability >= jobs[i][0]:
                best = max(jobs[i][1], best)
                i += 1
            res += best
        return res

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        """
        06.19
        1482. Minimum Number of Days to Make m Bouquets
        https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/description/?envType=daily-question&envId=2024-06-19
        """

        def feasible(days) -> bool:
            bonquets, flowers = 0, 0
            for bloom in bloomDay:
                if bloom > days:
                    flowers = 0
                else:
                    bonquets += (flowers + 1) // k
                    flowers = (flowers + 1) % k
            return bonquets >= m

        if len(bloomDay) < m * k:
            return -1
        left, right = 1, max(bloomDay)
        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left

    def maxDistance(self, position: List[int], m: int) -> int:
        """
        06.20
        1552. Magnetic Force Between Two Balls
        https://leetcode.com/problems/magnetic-force-between-two-balls/description/?envType=daily-question&envId=2024-06-20
        """
        n = len(position)
        position.sort()

        def count(d):
            ans, curr = 1, position[0]
            for i in range(1, n):
                if position[i] - curr >= d:
                    ans += 1
                    curr = position[i]
            return ans

        l, r = 0, position[-1] - position[0]
        while l < r:
            mid = r - (r - l) // 2
            if count(mid) >= m:
                l = mid
            else:
                r = mid - 1
        return l

    def maxSatisfied(self, customers: List[int], grumpy: List[int], k: int) -> int:
        """
        06.21
        1052. Grumpy Bookstore Owner
        https://leetcode.com/problems/grumpy-bookstore-owner/description/?envType=daily-question&envId=2024-06-21
        """
        n = len(customers)
        # the base score we could ensure
        res = sum([customers[i] * (1 - grumpy[i]) for i in range(n)])
        # initial sliding window
        best_gain = sum([customers[i] * grumpy[i] for i in range(k)])
        gain = best_gain
        for i in range(k, n):
            # add new values, kick out old values
            gain += customers[i] * grumpy[i] - customers[i - k] * grumpy[i - k]
            best_gain = max(best_gain, gain)
        return res + best_gain

    def numberOfSubarrays(self, A, k):
        """
        06.22
        1248. Count Number of Nice Subarrays
        https://leetcode.com/problems/count-number-of-nice-subarrays/description/?envType=daily-question&envId=2024-06-22
        sliding window
        """

        def atMost(k):
            res = i = 0
            for j in range(len(A)):
                k -= A[j] % 2
                while k < 0:
                    k += A[i] % 2
                    i += 1
                res += j - i + 1
            return res

        return atMost(k) - atMost(k - 1)

    def longestSubarray(self, A, limit):
        """
        06.23
        1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
        https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/description/?envType=daily-question&envId=2024-06-23
        heap
        """
        maxq, minq = [], []
        res = i = 0
        for j, a in enumerate(A):
            heapq.heappush(maxq, [-a, j])
            heapq.heappush(minq, [a, j])
            while -maxq[0][0] - minq[0][0] > limit:
                i = min(maxq[0][1], minq[0][1]) + 1
                while maxq[0][1] < i:
                    heapq.heappop(maxq)
                while minq[0][1] < i:
                    heapq.heappop(minq)
            res = max(res, j - i + 1)
        return res

    def minKBitFlips(self, nums, k):
        """
        06.24
        995. Minimum Number of K Consecutive Bit Flips
        https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/description/?envType=daily-question&envId=2024-06-25
        Queue
        """
        n = len(nums)
        queue = deque()  # Stores indices of active flips
        flips = 0  # Count of flips

        for i in range(n):
            # Check if the oldest flip is still active within the window
            if queue and queue[0] == i - k:
                queue.popleft()

            # If the current element is 0, we need to flip
            if not (nums[i] ^ len(queue) & 1):
                if i + k > n:
                    return -1  # Impossible to flip
                queue.append(i)
                flips += 1

        return flips

    def bstToGst(self, root: TreeNode) -> TreeNode:
        """
        06.25
        1038. Binary Search Tree to Greater Sum Tree
        https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/description/?envType=daily-question&envId=2024-06-25
        BST, post-traverse
        """
        self.total = 0

        def dfs(node):
            if not node:
                return
            dfs(node.right)
            self.total += node.val
            node.val = self.total
            dfs(node.left)

        dfs(root)
        return root

    def balanceBST(self, root: TreeNode) -> TreeNode:
        """
        06.26
        1038. Binary Search Tree to Greater Sum Tree
        https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/description/?envType=daily-question&envId=2024-06-26
        inorder, buildBST
        """
        nodes = []

        def inorder(node: TreeNode):
            if node:
                inorder(node.left)
                nodes.append(node)
                inorder(node.right)

        inorder(root)

        def buildBST(start, end):
            if start > end:
                return None
            mid = (start + end) // 2
            node = nodes[mid]
            node.left = buildBST(start, mid - 1)
            node.right = buildBST(mid + 1, end)
            return node

        return buildBST(0, len(nodes) - 1)

    def findCenter(self, e):
        """
        06.27
        1791. Find Center of Star Graph
        https://leetcode.com/problems/find-center-of-star-graph/description/?envType=daily-question&envId=2024-06-27
        """
        return e[0][e[0][1] in e[1]]

    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        """
        06.28
        2285. Maximum Total Importance of Roads
        https://leetcode.com/problems/maximum-total-importance-of-roads/description/?envType=daily-question&envId=2024-06-28
        """
        g = defaultdict(list)
        for x, y in roads:
            g[x].append(y)
            g[y].append(x)
        n = len(g)
        q = []
        for x, v in g.items():
            heappush(q, [-len(v), x])
        m = {}
        while q:
            m[heappop(q)] = n
            n -= 1

        return sum(m[x] + m[y] for x, y in roads)

    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        """
        06.29
        2192. All Ancestors of a Node in a Directed Acyclic Graph
        https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/description/?envType=daily-question&envId=2024-06-29
        graph, dfs
        """
        direct_child = defaultdict(list)
        ans = [[] for _ in range(n)]
        for x, y in edges:
            direct_child[x].append(y)

        def dfs(x, curr):
            for ch in direct_child[curr]:
                if ans[ch] and ans[ch][-1] == x:
                    continue
                ans[ch].append(x)
                dfs(x, ch)

        for i in range(n):
            dfs(i, i)
        return ans

    def maxNumEdgesToRemove(self, n, edges):
        """
        06.30
        1579. Remove Max Number of Edges to Keep Graph Fully Traversable
        https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/description
        """

        # Union find
        def find(i):
            if i != root[i]:
                root[i] = find(root[i])
            return root[i]

        def uni(x, y):
            x, y = find(x), find(y)
            if x == y:
                return 0
            root[x] = y
            return 1

        res = e1 = e2 = 0

        # Alice and Bob
        root = list(range(n + 1))
        for t, i, j in edges:
            if t == 3:
                if uni(i, j):
                    e1 += 1
                    e2 += 1
                else:
                    res += 1
        root0 = root[:]

        # only Alice
        for t, i, j in edges:
            if t == 1:
                if uni(i, j):
                    e1 += 1
                else:
                    res += 1

        # only Bob
        root = root0
        for t, i, j in edges:
            if t == 2:
                if uni(i, j):
                    e2 += 1
                else:
                    res += 1

        return res if e1 == e2 == n - 1 else -1


class RandomSolution:
    def printVertically(self, s: str) -> List[str]:
        """
        1324. Print Words Vertically
        https://leetcode.com/problems/print-words-vertically/description/
        string array
        """
        words = s.split(" ")
        # max size of word, as the indicator of result
        n = max([len(w) for w in words])
        res = []
        for j in range(n):
            # array with j-index values
            t = [w[j] if j < len(w) else " " for w in words]
            # trim suffix ' '
            while t[-1] == " ":
                t.pop()
            res.append("".join(t))
        return res

    def minSumSquareDiff(
        self, nums1: List[int], nums2: List[int], k1: int, k2: int
    ) -> int:
        """
        2333. Minimum Sum of Squared Difference
        https://leetcode.com/problems/minimum-sum-of-squared-difference/description/
        """
        heap = [-abs(x - y) for x, y in zip(nums1, nums2)]
        s = -sum(heap)
        delta = k1 + k2
        if delta >= s:
            return 0
        heapify(heap)
        n = len(nums1)
        while delta > 0:
            d = -heappop(heap)
            gap = max(delta // n, 1) if heap else delta
            d -= gap
            heappush(heap, -d)
            delta -= gap
        return sum(pow(e, 2) for e in heap)

    def findCenter(self, edges: List[List[int]]) -> int:
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        res = 0
        l = 0
        for k, v in g.items():
            if len(v) > l:
                l = len(v)
                res = k
        return res

    def maximumImportance(self, n: int, a: List[List[int]]) -> int:
        d = [0 for _ in range(n)]
        # node degree
        for x, y in a:
            d[x] += 1
            d[y] += 1
        d.sort()
        ans = 0
        for i in range(1, n + 1):
            ans += i * d[i - 1]
        return ans
