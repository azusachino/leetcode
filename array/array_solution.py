import collections
import math
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
        ret = [-1] * n
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                ret[p] = nums[l] ** 2
                l += 1
            else:
                ret[p] = nums[r] ** 2
                r -= 1
            p -= 1
        return ret

    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        l, r = 0, len(tokens) - 1
        result = 0
        score = 0
        while l <= r:
            if power >= tokens[l]:
                power -= tokens[l]
                score += 1
                l += 1
            else:
                if score:
                    power += tokens[r]
                    score -= 1
                    r -= 1
                else:
                    break
            result = max(result, score)
        return result

    def minimumLength(self, s: str) -> int:
        sz = len(s)
        arr = list(s)
        l, r = 0, sz - 1
        # in case of aa, l & r will switch index
        while l < r and arr[l] == arr[r]:
            ch = arr[l]
            while l <= r and ch == arr[l]:
                l += 1
            while l < r and ch == arr[r]:
                r -= 1
        return r - l + 1

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        l = 0
        r = l + 1
        ret = 0
        while r < n:
            cur = prices[r] - prices[l]
            if cur > 0:
                ret = max(ret, cur)
            else:
                l = r
            r += 1
        return ret

    def maxFrequencyElements(self, nums: List[int]) -> int:
        d = collections.defaultdict(int)
        for n in nums:
            d[n] += 1
        max_freq = 0
        for v in d.values():
            max_freq = max(max_freq, v)
        max_freq_count = 0
        for v in d.values():
            if v == max_freq:
                max_freq_count += 1
        return max_freq_count * max_freq

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(set(nums2)))

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        c = collections.Counter({0: 1})
        psum = res = 0
        for i in nums:
            psum += i
            res += c[psum - goal]
            c[psum] += 1
        return res

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ret = [0] * n
        pre = [1 for _ in range(n)]
        suffix = [1] * n
        for i in range(1, n):
            pre[i] = pre[i - 1] * nums[i - 1]

        for j in range(n - 2, -1, -1):
            suffix[j] = suffix[j + 1] * nums[j + 1]

        for i in range(n):
            ret[i] = pre[i] * suffix[i]

        return ret

    def findMaxLength(self, nums: List[int]) -> int:
        """
        public class Solution {
            public int findMaxLength(int[] nums) {
                for (int i = 0; i < nums.length; i++) {
                    if (nums[i] == 0) nums[i] = -1;
                }

                Map<Integer, Integer> sumToIndex = new HashMap<>();
                sumToIndex.put(0, -1);
                int sum = 0, max = 0;

                for (int i = 0; i < nums.length; i++) {
                    sum += nums[i];
                    if (sumToIndex.containsKey(sum)) {
                        max = Math.max(max, i - sumToIndex.get(sum));
                    }
                    else {
                        sumToIndex.put(sum, i);
                    }
                }

                return max;
            }
        }
        """
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                nums[i] = -1
        sum_to_index = {0: -1}
        sum_ = max_ = 0
        for i in range(n):
            sum_ += nums[i]
            if sum_ in sum_to_index:
                max_ = max(max_, i - sum_to_index[sum_])
            else:
                sum_to_index[sum_] = i
        return max_

    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        ret = []
        i = 0
        n = len(intervals)
        while i < n and intervals[i][1] < newInterval[0]:
            ret.append(intervals[i])
            i += 1
        while i < n and intervals[i][0] < newInterval[1]:
            newInterval = [
                min(newInterval[0], intervals[i][0]),
                max(newInterval[1], intervals[i][1]),
            ]
            i += 1
        ret.append(newInterval)
        while i < n:
            ret.append(intervals[i])
            i += 1
        return ret

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda x: x[1])
        max_ = points[0][1]
        cnt = 1
        for point in points:
            # merge interval
            if point[0] > max_:
                cnt += 1
                max_ = point[1]
        return cnt


if __name__ == "__main__":
    solution = Solution()
    # n = 3
    # trust = [[1, 3], [2, 3]]
    # r = s.findJudge(n, trust)
    # print("findJudge: ", r)
    # tokens = [10, 33, 41, 91, 47, 84, 98, 34, 48, 70]
    # power = 43
    # r = s.bagOfTokensScore(tokens, power)
    # print("bagOfTokensScore", r)
    # s = "bbbbbbbbbbbbbbbbbbbbbbbbbbbabbbbbbbbbbbbbbbccbcbcbccbbabbb"
    # r = solution.minimumLength(s)
    # print("minimumLength", r)
    # nums = [10, 12, 11, 9, 6, 19, 11]
    # print(solution.maxFrequencyElements(nums))
    # nums = [1, 0, 1, 0, 1]
    # print(solution.numSubarraysWithSum(nums, 2))
    points = [[1, 2], [3, 4], [5, 6], [7, 8]]
    print(solution.findMinArrowShots(points))
