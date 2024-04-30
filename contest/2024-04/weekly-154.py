import collections
from typing import List


class Solution:
    """
    1189. Maximum Number of Balloons
        https://leetcode.com/problems/maximum-number-of-balloons/description/
    1190. Reverse Substrings Between Each Pair of Parentheses
        https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/description/
    1191. K-Concatenation Maximum Sum
        https://leetcode.com/problems/k-concatenation-maximum-sum/description/
    1192. Critical Connections in a Network
        https://leetcode.com/problems/critical-connections-in-a-network/description/
    """

    def maxNumberOfBalloons(self, text: str) -> int:
        cnt = collections.Counter(text)
        cntBalloon = collections.Counter("balloon")
        return min([cnt[c] // cntBalloon[c] for c in cntBalloon])

    def reverseParentheses(self, s: str) -> str:
        stk = []
        for c in s:
            if c == ")":
                tmp = []
                while stk[-1] != "(":
                    tmp.append(stk.pop())
                # pop out (
                stk.pop()
                stk.extend(tmp)
            else:
                stk.append(c)
        return "".join(stk)

    def kConcatenationMaxSum(self, arr: List[int], k: int, mod=10**9 + 7) -> int:
        def kadane(arr, res=0, cur=0):
            for num in arr:
                cur = max(num, num + cur)
                res = max(res, cur)
            return res

        return (
            ((k - 2) * max(sum(arr), 0) + kadane(arr * 2)) % mod
            if k > 1
            else kadane(arr) % mod
        )

    def criticalConnections(
        self, n: int, connections: List[List[int]]
    ) -> List[List[int]]:
        def makeGraph(connections):
            graph = collections.defaultdict(list)
            for conn in connections:
                graph[conn[0]].append(conn[1])
                graph[conn[1]].append(conn[0])
            return graph

        graph = makeGraph(connections)
        connections = set(map(tuple, (map(sorted, connections))))
        rank = [-2] * n

        def dfs(node, depth):
            if rank[node] >= 0:
                # visiting (0<=rank<n), or visited (rank=n)
                return rank[node]
            rank[node] = depth
            min_back_depth = n
            for neighbor in graph[node]:
                if rank[neighbor] == depth - 1:
                    continue  # don't immmediately go back to parent. that's why i didn't choose -1 as the special value, in case depth==0.
                back_depth = dfs(neighbor, depth + 1)
                if back_depth <= depth:
                    connections.discard(tuple(sorted((node, neighbor))))
                min_back_depth = min(min_back_depth, back_depth)
            rank[node] = (
                n  # this line is not necessary. see the "brain teaser" section below
            )
            return min_back_depth

        dfs(
            0, 0
        )  # since this is a connected graph, we don't have to loop over all nodes.
        return list(connections)
