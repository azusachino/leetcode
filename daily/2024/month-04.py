from collections import defaultdict, deque
from functools import reduce
import heapq
from operator import xor
from typing import List, Optional

from tree.local_tree import TreeNode


class Solution:
    """
    Daily LeetCode of 2024.04
    """

    def addOneRow(
        self, root: Optional[TreeNode], val: int, depth: int
    ) -> Optional[TreeNode]:
        """
        2024-04-16
        623. Add One Row to Tree
        https://leetcode.com/problems/add-one-row-to-tree
        DFS
        """

        def dfs(node, level):
            if not node:
                return
            if level == depth - 1:
                node.left = TreeNode(val, node.left, None)
                node.right = TreeNode(val, None, node.right)
                return
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        if depth == 1:
            return TreeNode(val, root)
        dfs(root, 1)
        return root

    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        """
        2024-04-17
        988. Smallest String Starting From Leaf
        https://leetcode.com/problems/smallest-string-starting-from-leaf
        DFS
        """
        # worst case
        self.res = [26]
        # dfs path tracker
        self.cur = []

        def dfs(node):
            self.cur.append(node.val)
            # reach left node
            if not node.left and not node.right:
                self.res = min(self.res, self.cur[::-1])
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            self.cur.pop()

        dfs(root)
        return "".join("abcdefghijklmnopqrstuvwxyz"[i] for i in self.res)

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        2024-04-18
        463. Island Perimeter
        https://leetcode.com/problems/island-perimeter
        DFS
        """
        res = 0
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res += 4
                    for x, y in dirs:
                        a, b = i + x, j + y
                        if 0 <= a < m and 0 <= b < n and grid[a][b] == 1:
                            res -= 1
        return res

    def numIslands(self, grid: List[List[str]]) -> int:
        """
        2024-04-19
        200. Number of Islands
        https://leetcode.com/problems/number-of-islands
        DFS
        """
        m, n = len(grid), len(grid[0])
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        res = 0

        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == "0":
                return
            grid[i][j] = "0"
            for x, y in dirs:
                dfs(i + x, j + y)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j)
                    res += 1
        return res

    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        """
        2024-04-20
        1992. Find All Groups of Farmland
        https://leetcode.com/problems/find-all-groups-of-farmland
        DFS/BFS
        """
        rows, cols = len(land), len(land[0])
        result = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()

        def bfs(start_row, start_col):
            queue = deque([(start_row, start_col)])
            visited.add((start_row, start_col))
            min_row, min_col, max_row, max_col = (
                start_row,
                start_col,
                start_row,
                start_col,
            )

            while queue:
                cur_row, cur_col = queue.popleft()

                for dr, dc in directions:
                    new_row, new_col = cur_row + dr, cur_col + dc

                    if (
                        0 <= new_row < rows
                        and 0 <= new_col < cols
                        and (new_row, new_col) not in visited
                        and land[new_row][new_col] == 1
                    ):
                        visited.add((new_row, new_col))
                        queue.append((new_row, new_col))
                        min_row = min(min_row, new_row)
                        min_col = min(min_col, new_col)
                        max_row = max(max_row, new_row)
                        max_col = max(max_col, new_col)

            return [min_row, min_col, max_row, max_col]

        for i in range(rows):
            for j in range(cols):
                if land[i][j] == 1 and (i, j) not in visited:
                    farmland = bfs(i, j)
                    result.append(farmland)

        return result

    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        """
        2024-04-21
        1971. Find if Path Exists in Graph
        https://leetcode.com/problems/find-if-path-exists-in-graph/
        UnionFind
        """
        uf = list(range(n))

        def find(x):
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        def uni(x, y):
            a, b = find(x), find(y)
            if a == b:
                return
            uf[b] = a

        for x, y in edges:
            uni(x, y)

        return find(source) == find(destination)

    def openLock(self, deadends: List[str], target: str) -> int:
        """
        2024-04-22
        752. Open the Lock
        https://leetcode.com/problems/open-the-lock/description/?envType=daily-question&envId=2024-04-22
        BFS
        """
        st = set(deadends)
        q = deque(["0000"])
        step = 0
        while q:
            sz = len(q)
            for _ in range(sz):
                cur = q.popleft()
                if cur == target:
                    return step

                # skip already visited pattern
                if cur in st:
                    continue
                st.add(cur)

                # next pattern
                for i in range(4):
                    plus, minus = "", ""
                    if cur[i] == "9":
                        plus = cur[:i] + "0" + cur[i + 1 :]
                    else:
                        plus = cur[:i] + str(int(cur[i]) + 1) + cur[i + 1 :]
                    if cur[i] == "0":
                        minus = cur[:i] + "9" + cur[i + 1 :]
                    else:
                        minus = cur[:i] + str(int(cur[i]) - 1) + cur[i + 1 :]
                    if plus not in st:
                        q.append(plus)
                    if minus not in st:
                        q.append(minus)
            step += 1
        return -1

    def findMinHeightTrees(self, n, edges):
        """
        2024-04-23
        310. Minimum Height Trees
        https://leetcode.com/problems/minimum-height-trees/description/?envType=daily-question&envId=2024-04-23
        Basically, the idea is to eat up all the leaves at the same time, until one/two leaves are left.
        """
        if n == 1:
            return [0]
        adj = [set() for _ in range(n)]
        # adjacent table
        for x, y in edges:
            adj[x].add(y)
            adj[y].add(x)

        # the initial leaf nodes
        leaf = [i for i in range(n) if len(adj[i]) == 1]

        # at least 2 top nodes
        while n > 2:
            n -= len(leaf)
            new_leaf = []
            for i in leaf:
                # for each leaf node, pop out its `parent` node
                j = adj[i].pop()
                # remove from the `parent` adjacent table
                adj[j].remove(i)
                # if the `parent` becomes new leaf, add to next iteration
                if len(adj[j]) == 1:
                    new_leaf.append(j)
            leaf = new_leaf
        return leaf

    def tribonacci(self, n: int) -> int:
        """
        2024-04-24
        1137. N-th Tribonacci Number
        https://leetcode.com/problems/n-th-tribonacci-number/description/?envType=daily-question&envId=2024-04-24
        DP
        """
        a, b, c = 1, 0, 0
        for _ in range(n):
            a, b, c = b, c, a + b + c
        return c

    def longestIdealString(self, s: str, k: int) -> int:
        """
        2024-04-25
        2370. Longest Ideal Subsequence
        https://leetcode.com/problems/longest-ideal-subsequence
        dp[c] means the length of the longest ideal subsequence
        ending with character c.

        Iterate the character i in string s,
        c can be the next character for string ending from i - k to i + k.
        So that dp[i] = max(dp[i-k], dp[i-k+1] ... , dp[i+k]) + 1.

        return the max(dp) as result.
        """
        dp = [0] * 128
        for c in s:
            i = ord(c)
            dp[i] = max(dp[i - k : i + k + 1]) + 1
        return max(dp)

    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        """
        2024-04-26
        1289. Minimum Falling Path Sum II
        https://leetcode.com/problems/minimum-falling-path-sum-ii/description/?envType=daily-question&envId=2024-04-26
        DP
        """
        n = len(grid)
        for i in range(1, n):
            # find two smallest from previous level
            r = heapq.nsmallest(2, grid[i - 1])
            for j in range(n):
                if grid[i - 1][j] == r[0]:
                    grid[i][j] += r[1]
                else:
                    grid[i][j] += r[0]
        return min(grid[-1])

    def findRotateSteps(self, ring: str, key: str) -> int:
        """
        2024-04-27
        514. Freedom Trail
        https://leetcode.com/problems/freedom-trail/description/?envType=daily-question&envId=2024-04-27
        DP
        """
        M, N = len(ring), len(key)

        def steps(i, k):
            x = abs(i - k)
            return min(
                x, M - x
            )  # ⭐️ minimum x steps to rotate the ring from i..k (🚫 without wrap-around, ✅ with wrap-around)

        pre = [0] * M  # 🤔 memo + 🛑 base case (ie. pre[0..M-1] = 0)
        j = N - 1
        while 0 <= j:  # key j
            cur = [float("inf")] * M
            for i in range(M):  # cur i
                for k in range(
                    M
                ):  # pre i (optimal k-th value is found as the recursive stack unwinds)
                    if ring[k] == key[j]:
                        cur[i] = min(
                            cur[i], 1 + steps(i, k) + pre[k]
                        )  # 🎯 min steps to reach key[j] from each ring[i] is the min steps to reach key[j + 1] from ring[k], 🔍 find optimal k via exhaustive search ('cur' denotes the current (j)th column and 'pre' denotes the previous (j+1)th column)
            pre = cur.copy()
            j -= 1
        return pre[
            0
        ]  # 🚀 when the ring starts at i = 0 (ie. index 0 is aligned with the 12:00 direction of the ring) return the min steps to construct key[j = N - 1..0]

    def sumOfDistancesInTree(self, N, edges):
        """
        2024-04-28
        834. Sum of Distances in Tree
        https://leetcode.com/problems/sum-of-distances-in-tree/description/?envType=daily-question&envId=2024-04-28
        """
        tree = defaultdict(set)
        res = [0] * N
        count = [1] * N
        for i, j in edges:
            tree[i].add(j)
            tree[j].add(i)

        def dfs(root, pre):
            for i in tree[root]:
                if i != pre:
                    dfs(i, root)
                    count[root] += count[i]
                    res[root] += res[i] + count[i]

        def dfs2(root, pre):
            for i in tree[root]:
                if i != pre:
                    res[i] = res[root] - count[i] + N - count[i]
                    dfs2(i, root)

        dfs(0, -1)
        dfs2(0, -1)
        return res

    def minOperations(self, nums: List[int], k: int) -> int:
        """
        2024-04-29
        2997. Minimum Number of Operations to Make Array XOR Equal to K
        https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/description/?envType=daily-question&envId=2024-04-29
        Count bits of XOR(nums) ^ k
        """
        return reduce(xor, nums, k).bit_count()

    def wonderfulSubstrings(self, word: str) -> int:
        """
        2024-04-30
        1915. Number of Wonderful Substrings
        https://leetcode.com/problems/number-of-wonderful-substrings/description/?envType=daily-question&envId=2024-04-30
        """
        count = [1] + [0] * 1024
        res = cur = 0
        base = ord("a")
        for c in word:
            cur ^= 1 << (ord(c) - base)
            res += count[cur]
            res += sum(count[cur ^ (1 << i)] for i in range(10))
            count[cur] += 1
        return res
