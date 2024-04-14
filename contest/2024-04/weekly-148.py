import bisect
import sys
from typing import List


class Solution:
    """
    1144. Decrease Elements To Make Array Zigzag
        https://leetcode.com/problems/decrease-elements-to-make-array-zigzag/solutions/350576/java-c-python-easy-and-concise/
    1145. Binary Tree Coloring Game
    1146. Snapshot Array
    1147. Longest Chunked Palindrome Decomposition
    """

    def movesToMakeZigzag(self, nums: List[int]) -> int:
        """
        Two options, either make A[even] smaller or make A[odd] smaller.
        """
        nums = [sys.maxsize] + nums + [sys.maxsize]
        res = [0, 0]
        for i in range(1, len(nums) - 1):
            res[i % 2] += max(0, nums[i] - min(nums[i - 1], nums[i + 1]) + 1)
        return min(res)


class SnapshotArray_:

    def __init__(self, length: int):
        self.length = length
        self.data = [0] * self.length
        self.snaps = []

    def set(self, index: int, val: int) -> None:
        self.data[index] = val

    def snap(self) -> int:
        self.snaps.append(self.data[:])
        self.data = [0] * self.length
        return len(self.snaps) - 1

    def get(self, index: int, snap_id: int) -> int:
        return self.snaps[snap_id][index]


class SnapshotArray(object):

    def __init__(self, n):
        self.A = [[[-1, 0]] for _ in range(n)]
        self.snap_id = 0

    def set(self, index, val):
        self.A[index].append([self.snap_id, val])

    def snap(self):
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index, snap_id):
        i = bisect.bisect(self.A[index], [snap_id + 1]) - 1
        return self.A[index][i][1]
