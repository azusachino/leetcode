from collections import Counter
from typing import List


class Solution:
    """
    1207. Unique Number of Occurrences
        https://leetcode.com/problems/unique-number-of-occurrences/description/
        array
    1208. Get Equal Substrings Within Budget
        https://leetcode.com/problems/get-equal-substrings-within-budget/
        string
    1209. Remove All Adjacent Duplicates in String II
        https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/description/
        stack
    1210. Minimum Moves to Reach Target with Rotations
        https://leetcode.com/problems/minimum-moves-to-reach-target-with-rotations/
    """

    def uniqueOccurrences(self, arr: List[int]) -> bool:
        v = Counter(arr).values()
        return len(set(v)) == len(v)

    def equalSubstring(self, s: str, t: str, cost: int) -> int:
        i = 0
        n = len(s)
        for j in range(n):
            cost -= abs(ord(s[j]) - ord(t[j]))
            if cost < 0:
                cost += abs(ord(s[i]) - ord(t[i]))
                i += 1
        return j - i + 1

    def removeDuplicates(self, s: str, k: int) -> str:
        # char, count
        st = [["#", 0]]
        for c in s:
            if st[-1][0] == c:
                st[-1][1] += 1
                if st[-1][1] == k:
                    st.pop()
            else:
                st.append([c, 1])

        return "".join(c * k for c, k in st)

    def minimumMoves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        start = (0, 0, 0, 1)
        end = (n - 1, n - 2, n - 1, n - 1)
        curr_level = {start}
        moves = 0
        visited = set()
        while curr_level:
            if end in curr_level:
                return moves
            next_level = set()
            for pos in curr_level:
                visited.add(pos)
                r1, c1, r2, c2 = pos
                if (
                    c1 + 1 < n
                    and grid[r1][c1 + 1] == 0
                    and c2 + 1 < n
                    and grid[r2][c2 + 1] == 0
                ):
                    if (r1, c1 + 1, r2, c2 + 1) not in visited:
                        next_level.add((r1, c1 + 1, r2, c2 + 1))
                if (
                    r1 + 1 < n
                    and grid[r1 + 1][c1] == 0
                    and r2 + 1 < n
                    and grid[r2 + 1][c2] == 0
                ):
                    if (r1 + 1, c1, r2 + 1, c1) not in visited:
                        next_level.add((r1 + 1, c1, r2 + 1, c2))
                if (
                    r1 == r2
                    and c2 == c1 + 1
                    and r1 + 1 < n
                    and grid[r1 + 1][c1] + grid[r1 + 1][c1 + 1] == 0
                ):
                    if (r1, c1, r1 + 1, c1) not in visited:
                        next_level.add((r1, c1, r1 + 1, c1))
                if (
                    c1 == c2
                    and r2 == r1 + 1
                    and c1 + 1 < n
                    and grid[r1][c1 + 1] + grid[r1 + 1][c1 + 1] == 0
                ):
                    if (r1, c1, r1, c1 + 1) not in visited:
                        next_level.add((r1, c1, r1, c1 + 1))
            curr_level = next_level
            moves += 1
        return -1
