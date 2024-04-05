from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def dfs(i, j, target) -> bool:
            # find all character
            if len(target) == 0:
                return True
            # out of bound
            if i < 0 or i >= m or j < 0 or j >= n or word[0] != board[i][j]:
                return False
            cur = board[i][j]
            # visited
            board[i][j] = "#"
            word = word[1:]
            # four direction iteration
            res = (
                dfs(i + 1, j, word)
                or dfs(i - 1, j, word)
                or dfs(i, j + 1, word)
                or dfs(i, j - 1, word)
            )
            # reset path
            board[i][j] = cur
            return res

        for i in range(m):
            for j in range(n):
                if dfs(i, j, word):
                    return True
        return False
