from bisect import bisect_right
import calendar
from collections import defaultdict
from typing import List


class Solution:
    """
    1184. Distance Between Bus Stops
        https://leetcode.com/problems/distance-between-bus-stops/description/
        https://leetcode.ca/2019-02-26-1184-Distance-Between-Bus-Stops/
        graph
    1185. Day of the Week
        https://leetcode.com/problems/day-of-the-week/description/
        https://leetcode.ca/2019-02-27-1185-Day-of-the-Week/
        ```c++
            class Solution {
            public:
                string dayOfTheWeek(int d, int m, int y) {
                    if (m < 3) {
                        m += 12;
                        y -= 1;
                    }
                    int c = y / 100;
                    y %= 100;
                    int w = (c / 4 - 2 * c + y + y / 4 + 13 * (m + 1) / 5 + d - 1) % 7;
                    vector<string> weeks = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};
                    return weeks[(w + 7) % 7];
                }
            };
        ```
    1186. Maximum Subarray Sum with One Deletion
        https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/description/
        https://leetcode.ca/2019-02-28-1186-Maximum-Subarray-Sum-with-One-Deletion/
    1187. Make Array Strictly Increasing
        https://leetcode.com/problems/make-array-strictly-increasing/description/
        https://leetcode.ca/2019-03-01-1187-Make-Array-Strictly-Increasing/
    """

    def distanceBetweenBusStops(
        self, distance: List[int], start: int, destination: int
    ) -> int:
        a = min(start, destination)
        b = max(start, destination)
        return min(sum(distance[a:b]), sum(distance) - sum(distance[a:b]))

    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        dayNumber = calendar.weekday(year, month, day)

        # Modify days list to start with Sunday as 0
        days = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]

        return days[dayNumber]

    def maximumSum(self, arr: List[int]) -> int:
        """
        pre_sum from left and right
        for each index its sum of left and right, find out which one might be the greatest
        """
        n = len(arr)
        left, right = [0] * n, [0] * n
        res = max(arr)
        s = 0
        for i, x in enumerate(arr):
            s = max(s, 0) + x
            left[i] = s
        s = 0
        for j in range(n - 1, -1, -1):
            s = max(s, 0) + arr[j]
            right[j] = s
        for i in range(1, n - 1):
            res = max(res, left[i - 1] + right[i + 1])
        return res

    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        dp = {-1: 0}
        arr2.sort()
        for i in arr1:
            tmp = defaultdict(lambda: float("inf"))
            for key in dp:
                if i > key:
                    tmp[i] = min(tmp[i], dp[key])
                loc = bisect_right(arr2, key)
                if loc < len(arr2):
                    tmp[arr2[loc]] = min(tmp[arr2[loc]], dp[key] + 1)
            dp = tmp
        if dp:
            return min(dp.values())
        return -1
