from itertools import groupby
from typing import List
from uf import UF


class Solution:
    def findAllPeople(
        self, n: int, meetings: List[List[int]], firstPerson: int
    ) -> List[int]:
        uf = UF(n)
        uf.union(0, firstPerson)
        for _, grp in groupby(sorted(meetings, key=lambda x: x[2]), key=lambda x: x[2]):
            seen = set()
            for x, y, _ in grp:
                seen.add(x)
                seen.add(y)
                uf.union(x, y)
            for x in seen:
                if uf.find(x) != uf.find(0):
                    uf.parent[x] = x

        return [x for x in range(n) if uf.find(x) == uf.find(0)]

    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        max_num, n = max(nums), len(nums)
        arr = [-1] * (1 + max_num)
        uf = UF(n)

        for i, x in enumerate(nums):
            for p in range(2, x):
                if p**2 > x:
                    break
                if x % p != 0:
                    continue
                if arr[p] != -1:
                    uf.union(arr[p], i)
                else:
                    arr[p] = i
                while x % p == 0:
                    x //= p
            if x > 1:
                if arr[x] != -1:
                    uf.union(arr[x], i)
                else:
                    arr[x] = i
        return uf.count() == 1


if __name__ == "__main__":
    s = Solution()
    nums = [4, 3, 12, 8]
    r = s.canTraverseAllPairs(nums)
    print("canTraverseAllPairs", r)
