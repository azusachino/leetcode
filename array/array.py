from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        count = [0] * (n + 1)
        for i, j in trust:
            count[i] -= 1
            count[j] += 1
        for i in range(1, n + 1):
            if count[i] == n - 1:
                return i
        return -1

    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l, r = 0, n - 1
        p = n - 1
        ret = [-1]*n
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                ret[p] = nums[l] ** 2
                l += 1
            else:
                ret[p] = nums[r] ** 2
                r -= 1
            p -= 1
        return ret


if __name__ == "__main__":
    s = Solution()
    n = 3
    trust = [[1, 3], [2, 3]]
    r = s.findJudge(n, trust)
    print("findJudge: ", r)
