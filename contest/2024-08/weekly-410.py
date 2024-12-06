from collections import defaultdict
from typing import List


class Solution:
    """
    08.11
    3248. Snake in Matrix
        https://leetcode.com/problems/snake-in-matrix/description/
    3249. Count the Number of Good Nodes
        https://leetcode.com/problems/count-the-number-of-good-nodes/description/
    3250. Find the Count of Monotonic Pairs I
        https://leetcode.com/problems/find-the-count-of-monotonic-pairs-i/
    3251. Find the Count of Monotonic Pairs I
        https://leetcode.com/problems/find-the-count-of-monotonic-pairs-ii/
    """

    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        dirs = {"UP": [0, -1], "RIGHT": [1, 0], "DOWN": [0, 1], "LEFT": [-1, 0]}
        x = y = 0
        for cmd in commands:
            dx, dy = dirs[cmd]
            x += dx
            y += dy
        return x + y * n

    def countGoodNodes(self, edges: List[List[int]]) -> int:
        tree = defaultdict(list)
        for x, y in edges:
            tree[x].append(y)
            tree[y].append(x)

        def dfs(node, parent):
            cur_size = 1
            child_sizes = []
            for i in tree[node]:
                if i == parent:
                    continue
                size = dfs(i, node)
                cur_size += size
                child_sizes.append(size)
            # multi-child tree
            if len(set(child_sizes)) <= 1:
                self.good_nodes += 1
            return cur_size

        self.good_nodes = 0
        dfs(0, -1)
        return self.good_nodes

    def countOfPairs(self, A: List[int]) -> int:
        # @credit https://leetcode.com/problems/find-the-count-of-monotonic-pairs-i/solutions/5619383/java-c-python-1d-dp-o-n-space/
        mod = 10**9 + 7
        n, m = len(A), max(A) + 1
        dp, dp2 = [1] * m, [0] * m
        for i in range(1, n):
            d = max(0, A[i] - A[i - 1])
            for j in range(d, A[i] + 1):
                dp2[j] = (dp2[j - 1] + dp[j - d]) % mod
            dp, dp2 = dp2, [0] * m
        return sum(dp) % mod
