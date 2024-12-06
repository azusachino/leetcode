from heapq import heappop, heappush
import sys
import bisect
import collections
from functools import reduce
from itertools import accumulate, chain, groupby
import math
from operator import ixor
from typing import List


class Solution:
    def makeFancyString(self, s: str) -> str:
        """
        11.01
        1957. Delete Characters to Make Fancy String
        https://leetcode.com/problems/delete-characters-to-make-fancy-string/?envType=daily-question&envId=2024-11-01
        """
        st = []
        for c in s:
            if not st or st[-1] != c:
                st.append(c)
            # st[-1] == c
            else:
                if len(st) >= 2 and st[-2] == c:
                    continue
                else:
                    st.append(c)
        return "".join(st)

    def isCircularSentence(self, s: str) -> bool:
        """
        11.02
        2490. Circular Sentence
        https://leetcode.com/problems/circular-sentence/?envType=daily-question&envId=2024-11-02
        """
        stk = []
        arr = s.split(" ")
        for c in arr:
            if stk and c[0] != stk[-1][-1]:
                return False
            stk.append(c)
        return stk[0][0] == stk[-1][-1]

    def rotateString(self, s: str, goal: str) -> bool:
        """
        11.03
        796. Rotate String
        https://leetcode.com/problems/rotate-string/?envType=daily-question&envId=2024-11-03
        """
        if len(s) != len(goal):
            return False
        return goal in (s + s)

    def compressedString(self, word: str) -> str:
        """
        11.04
        3163. String Compression III
        https://leetcode.com/problems/string-compression-iii/?envType=daily-question&envId=2024-11-04
        """
        cur = ""
        curc = 0
        res = ""
        for c in word:
            if cur != c:
                if curc:
                    res += str(curc) + cur
                cur = c
                curc = 1
            else:
                curc += 1
                if curc > 9:
                    res += "9" + cur
                    curc = 1
        if curc:
            res += str(curc) + cur
        return res

    def minChanges(self, s: str) -> int:
        """
        11.05
        2914. Minimum Number of Changes to Make Binary String Beautiful
        https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/?envType=daily-question&envId=2024-11-05
        """
        count = 0
        i = 0
        while i < len(s) - 1:
            if s[i] != s[i + 1]:
                count += 1
            i += 2
        return count

    def canSortArray(self, nums: List[int]) -> bool:
        """
        11.06
        3011. Find If Array Can Be Sorted
        https://leetcode.com/problems/find-if-array-can-be-sorted/?envType=daily-question&envId=2024-11-06
        """
        return list(
            chain.from_iterable(sorted(g) for _, g in groupby(nums, key=int.bit_count))
        ) == sorted(nums)

    def largestCombination(self, candidates: List[int]) -> int:
        """
        11.07
        2275. Largest Combination With Bitwise AND Greater Than Zero
        https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/?envType=daily-question&envId=2024-11-07
        """
        cnt = [0] * 32
        for c in candidates:
            for i in range(32):
                cnt[i] += (c >> i) & 1
                if c >> i == 0:
                    break
        return max(cnt)

    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        """
        11.08
        1829. Maximum XOR for Each Query
        https://leetcode.com/problems/maximum-xor-for-each-query/?envType=daily-question&envId=2024-11-08
        !! Note that the maximum possible XOR result is always 2^(maximumBit) - 1
        """
        maxXOR, arrayXOR, ans = (1 << maximumBit) - 1, reduce(ixor, nums), []
        for i in range(len(nums) - 1, -1, -1):
            ans.append(arrayXOR ^ maxXOR)
            arrayXOR ^= nums[i]
        return ans

    def minEnd(self, n: int, x: int) -> int:
        """
        11.09
        3133. Minimum Array End
        https://leetcode.com/problems/minimum-array-end/?envType=daily-question&envId=2024-11-09
        """
        n -= 1
        b = 1
        for i in range(64):
            if b & x == 0:
                x |= (n & 1) * b
                n >>= 1
            b <<= 1
        return x

    def update(self, bits: List[int], x: int, change: int):
        # insert or remove element from window, time: O(32)
        for i in range(32):
            if (x >> i) & 1:
                bits[i] += change

    def bitsToNum(self, bits: List[int]) -> int:
        # convert 32-size bits array to integer, time: O(32)
        result = 0
        for i in range(32):
            if bits[i]:
                result |= 1 << i
        return result

    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        """
        11.10
        3097. Shortest Subarray With OR at Least K II
        https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-ii/?envType=daily-question&envId=2024-11-10
        """
        n = len(nums)
        result = n + 1
        bits = [0] * 32
        start = 0
        for end in range(n):
            self.update(bits, nums[end], 1)  # insert nums[end] into window
            while start <= end and self.bitsToNum(bits) >= k:
                result = min(result, end - start + 1)
                self.update(bits, nums[start], -1)  # remove nums[start] from window
                start += 1
        return result if result != n + 1 else -1

    def primeSubOperation(self, A: List[int]) -> bool:
        """
        11.11
        2601. Prime Subtraction Operation
        https://leetcode.com/problems/prime-subtraction-operation/?envType=daily-question&envId=2024-11-11
        """
        for i in range(len(A) - 2, -1, -1):
            if A[i] < A[i + 1]:
                continue
            index = bisect.bisect_right(primes, A[i] - A[i + 1])
            if index == len(primes) or A[i] - primes[index] < 1:
                return False
            A[i] -= primes[index]
        return True

    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        """
        11.12
        2070. Most Beautiful Item for Each Query
        https://leetcode.com/problems/most-beautiful-item-for-each-query/?envType=daily-question&envId=2024-11-12
        class Solution {
            public int[] maximumBeauty(int[][] items, int[] queries) {
                int[] result = new int[queries.length];
                Arrays.sort(items, (a, b) -> (a[0] - b[0]));

                var map = new TreeMap<Integer, Integer>();

                // init base case
                map.put(0, 0);

                int currMax = 0;
                for (int[] item : items) {
                    currMax = Math.max(currMax, item[1]); // maintain largerst beauty so far
                    map.put(item[0], currMax); // store in treeMap
                }

                for (int i = 0; i < queries.length; ++i) {
                    result[i] = map.floorEntry(queries[i]).getValue();
                }

                return result;
            }
        }
        """
        pass

    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        """
        11.13
        2563. Count the Number of Fair Pairs
        https://leetcode.com/problems/count-the-number-of-fair-pairs/?envType=daily-question&envId=2024-11-13
        """
        nums.sort()
        res = 0
        n = len(nums)
        for i in range(n):
            l = bisect.bisect_left(nums, lower - nums[i], lo=i + 1, hi=n)
            r = bisect.bisect_right(nums, upper - nums[i], lo=i + 1, hi=n)
            res += r - l
        return res

    def minimizedMaximum(self, n, A):
        """
        11.14
        2064. Minimized Maximum of Products Distributed to Any Store
        https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/?envType=daily-question&envId=2024-11-14
        """
        left, right = 1, max(A)
        while left < right:
            x = (left + right) // 2
            if sum(math.ceil(a / x) for a in A) > n:
                left = x + 1
            else:
                right = x
        return left

    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        """
        11.15
        1574. Shortest Subarray to be Removed to Make Array Sorted
        https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/?envType=daily-question&envId=2024-11-15
        """
        n = len(arr)
        left, right = 0, n - 1
        while left < n - 1 and arr[left] <= arr[left + 1]:
            left += 1
        if left == n - 1:
            return 0
        while right > 0 and arr[right] >= arr[right - 1]:
            right -= 1
        result = min(n - left - 1, right)
        for i in range(left + 1):
            if arr[i] <= arr[right]:
                result = min(result, right - i - 1)
            elif right < n - 1:
                right += 1
            else:
                break
        return result

    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        """
        11.16
        3254. Find the Power of K-Size Subarrays I
        https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/?envType=daily-question&envId=2024-11-16
        """
        if k == 1:
            return nums
        n = len(nums)
        res = [-1] * (n - k + 1)
        cc = 1
        for i in range(n - 1):
            if nums[i] + 1 == nums[i + 1]:
                cc += 1
            else:
                cc = 1
            if cc >= k:
                res[i - k + 2] = nums[i + 1]
        return res

    def shortestSubarray(self, A, K):
        """
        11.17
        862. Shortest Subarray with Sum at Least K
        https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/?envType=daily-question&envId=2024-11-17
        """
        d = collections.deque([[0, 0]])
        res, cur = float("inf"), 0
        for i, a in enumerate(A):
            cur += a
            while d and cur - d[0][1] >= K:
                res = min(res, i + 1 - d.popleft()[0])
            while d and cur <= d[-1][1]:
                d.pop()
            d.append([i + 1, cur])
        return res if res < float("inf") else -1

    def decrypt(self, code: List[int], k: int) -> List[int]:
        """
        11.18
        1652. Defuse the Bomb
        https://leetcode.com/problems/defuse-the-bomb/?envType=daily-question&envId=2024-11-18
        """
        n, code = len(code), list(accumulate(code + code))
        if k < 0:
            return [code[i] - code[i + k] for i in range(n - 1, 2 * n - 1)]
        if k > 0:
            return [code[i + k] - code[i] for i in range(n)]
        return [0] * n

    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        """
        11.19
        2461. Maximum Sum of Distinct Subarrays With Length K
        https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/?envType=daily-question&envId=2024-11-19
        """
        res = 0
        cnt = collections.Counter()
        cur = 0
        l = r = 0
        n = len(nums)
        while r < n:
            rv = nums[r]
            cnt[rv] += 1
            cur += rv
            r += 1
            if r - l >= k:
                if len(cnt) == k:
                    res = max(res, cur)
                lv = nums[l]
                if lv in cnt:
                    cnt[lv] -= 1
                    if cnt[lv] == 0:
                        del cnt[lv]
                cur -= lv
                l += 1
        return res

    def takeCharacters(self, s: str, k: int) -> int:
        """
        11.20
        2516. Take K of Each Character From Left and Right
        https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/?envType=daily-question&envId=2024-11-20
        idea. convert least problem to maximum problem
        eg. to find at least k of each character, we need to find the maximum substring (window) that contains at most Cnt[ch] - k characters
        """
        n = len(s)
        limitMap = collections.Counter(s)
        for ch in "abc":
            if limitMap[ch] < k:
                return -1
            limitMap[ch] -= k

        currCntMap = collections.defaultdict(int)
        res = 0
        l = 0
        for r in range(n):
            currCntMap[s[r]] += 1
            while currCntMap[s[r]] > limitMap[s[r]]:
                currCntMap[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return n - res

    def countUnguarded(
        self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]
    ) -> int:
        """
        11.21
        2257. Count Unguarded Cells in the Grid
        https://leetcode.com/problems/count-unguarded-cells-in-the-grid/?envType=daily-question&envId=2024-11-21
        """
        dp = [[0] * n for _ in range(m)]
        for x, y in guards + walls:
            dp[x][y] = 1
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        for x, y in guards:
            for dx, dy in directions:
                curr_x = x
                curr_y = y

                while (
                    0 <= curr_x + dx < m
                    and 0 <= curr_y + dy < n
                    # reached wall
                    and dp[curr_x + dx][curr_y + dy] != 1
                ):
                    curr_x += dx
                    curr_y += dy
                    dp[curr_x][curr_y] = 2

        return sum(1 for i in range(m) for j in range(n) if dp[i][j] == 0)

    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        """
        11.22
        1072. Flip Columns For Maximum Number of Equal Rows
        https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/?envType=daily-question&envId=2024-11-22
        """
        # tuple is just to make this combination hashable in dictionary
        return max(
            collections.Counter(tuple(x ^ r[0] for x in r) for r in matrix).values()
        )

    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        """
        11.23
        1861. Rotating the Box
        https://leetcode.com/problems/rotating-the-box/?envType=daily-question&envId=2024-11-23
        """
        m, n = len(box), len(box[0])

        ans = [["."] * m for _ in range(n)]

        for i, row in enumerate(box):
            num_spaces = 0
            for j in range(n - 1, -1, -1):
                # reset while encountering a obstacle
                if row[j] == "*":
                    num_spaces = 0
                    ans[j][m - i - 1] = "*"
                elif row[j] == ".":
                    num_spaces += 1
                elif row[j] == "#":
                    ans[j + num_spaces][m - i - 1] = "#"

        return ans

    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        """
        11.24
        1975. Maximum Matrix Sum
        https://leetcode.com/problems/maximum-matrix-sum/?envType=daily-question&envId=2024-11-24
        """
        arr = [num for row in matrix for num in row]
        abs_total = sum(map(abs, arr))
        neg = sum([num < 0 for num in arr])
        mi = min(map(abs, arr))
        return abs_total if neg % 2 == 0 else abs_total - 2 * mi

    def slidingPuzzle(self, board: List[List[int]]) -> int:
        """
        11.25
        773. Sliding Puzzle
        https://leetcode.com/problems/sliding-puzzle/?envType=daily-question&envId=2024-11-25
        """
        s = "".join(str(d) for row in board for d in row)
        dq, seen = collections.deque(), {s}
        dq.append((s, s.index("0")))
        steps, height, width = 0, len(board), len(board[0])
        while dq:
            for _ in range(len(dq)):
                t, i = dq.popleft()
                if t == "123450":
                    return steps
                x, y = i // width, i % width
                for r, c in (x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y):
                    if height > r >= 0 <= c < width:
                        ch = [d for d in t]
                        ch[i], ch[r * width + c] = (
                            ch[r * width + c],
                            "0",
                        )  # swap '0' and its neighbor.
                        s = "".join(ch)
                        if s not in seen:
                            seen.add(s)
                            dq.append((s, r * width + c))
            steps += 1
        return -1

    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        """
        11.26
        2924. Find Champion II
        https://leetcode.com/problems/find-champion-ii/description/?envType=daily-question&envId=2024-11-26
        """
        weak = {b for _, b in edges}
        return -1 if len(weak) < n - 1 else n * (n - 1) // 2 - sum(weak)

    def shortestDistanceAfterQueries(
        self, n: int, queries: List[List[int]]
    ) -> List[int]:
        """
        11.27
        3243. Shortest Distance After Road Addition Queries I
        https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i/description/?envType=daily-question&envId=2024-11-27
        """

        def bfs(graph, n: int) -> int:
            q = collections.deque([0])
            dist = [sys.maxsize] * n
            dist[0] = 0
            visited = set([0])

            while q:
                node = q.popleft()
                if node == n - 1:
                    return dist[node]
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        dist[neighbor] = dist[node] + 1
                        q.append(neighbor)
                        visited.add(neighbor)
            return -1

        self.graph = [[] for _ in range(n)]
        for i in range(n - 1):
            self.graph[i].append(i + 1)
        res = []
        for query in queries:
            self.graph[query[0]].append(query[1])
            res.append(bfs(self.graph, n))
        return res

    def minimumObstacles(self, grid: List[List[int]]) -> int:
        """
        11.28
        2290. Minimum Obstacle Removal to Reach Corner
        https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/description/?envType=daily-question&envId=2024-11-28
        """
        m, n = map(len, (grid, grid[0]))
        dist = [[sys.maxsize] * n for _ in range(m)]
        dist[0][0] = grid[0][0]
        hp = [(dist[0][0], 0, 0)]
        while hp:
            o, r, c = heappop(hp)
            if (r, c) == (m - 1, n - 1):
                return o
            for i, j in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
                if m > i >= 0 <= j < n and grid[i][j] + o < dist[i][j]:
                    dist[i][j] = grid[i][j] + o
                    heappush(hp, (dist[i][j], i, j))
        return -1

    def minimumTime(self, grid: List[List[int]]) -> int:
        """
        11.29
        2577. Minimum Time to Visit a Cell In a Grid
        https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid/description/?envType=daily-question&envId=2024-11-29
        """
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        m, n = len(grid), len(grid[0])
        visited = set()
        pq = [(grid[0][0], 0, 0)]

        while pq:
            time, row, col = heappop(pq)
            if row == m - 1 and col == n - 1:
                return time
            if (row, col) in visited:
                continue
            visited.add((row, col))
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                r, c = row + dr, col + dc
                if 0 <= r < m and 0 <= c < n and (r, c) not in visited:
                    wait = 1 if ((grid[r][c] - time) % 2 == 0) else 0
                    heappush(pq, (max(time + 1, grid[r][c] + wait), r, c))
        return -1

    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        """
        11.30
        2097. Valid Arrangement of Pairs
        https://leetcode.com/problems/valid-arrangement-of-pairs/description/?envType=daily-question&envId=2024-11-30
        """
        graph = collections.defaultdict(list)
        degree = collections.defaultdict(int)  # net out degree
        for x, y in pairs:
            graph[x].append(y)
            degree[x] += 1
            degree[y] -= 1

        for k in degree:
            if degree[k] == 1:
                x = k
                break

        ans = []
        stack = [x]
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            ans.append(stack.pop())
        ans.reverse()
        return [[ans[i], ans[i + 1]] for i in range(len(ans) - 1)]


