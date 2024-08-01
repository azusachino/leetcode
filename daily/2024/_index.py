from collections import Counter, defaultdict
import heapq
from typing import List


class Solution:
    def minDeletions(self, s: str) -> int:
        cnt = Counter(s)
        used = set()
        res = 0
        for _, v in cnt.items():
            while v > 0 and v in used:
                v -= 1
                res += 1
            used.add(v)
        return res


if __name__ == "__main__":
    solution = Solution()
    heights = [4, 2, 7, 6, 9, 14, 12]
    bricks = 5
    ladders = 1
    print(solution.furthestBuilding(heights, bricks, ladders))
