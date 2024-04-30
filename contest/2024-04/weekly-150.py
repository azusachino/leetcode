from collections import deque
import sys
from typing import Counter, List, Optional

from tree.local_tree import TreeNode


class Solution:
    """
    1160. Find Words That Can Be Formed by Characters
        https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/
        String, Mapping
    1161. Maximum Level Sum of a Binary Tree
        https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/
        Tree, BFS
    1162. As Far from Land as Possible
        https://leetcode.com/problems/as-far-from-land-as-possible/description/
        Graph
    1163. Last Substring in Lexicographical Order
        https://leetcode.com/problems/last-substring-in-lexicographical-order/
        https://leetcode.ca/2019-02-05-1163-Last-Substring-in-Lexicographical-Order/
        String
    """

    def countCharacters(self, words: List[str], chars: str) -> int:
        cnt = Counter(chars)
        ans = 0
        for w in words:
            wc = Counter(w)
            if all(cnt[c] >= v for c, v in wc.items()):
                ans += len(w)
        return ans

    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        mx = -sys.maxsize
        i = 0
        while q:
            i += 1
            s = 0
            for _ in range(len(q)):
                node = q.popleft()
                s += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if mx < s:
                mx = s
                ans = i
        return ans

    def maxDistance(self, grid: List[List[int]]) -> int:
        """
        We can add all land cells to the queue q.
        If the queue is empty, or the number of elements in the queue equals the number of cells in the grid, it means that the grid contains only land or ocean, so return -1.

        Otherwise, we start BFS from the land cells. Define the initial step count res = -1;

        In each round of search, we spread all cells in the queue in four directions. If a cell is an ocean cell, we mark it as a land cell and add it to the queue. After a round of spreading, we increase the step count by 1.
        Repeat this process until the queue is empty.

        Finally, we return the step count res.
        """
        n = len(grid)
        q = deque((i, j) for i in range(n) for j in range(n) if grid[i][j])
        res = -1
        # no island or all island
        if len(q) in (0, n**2):
            return res
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                for di, dj in dirs:
                    x, y = i + di, j + dj
                    # island fill
                    if 0 <= x < n and 0 <= y < n and grid[x][y] == 0:
                        grid[x][y] = 1
                        q.append((x, y))
            res += 1
        return res

    def lastSubstring(self, s: str) -> str:
        """
        don't understand
        """
        i, j, k = 0, 1, 0
        while j + k < len(s):
            if s[i + k] == s[j + k]:
                k += 1
            elif s[i + k] < s[j + k]:
                i += k + 1
                k = 0
                if i >= j:
                    j = i + 1
            else:
                j += k + 1
                k = 0
        return s[i:]