primes = [
    2,
    3,
    5,
    7,
    11,
    13,
    17,
    19,
    23,
    29,
    31,
    37,
    41,
    43,
    47,
    53,
    59,
    61,
    67,
    71,
    73,
    79,
    83,
    89,
    97,
    101,
    103,
    107,
    109,
    113,
    127,
    131,
    137,
    139,
    149,
    151,
    157,
    163,
    167,
    173,
    179,
    181,
    191,
    193,
    197,
    199,
    211,
    223,
    227,
    229,
    233,
    239,
    241,
    251,
    257,
    263,
    269,
    271,
    277,
    281,
    283,
    293,
    307,
    311,
    313,
    317,
    331,
    337,
    347,
    353,
    359,
    367,
    373,
    379,
    383,
    389,
    397,
    401,
    409,
    419,
    421,
    431,
    433,
    439,
    443,
    449,
    457,
    461,
    463,
    467,
    479,
    487,
    491,
    499,
    503,
    509,
    521,
    523,
    541,
    547,
    557,
    563,
    569,
    571,
    577,
    587,
    593,
    599,
    601,
    607,
    613,
    617,
    619,
    631,
    641,
    643,
    647,
    653,
    659,
    661,
    673,
    677,
    683,
    691,
    701,
    709,
    719,
    727,
    733,
    739,
    743,
    751,
    757,
    761,
    769,
    773,
    787,
    797,
    809,
    811,
    821,
    823,
    827,
    829,
    839,
    853,
    857,
    859,
    863,
    877,
    881,
    883,
    887,
    907,
    911,
    919,
    929,
    937,
    941,
    947,
    953,
    967,
    971,
    977,
    983,
    991,
    997,
]
