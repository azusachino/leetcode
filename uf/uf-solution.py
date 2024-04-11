from itertools import groupby
from typing import List


class UF:
    def __init__(self, n):
        self.data = list(range(n))
        self.rank = [1] * n
        self.cnt = n

    def find(self, x):
        if self.data[x] != x:
            self.data[x] = self.find(self.data[x])
        return self.data[x]

    def union(self, x, y):
        i, j = self.find(x), self.find(y)
        if i == j:
            return
        if self.rank[i] >= self.rank[j]:
            self.data[j] = i
            self.rank[i] += self.rank[j]
        else:
            self.data[i] = j
            self.rank[j] += self.rank[i]
        self.cnt -= 1

    def count(self):
        return self.cnt


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

    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort()
        uf = UF(n)
        for t, x, y in logs:
            uf.union(x, y)
            if uf.count() == 1:
                return t
        return -1


if __name__ == "__main__":
    s = Solution()
    nums = [4, 3, 12, 8]
    r = s.canTraverseAllPairs(nums)
    print("canTraverseAllPairs", r)
    logs = [
        [20190101, 0, 1],
        [20190104, 3, 4],
        [20190107, 2, 3],
        [20190211, 1, 5],
        [20190224, 2, 4],
        [20190301, 0, 3],
        [20190312, 1, 2],
        [20190322, 4, 5],
    ]
    print(s.earliestAcq(logs, 6))
