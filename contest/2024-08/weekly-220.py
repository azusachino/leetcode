from collections import deque
from typing import List


class Solution:
    """
    1694. Reformat Phone Number
        https://leetcode.com/problems/reformat-phone-number/description/
    1695. Maximum Erasure Value
        https://leetcode.com/problems/maximum-erasure-value/
    1696. Jump Game VI
        https://leetcode.com/problems/jump-game-vi/description/
    1697. Checking Existence of Edge Length Limited Paths
        https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/description/
    """

    def reformatNumber(self, number: str) -> str:
        number = number.replace("-", "").replace(" ", "")  # removing - and space
        ans = []
        for i in range(0, len(number), 3):
            if len(number) - i != 4:
                ans.append(number[i : i + 3])
            else:
                ans.extend([number[i : i + 2], number[i + 2 :]])
                break
        return "-".join(ans)

    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res = 0
        l = r = 0
        n = len(nums)
        st = set()
        cur = 0
        while r < n:
            rn = nums[r]
            while rn in st and l < n:
                ln = nums[l]
                if ln in st:
                    st.remove(ln)
                cur -= ln
                l += 1
            st.add(rn)
            cur += rn
            res = max(res, cur)
            r += 1
        return res

    def maxResult(self, nums: List[int], k: int) -> int:
        # @credit https://leetcode.ca/2020-07-22-1696-Jump-Game-VI/
        n = len(nums)
        f = [0] * n
        q = deque([0])
        for i in range(n):
            if i - q[0] > k:
                q.popleft()
            f[i] = nums[i] + f[q[0]]
            while q and f[q[-1]] <= f[i]:
                q.pop()
            q.append(i)
        return f[-1]

    def distanceLimitedPathsExist(
        self, n: int, edgeList: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        # @credit https://leetcode.ca/2020-07-23-1697-Checking-Existence-of-Edge-Length-Limited-Paths/
        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        p = list(range(n))
        edgeList.sort(key=lambda x: x[2])
        j = 0
        ans = [False] * len(queries)
        for i, (a, b, limit) in sorted(enumerate(queries), key=lambda x: x[1][2]):
            while j < len(edgeList) and edgeList[j][2] < limit:
                u, v, _ = edgeList[j]
                p[find(u)] = find(v)
                j += 1
            ans[i] = find(a) == find(b)
        return ans