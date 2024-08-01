from collections import deque
from typing import List


class Solution:
    """
    2024.07.07
    3210. Find the Encrypted String
        https://leetcode.com/problems/find-the-encrypted-string/description/
    3211. Generate Binary Strings Without Adjacent Zeros
        https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/description/
    3212. Count Submatrices With Equal Frequency of X and Y
        https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/description/
    3213. Construct String with Minimum Cost
        https://leetcode.com/problems/construct-string-with-minimum-cost/description/
        https://leetcode.com/problems/construct-string-with-minimum-cost/solutions/5432354/python-trie-dp-solution/
    """

    def getEncryptedString(self, s: str, k: int) -> str:
        q = deque(list(s))
        q.rotate(-k)
        return "".join(q)

    def validStrings(self, n: int) -> List[str]:
        base = ["0", "1"]
        if n == 1:
            return base
        for _ in range(n - 1):
            new_ = []
            for s in base:
                if s[-1] == "1":
                    new_.append(s + "0")
                    new_.append(s + "1")
                else:
                    new_.append(s + "1")
            base = new_
        return base

    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        """
        X[i][j] means the count of X in first i rows, j cols
        X[i][j] = X[i-1][j] + X[i][j-1] - X[i-1][j-1] + (A[i][j] == "X")

        check if X[i][j] == Y[i][j] > 0, then increment result res.
        """
        m, n = len(grid), len(grid[0])
        X = [[0] * (n + 1) for _ in range(m + 1)]
        Y = [[0] * (n + 1) for _ in range(m + 1)]
        res = 0
        for i in range(m):
            for j in range(n):
                X[i][j] = (
                    X[i - 1][j] + X[i][j - 1] - X[i - 1][j - 1] + (grid[i][j] == "X")
                )
                Y[i][j] = (
                    Y[i - 1][j] + Y[i][j - 1] - Y[i - 1][j - 1] + (grid[i][j] == "Y")
                )
                if X[i][j] == Y[i][j] > 0:
                    res += 1
        return res

    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        n = len(target)

        trie = Trie()
        for word, cost in zip(words, costs):
            trie.insert(word, cost)

        dp = [10**10] * (n + 1)
        dp[0] = 0

        for i in range(n):
            if dp[i] >= 10**10:
                continue

            matches = trie.search(target, i)
            for idx, cost in matches:
                dp[idx] = min(dp[idx], dp[i] + cost)

        result = dp[n]
        return result if result < 10**10 else -1


class TrieNode:
    def __init__(self):
        self.children = {}
        self.cost = 10**10


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, cost):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.cost = min(cost, node.cost)

    def search(self, s, start):
        node = self.root
        matches = []
        for i in range(start, len(s)):
            if s[i] in node.children:
                node = node.children[s[i]]
                if node.cost < 10**10:
                    matches.append((i + 1, node.cost))
            else:
                break
        return matches


class AnotherSolution:
    def getEncryptedString(self, s: str, k: int) -> str:
        encrypted_string = ""
        n = len(s)
        for i in range(n):
            j = (i + k) % n
            encrypted_string += s[j]
        return encrypted_string

    def canBuild(self, target: str, words: List[str]) -> bool:
        ws = set(words)

        def dfs(target, ws):
            if not target:
                return True
            for w in ws:
                l = len(w)
                if target[: len(w)] == w:
                    ws.remove(w)
                    return dfs(target[l:], ws)
            return False

        return dfs(target, ws)


if __name__ == "__main__":
    s = Solution()
    # print(s.getEncryptedString("dart", 3))
    target = "abcdef"
    words = ["abdef", "abc", "de", "def", "ef"]
    ans = AnotherSolution()
    print(ans.canBuild(target, words))
