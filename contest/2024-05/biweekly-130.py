from itertools import pairwise
from typing import Counter, List


class Solution:
    """
    3142. Check if Grid Satisfies Conditions
        https://leetcode.com/problems/check-if-grid-satisfies-conditions/description/
        graph
    3143. Maximum Points Inside the Square
        https://leetcode.com/problems/maximum-points-inside-the-square/description/
        sort
    3144. Minimum Substring Partition of Equal Character Frequency
        https://leetcode.com/problems/minimum-substring-partition-of-equal-character-frequency/description/
        string, dp
    3145. Find Products of Elements of Big Array
        https://leetcode.com/problems/find-products-of-elements-of-big-array/
    """

    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        for a, b in pairwise(grid[0]):
            if a == b:
                return False

        for c in list(map(set, zip(*grid))):
            if len(c) != 1:
                return False

        return True

    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        """
        class Solution {
            public int maxPointsInsideSquare(int[][] points, String s) {
                var treeMap = new TreeMap<Integer, List<Character>>();
                var n = s.length();
                for (var i = 0; i < n; i++) {
                    var p = points[i];
                    var k = Math.max(Math.abs(p[0]), Math.abs(p[1]));
                    treeMap.computeIfAbsent(k, (v) -> new ArrayList<>()).add(s.charAt(i));
                }

                var set = new HashSet<Character>();
                for (var entry : treeMap.entrySet()) {
                    var v = entry.getValue();
                    var curSet = new HashSet<Character>(v);
                    if (v.size() != curSet.size()) {
                        break;
                    }
                    for (var x : v) {
                        if (set.contains(x)) {
                            return set.size();
                        }
                    }
                    set.addAll(v);
                }
                return set.size();
            }
        }
        """
        pass

    def isBalanced(self, charFreq):
        # Inspired by : lee215
        return len(set(charFreq.values())) == 1

    def minimumSubstringsInPartition(self, S):
        N = len(S)
        DP = [N] * N
        for END in range(N):
            charFreq = Counter()
            for START in range(END, -1, -1):
                charFreq[S[START]] += 1
                if self.isBalanced(charFreq):
                    DP[END] = min(DP[END], 1 + DP[START - 1] if START > 0 else 1)

        return DP[N - 1]
