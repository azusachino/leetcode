from bisect import bisect_left, bisect_right
from collections import defaultdict
from typing import Counter, List


class Solution:
    """
    1150. check if a number is majority element in a sorted array
    1151. Minimun swaps to group all 1's together
    1152. Analyze user website visit pattern
    1153. string transforms to another string
    """

    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        left = bisect_left(nums, target)
        right = bisect_right(nums, target)
        return right - left > len(nums) // 2

    def minSwaps(self, data: List[int]) -> int:
        """
        First, we count the number of 1s in the array, denoted as k.
        Then we use a sliding window of size k, moving the right boundary of the window from left to right, and count the number of 1s in the window, denoted as t.
        Each time we move the window, we update the value of t.
        Finally, when the right boundary of the window moves to the end of the array, the number of 1s in the window is the maximum, denoted as mx.
        The final answer is k-mx.
        """
        k = data.count(1)
        t = sum(data[:k])
        mx = t
        for i in range(k, len(data)):
            t += data[i]
            t -= data[i - k]
            mx = max(mx, t)
        return k - mx

    def mostVisitedPattern(
        self, username: List[str], timestamp: List[int], website: List[str]
    ) -> List[str]:
        d = defaultdict(list)
        for user, _, site in sorted(
            zip(username, timestamp, website), key=lambda x: x[1]
        ):
            d[user].append(site)

        cnt = Counter()
        for sites in d.values():
            m = len(sites)
            s = set()
            if m > 2:
                for i in range(m - 2):
                    for j in range(i + 1, m - 1):
                        for k in range(j + 1, m):
                            s.add((sites[i], sites[j], sites[k]))
            for t in s:
                cnt[t] += 1
        return sorted(cnt.items(), key=lambda x: (-x[1], x[0]))[0][0]

    def canConvert(self, str1: str, str2: str) -> bool:
        """
        First, we can check if str1 and str2 are equal. If they are, return true directly.

        Then we count the occurrence of each letter in str2. If the occurrence equals 26, it means str2 contains all lowercase letters. In this case, no matter how str1 is transformed, it cannot become str2, so return false directly.

        Otherwise, we use an array or hash table d to record the letter each letter in str1 is transformed to. We traverse the strings str1 and str2. If a letter in str1 has been transformed, the transformed letter must be the same as the corresponding letter in str2, otherwise return false.

        After the traversal, return true.
        """
        if str1 == str2:
            return True
        if len(set(str2)) == 26:
            return False
        d = {}
        for a, b in zip(str1, str2):
            if a not in d:
                d[a] = b
            elif d[a] != b:
                return False
        return True
