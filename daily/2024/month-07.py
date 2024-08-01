from collections import defaultdict, deque
from heapq import heappop, heappush
from math import ceil, gcd, inf
import sys
from typing import Counter, List, Optional

from linklist.list import ListNode
from tree.local_tree import TreeNode


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        """
        07.01
        1550. Three Consecutive Odds
        https://leetcode.com/problems/three-consecutive-odds/description/?envType=daily-question&envId=2024-07-01
        """
        n = len(arr)

        def is_odd(x):
            return x % 2 == 1

        for i in range(n - 2):
            if is_odd(arr[i]) and is_odd(arr[i + 1]) and is_odd(arr[i + 2]):
                return True
        return False

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        07.02
        350. Intersection of Two Arrays II
        https://leetcode.com/problems/intersection-of-two-arrays-ii/description/?envType=daily-question&envId=2024-07-02
        """
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)

        cnt = Counter(nums1)
        ans = []
        for x in nums2:
            if cnt[x]:
                ans.append(x)
                cnt[x] -= 1
        return ans

    def minDifference(self, nums: List[int]) -> int:
        """
        07.03
        1509. Minimum Difference Between Largest and Smallest Value in Three Moves
        https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/description/?envType=daily-question&envId=2024-07-03
        """
        l = len(nums)
        if l <= 4:
            return 0
        nums.sort()
        res = sys.maxsize
        for i in range(4):
            res = min(res, nums[l - 4 + i] - nums[i])
        return res

    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        07.04
        2181. Merge Nodes in Between Zeros
        https://leetcode.com/problems/merge-nodes-in-between-zeros
        """
        slow = head
        while True:
            fast = slow.next
            # put the values onto the previous 0
            while fast and fast.val != 0:
                slow.val += fast.val
                fast = fast.next

            if fast.next:
                slow.next = fast
                slow = slow.next
            else:
                # break the connection to the rest
                slow.next = None
                return head

    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        """
        07.05
        2058. Find the Minimum and Maximum Number of Nodes Between Critical Points
        https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points
        """
        prev, cur = head, head.next
        first = last = None
        res = [sys.maxsize, -sys.maxsize]
        # cur position
        idx = 1
        while cur.next:
            if cur.val < min(prev.val, cur.next.val) or cur.val > max(
                prev.val, cur.next.val
            ):
                if not last:
                    first = last = idx
                else:
                    # tracking minimum distance along the way
                    res[0] = min(res[0], idx - last)
                    res[1] = idx - first
                    last = idx
            idx += 1
            prev, cur = cur, cur.next
        return res if first != last else [-1, -1]

    def passThePillow(self, n: int, time: int) -> int:
        """
        07.06
        2582. Pass the Pillow
        https://leetcode.com/problems/pass-the-pillow
        """
        return n - abs(n - 1 - time % (n * 2 - 2))

    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        """
        07.07
        1518. Water Bottles
        https://leetcode.com/problems/water-bottles/description/?envType=daily-question&envId=2024-07-07
        """
        return numBottles + (numBottles - 1) // (numExchange - 1)

    def findTheWinner(self, n: int, k: int) -> int:
        """
        07.08
        1823. Find the Winner of the Circular Game
        https://leetcode.com/problems/find-the-winner-of-the-circular-game/description/?envType=daily-question&envId=2024-07-08
        """
        nums = deque(range(n))
        while len(nums) > 1:
            nums.rotate(1 - k)
            nums.popleft()
        return nums.pop() + 1

    def averageWaitingTime(self, A: List[List[int]]) -> float:
        """
        07.09
        1701. Average Waiting Time
        https://leetcode.com/problems/average-waiting-time/description/?envType=daily-question&envId=2024-07-09
        """
        n = len(A)
        arr = []
        cur = 0
        for x, y in A:
            if x > cur:
                cur = x + y
                arr.append(y)
            else:
                cur += y
                arr.append(cur - x)
        return sum(arr) / n

    def minOperations(self, logs: List[str]) -> int:
        """
        07.10
        1598. Crawler Log Folder
        https://leetcode.com/problems/crawler-log-folder/description/?envType=daily-question&envId=2024-07-10
        stack
        """
        st = []
        for d in logs:
            if d == "./":
                continue
            elif d == "../":
                if st:
                    st.pop()
            else:
                st.append(d)
        return len(st)

    def reverseParentheses(self, s: str) -> str:
        """
        07.11
        1190. Reverse Substrings Between Each Pair of Parentheses
        https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses
        """
        st = []
        for c in s:
            if c == ")":
                new_ = []
                # pop out non (), to do reverse
                while st[-1] != "(":
                    new_.append(st.pop())

                st.pop()
                st.extend(new_)
            else:
                st.append(c)
        return "".join(st)

    def maximumGain(self, s: str, x: int, y: int) -> int:
        """
        07.12
        1717. Maximum Score From Removing Substrings
        https://leetcode.com/problems/maximum-score-from-removing-substrings/description/?envType=daily-question&envId=2024-07-12
        """
        # let x be with higher score
        if x < y:
            x, y, s = y, x, s[::-1]
        a = b = res = 0
        for c in s:
            if c == "a":
                a += 1
            elif c == "b":
                # greedily remove x-pair
                if a:
                    res += x
                    a -= 1
                else:
                    b += 1
            # reset a,b count
            else:
                res += min(a, b) * y
                a = b = 0
        return res + min(a, b) * y

    def survivedRobotsHealths(
        self, positions: List[int], h: List[int], directions: str
    ) -> List[int]:
        """
        07.13
        2751. Robot Collisions
        https://leetcode.com/problems/robot-collisions/description/?envType=daily-question&envId=2024-07-13
        """
        n = len(positions)
        # sort with its position
        ind = sorted(range(n), key=positions.__getitem__)
        stack = []
        for i in ind:
            # right-ward robots won't collide
            if directions[i] == "R":
                stack.append(i)
                continue
            # If it's moving to left, compare its healths[i] with the top robot in stack.
            while stack and h[i] > 0:
                if h[stack[-1]] < h[i]:
                    h[stack.pop()] = 0
                    h[i] -= 1
                elif h[stack[-1]] > h[i]:
                    h[stack[-1]] -= 1
                    h[i] = 0
                else:
                    h[stack.pop()] = 0
                    h[i] = 0
        return [v for v in h if v > 0]

    def countOfAtoms(self, formula):
        """
        07.14
        726. Number of Atoms
        https://leetcode.com/problems/number-of-atoms/description/?envType=daily-question&envId=2024-07-14
        """
        dic, coeff, stack, elem, cnt, i = defaultdict(int), 1, [], "", 0, 0
        for c in formula[::-1]:
            if c.isdigit():
                cnt += int(c) * (10**i)
                i += 1
            elif c == ")":
                if cnt:
                    stack.append(cnt)
                    coeff *= cnt
                else:
                    stack.append(1)
                i = cnt = 0
            elif c == "(":
                coeff //= stack.pop()
                i = cnt = 0
            elif c.isupper():
                elem += c
                dic[elem[::-1]] += (cnt or 1) * coeff
                elem = ""
                i = cnt = 0
            elif c.islower():
                elem += c
        return "".join(k + str(v > 1 and v or "") for k, v in sorted(dic.items()))

    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        """
        07.15
        2196. Create Binary Tree From Descriptions
        https://leetcode.com/problems/create-binary-tree-from-descriptions/description/?envType=daily-question&envId=2024-07-15
        """
        children = set()
        m = {}
        for p, c, l in descriptions:
            np = m.setdefault(p, TreeNode(p))
            nc = m.setdefault(c, TreeNode(c))
            if l:
                np.left = nc
            else:
                np.right = nc
            children.add(c)
        root = (set(m) - set(children)).pop()
        return m[root]

    def getDirections(
        self, root: Optional[TreeNode], startValue: int, destValue: int
    ) -> str:
        """
        07.16
        2096. Step-By-Step Directions From a Binary Tree Node to Another
        https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/description/?envType=daily-question&envId=2024-07-16
        """

        def find(n: TreeNode, val: int, path: List[str]) -> bool:
            if n.val == val:
                return True
            if n.left and find(n.left, val, path):
                path.append("L")
            elif n.right and find(n.right, val, path):
                path.append("R")
            return path

        s, d = [], []
        find(root, startValue, s)
        find(root, destValue, d)
        while len(s) and len(d) and s[-1] == d[-1]:
            s.pop()
            d.pop()
        return "".join("U" * len(s)) + "".join(reversed(d))

    def delNodes(
        self, root: Optional[TreeNode], to_delete: List[int]
    ) -> List[TreeNode]:
        """
        07.17
        1110. Delete Nodes And Return Forest
        https://leetcode.com/problems/delete-nodes-and-return-forest/description/
        """
        if not root:
            return []

        res = []
        #
        st = set(to_delete)

        def dfs(node, is_root):
            if not node:
                return None
            is_del = node.val in st

            node.left = dfs(node.left, is_del)
            node.right = dfs(node.right, is_del)

            # only append root node
            if not is_del and is_root:
                res.append(node)

            return None if is_del else node

        dfs(root, True)
        return res

    def countPairs(self, root: TreeNode, distance: int) -> int:
        """
        07.18
        1530. Number of Good Leaf Nodes Pairs
        https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/description/
        """
        self.res = 0

        def dfs(node: Optional[TreeNode]):
            if not node:
                return []
            # distance to the root node
            if not node.left and not node.right:
                return [1]
            ll = dfs(node.left)
            rl = dfs(node.right)
            self.res += sum(l + r <= distance for l in ll for r in rl)
            return [1 + i for i in ll + rl]

        dfs(root)
        return self.res

    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        """
        07.19
        1380. Lucky Numbers in a Matrix
        https://leetcode.com/problems/lucky-numbers-in-a-matrix/description/
        """
        mi = [min(row) for row in matrix]
        mx = [max(col) for col in zip(*matrix)]
        return [
            cell for i, row in enumerate(matrix) for j, cell in row if mi[i] == mx[j]
        ]

    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        """
        07.20
        1605. Find Valid Matrix Given Row and Column Sums
        https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/description/?envType=daily-question&envId=2024-07-20
        """
        m, n = len(rowSum), len(colSum)
        res = [[0] * n for i in range(m)]

        for i in range(m):
            for j in range(n):
                res[i][j] = min(rowSum[i], colSum[j])
                rowSum[i] -= res[i][j]
                colSum[j] -= res[i][j]
        return res

    def buildMatrix(
        self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]
    ) -> List[List[int]]:
        """
        07.21
        2392. Build a Matrix With Conditions
        https://leetcode.com/problems/build-a-matrix-with-conditions/description/?envType=daily-question&envId=2024-07-22
        """

        # return True if all okay and return False if cycle was found
        def dfs(src, graph, visited, cur_path, res) -> bool:
            if src in cur_path:
                return False  # cycle detected

            if src in visited:
                return True  # all okay, but we've already visited this node

            visited.add(src)
            cur_path.add(src)

            for neighbor in graph[src]:
                if not dfs(
                    neighbor, graph, visited, cur_path, res
                ):  # if any child returns false
                    return False

            cur_path.remove(src)  # backtrack path
            res.append(src)
            return True

        # if there will be cycle - return empty array, in other case return 1d array as described above
        def topo_sort(edges) -> list[int]:
            graph = defaultdict(list)
            for src, dst in edges:
                graph[src].append(dst)

            visited: set[int] = set()
            cur_path: set[int] = set()
            res: list[int] = []

            for src in range(1, k + 1, 1):
                if not dfs(src, graph, visited, cur_path, res):
                    return []

            return res[
                ::-1
            ]  # we will have res as reversed so we need to reverse it one more time

        row_sorting: list[int] = topo_sort(rowConditions)
        col_sorting: list[int] = topo_sort(colConditions)
        if [] in (row_sorting, col_sorting):
            return []

        value_position: dict[int, list[int]] = {
            n: [0, 0] for n in range(1, k + 1, 1)
        }  # element -> [row_index, col_index]
        for ind, val in enumerate(row_sorting):
            value_position[val][0] = ind
        for ind, val in enumerate(col_sorting):
            value_position[val][1] = ind

        res: list[list[int]] = [[0 for _ in range(k)] for _ in range(k)]
        for value in range(1, k + 1, 1):
            row, column = value_position[value]
            res[row][column] = value

        return res

    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        """
        07.22
        https://leetcode.com/problems/sort-the-people/description/
        2418. Sort the People
        """
        return [n for _, n in sorted(zip(heights, names), reverse=True)]

    def frequencySort(self, nums: List[int]) -> List[int]:
        """
        07.23
        1636. Sort Array by Increasing Frequency
        https://leetcode.com/problems/sort-array-by-increasing-frequency/description/
        """
        freqs = Counter(nums)
        nums.sort(key=lambda x: (freqs[x], -x))
        return nums

    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        """
        07.24
        2191. Sort the Jumbled Numbers
        https://leetcode.com/problems/sort-the-jumbled-numbers/description/
        """

        def cvt(num):
            if num == 0:
                return mapping[0]
            n, f = 0, 1
            while num > 0:
                num, r = divmod(num, 10)
                n += mapping[r] * f
                f *= 10
            return n

        return nums.sort(key=lambda x: cvt(x))

    def sortArray(self, nums: List[int]) -> List[int]:
        """
        07.25
        912. Sort an Array
        https://leetcode.com/problems/sort-an-array/description/?envType=daily-question&envId=2024-07-25
        """
        return sorted(nums)

    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        """
        07.26
        1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance
        https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/description/
        """
        dis = [[sys.maxsize] * n for _ in range(n)]
        for i, j, w in edges:
            dis[i][j] = dis[j][i] = w
        for i in range(n):
            dis[i][i] = 0

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
        res = {sum(d <= distanceThreshold for d in dis[i]): i for i in range(n)}
        return res[min(res)]

    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:
        """
        07.27
        2976. Minimum Cost to Convert String I
        https://leetcode.com/problems/minimum-cost-to-convert-string-i/description/?envType=daily-question&envId=2024-07-27
        """
        g = [[inf] * 26 for _ in range(26)]
        for i in range(26):
            g[i][i] = 0
        a = ord("a")
        for x, y, z in zip(original, changed, cost):
            x = ord(x) - a
            y = ord(y) - a
            g[x][y] = min(g[x][y], z)
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    g[i][j] = min(g[i][j], g[i][k] + g[k][j])
        res = 0
        for x, y in zip(source, target):
            if x != y:
                x = ord(x) - a
                y = ord(y) - a
                if g[x][y] >= inf:
                    return -1
                res += g[x][y]

        return res

    def secondMinimum(self, n, edges, time, change):
        """
        07.28
        2045. Second Minimum Time to Reach Destination
        https://leetcode.com/problems/second-minimum-time-to-reach-destination/description/
        """
        D = [[] for _ in range(n + 1)]
        D[1] = [0]
        G, heap = defaultdict(list), [(0, 1)]

        for a, b in edges:
            G[a] += [b]
            G[b] += [a]

        while heap:
            min_dist, idx = heappop(heap)
            if idx == n and len(D[n]) == 2:
                return max(D[n])

            for neib in G[idx]:
                if (min_dist // change) % 2 == 0:
                    cand = min_dist + time
                else:
                    cand = ceil(min_dist / (2 * change)) * (2 * change) + time

                if not D[neib] or (len(D[neib]) == 1 and D[neib] != [cand]):
                    D[neib] += [cand]
                    heappush(heap, (cand, neib))

    def numTeams(self, rating: List[int]) -> int:
        """
        07.29
        1395. Count Number of Teams
        https://leetcode.com/problems/count-number-of-teams/description/?envType=daily-question&envId=2024-07-29
            int numTeams(vector<int> &rating)
            {
                int r = 0;
                const int n = rating.size();
                for (int i = 0; i < n; ++i)
                {
                    for (int j = 0; j < i; ++j)
                    {
                        for (int k = 0; k < j; ++k)
                        {
                            if ((rating[i] < rating[j] && rating[j] < rating[k]) || (rating[i] > rating[j] && rating[j] > rating[k]))
                            {
                                ++r;
                            }
                        }
                    }
                }
                return r;
            }
        """
        res = 0
        n = len(rating)
        for i, z in enumerate(rating):
            l = sum(x < z for x in rating[:i])
            r = sum(y > z for y in rating[i + 1 :])
            res += l * r
            res += (i - l) * (n - i - 1 - r)
        return res

    def minimumDeletions(self, s: str) -> int:
        """
        07.30
        1653. Minimum Deletions to Make String Balanced
        https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/description/?envType=daily-question&envId=2024-07-30
        """
        # could improve the space to O(1)
        st = []
        cnt = 0
        for c in s:
            if st and c == "a":
                cnt += 1
                st.pop()
            elif c == "b":
                st.append(c)
        return cnt

    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        """
        07.31
        1105. Filling Bookcase Shelves
        https://leetcode.com/problems/filling-bookcase-shelves/description/
        """
        n = len(books)
        # dp[i]: the min height for placing first books `i-1` on shelves
        dp = [sys.maxsize] * (n + 1)
        dp[0] = 0
        for i in range(n):
            cur_width = max_height = 0
            for j in range(i, -1, -1):
                cur_width += books[j][0]
                if cur_width > shelfWidth:
                    break
                max_height = max(max_height, books[j][1])
                dp[i + 1] = min(dp[i + 1], dp[j] + max_height)
        return dp[n]


class OtherSolution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(arr: List[int]):
            if not arr:
                return None
            m = max(arr)
            i = arr.index(m)
            root = TreeNode(m)
            root.left = helper(arr[:i])
            root.right = helper(arr[i + 1 :])
            return root

        return helper(nums)

    def minOperations(self, nums: List[int]) -> int:
        """
        2654. Minimum Number of Operations to Make All Array Elements Equal to 1
        https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/description/
        """
        n = len(nums)
        cnt = nums.count(1)
        if cnt:
            return n - cnt
        mi = n + 1
        for i in range(n):
            g = nums[i]
            for j in range(i + 1, n):
                g = gcd(g, nums[j])
                if g == 1:
                    mi = min(mi, j - i + 1)
        return -1 if mi > n else n - 1 + mi - 1

    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        """
        1654. Minimum Jumps to Reach Home
        https://leetcode.com/problems/minimum-jumps-to-reach-home/description/
        BFS
        """
        s = set(forbidden)
        q = deque([(0, 1)])
        vis = {(0, 1)}
        ans = 0
        while q:
            for _ in range(len(q)):
                i, k = q.popleft()
                if i == x:
                    return ans
                nxt = [(i + a, 1)]
                if k & 1:
                    nxt.append((i - b, 0))
                for j, k in nxt:
                    if 0 <= j < 6000 and j not in s and (j, k) not in vis:
                        q.append((j, k))
                        vis.add((j, k))
            ans += 1
        return -1

    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def height(node):
            if not node:
                return -1
            return 1 + max(height(node.left), height(node.right))

        def dfs(node, r, c):
            if not node:
                return
            res[r][c] = str(node.val)
            dfs(node.left, r + 1, c - 2 ** (h - r - 1))
            dfs(node.right, r + 1, c + 2 ** (h - r - 1))

        h = height(root)
        m, n = h + 1, 2 ** (h + 1) - 1
        res = [[""] * n for _ in range(m)]
        dfs(root, 0, (n - 1) // 2)
        return res

    def printTreeAnother(self, root):
        def get_height(node):
            if not node:
                return 0
            return 1 + max(get_height(node.left), get_height(node.right))

        def dfs(node, row, left, right):
            if not node:
                return
            mid = (left + right) // 2
            self.output[row][mid] = str(node.val)
            dfs(node.left, row + 1, left, mid - 1)
            dfs(node.right, row + 1, mid + 1, right)

        h = get_height(root)
        width = 2**h - 1
        self.output = [[""] * width for _ in range(h)]
        dfs(root, 0, 0, width - 1)
        return self.output

    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        while True:
            fast = slow.next
            # put the values onto the previous 0
            while fast and fast.val != 0:
                slow.val += fast.val
                fast = fast.next

            if fast.next:
                slow.next = fast
                slow = slow.next
            else:
                # break the connection to the rest
                slow.next = None
                return head

    def maxDepth(self, s: str) -> int:
        d = 0
        res = 0
        for c in s:
            if c == "(":
                d += 1
            elif c == ")":
                d -= 1
            res = max(res, d)
        return res

    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        g = defaultdict(set)
        for x, y in roads:
            g[x].add(y)
            g[y].add(x)
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                # remove inter-connection, be counted only once
                res = max(res, len(g[i]) + len(g[j]) - (i in g[j]))
        return res

    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        def check(x, y):
            i, j = 0, len(y) - 1
            # Greedily take the a_suffix and b_prefix as long as they are palindrome,
            while i < j and x[i] == y[j]:
                i, j = i + 1, j - 1
            # already palindrome, or
            return i >= j or palindrome(x, i, j) or palindrome(y, i, j)

        def palindrome(s, i, j):
            return s[i : j + 1] == s[i : j + 1][::-1]

        return check(a, b) or check(b, a)

    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        m = {}
        res = -1
        for i, c in enumerate(s):
            if c in m:
                res = max(res, i - m[c] - 1)
            else:
                m[c] = i
        return res

    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        while numBottles >= numExchange:
            numBottles, remainder = divmod(numBottles, numExchange)
            ans += numBottles
            numBottles += remainder
        return ans

    def findTheWinner(self, n: int, k: int) -> int:
        arr = list(range(n))
        steps = 0
        idx = 0
        while steps < n:
            idx = (idx + k) // len(arr)
            arr = arr[:idx] + arr[idx + 1 :]
            steps += 1
        return arr[0]

    def makeGood(self, s: str) -> str:
        stk = []
        for c in s:
            if stk and stk[-1][1] != c.isupper() and stk[-1][-1] == c.upper():
                stk.pop()
            else:
                stk.append([c, c.isupper(), c.upper()])
        return "".join(x[0] for x in stk)

    def minRemoveToMakeValid(self, s: str) -> str:
        def helper(s, x, y):
            stk = []
            cnt = 0
            for c in s:
                if c == x:
                    cnt += 1
                elif c == y:
                    if cnt:
                        cnt -= 1
                    else:
                        continue
                stk.append(c)
            return stk

        return "".join(helper(helper(s, "(", ")")[::-1], ")", "(")[::-1])

    def getDirections(
        self, root: Optional[TreeNode], startValue: int, destValue: int
    ) -> str:
        def lca(node):
            """
            Return lowest common ancestor of start and dest nodes.
            """
            if not node or node.val in (startValue, destValue):
                return node
            left, right = lca(node.left), lca(node.right)
            return node if left and right else left or right

        p = lca(root)
        ps = pd = ""
        stk = [(p, "")]
        while stk:
            node, path = stk.pop()
            if node.val == startValue:
                ps = path
            elif node.val == destValue:
                pd = path

            if node.left:
                stk.append((node.left, path + "L"))
            if node.right:
                stk.append((node.right, path + "R"))
        return "U" * len(ps) + pd

    def delNodes(
        self, root: Optional[TreeNode], to_delete: List[int]
    ) -> List[TreeNode]:
        del_set = set(to_delete)
        res = []

        def dfs(root, is_root):
            if not root:
                return
            is_root_del = root.val in del_set
            # append only root, also not deleted
            if is_root and not is_root_del:
                res.append(root)
            # if root deleted, child becomes new root
            root.left = dfs(root.left, is_root_del)
            root.right = dfs(root.right, is_root_del)
            return None if is_root_del else root

        dfs(root, True)
        return res

    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        return list({min(row) for row in matrix} & {max(col) for col in zip(*matrix)})

    def lowestCommonAncestor(
        self, root: "TreeNode", nodes: "List[TreeNode]"
    ) -> "TreeNode":
        """
        1676 - Lowest Common Ancestor of a Binary Tree IV
            https://leetcode.ca/2020-07-02-1676-Lowest-Common-Ancestor-of-a-Binary-Tree-IV/
        """

        def dfs(root):
            if not root or root.val in s:
                return root
            l, r = dfs(root.left), dfs(root.right)
            # find both l and r
            if l and r:
                return root
            return l or r

        s = {node.val for node in nodes}
        return dfs(root)

    def frequencySort(self, nums: List[int]) -> List[int]:
        from functools import cmp_to_key

        def cmp_(a, b):
            x, y = cnt[a], cnt[b]
            if x != y:
                return x - y
            return b - a

        cnt = Counter(nums)
        return sorted(nums, key=cmp_to_key(cmp_))
