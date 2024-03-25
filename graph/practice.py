from collections import defaultdict
from typing import List


class Solution:
    def dfs(self, adj_table: dict, src):
        def helper(adj_table, cur):
            if cur:
                print(cur)
                for nxt in adj_table[cur]:
                    helper(adj_table, nxt)

        return helper(adj_table, src)

    def bfs(self, adj_table, src):
        q = [src]
        while q:
            sz = len(q)
            for _ in range(sz):
                cur = q.pop(0)
                print(cur)
                for nxt in adj_table[cur]:
                    q.append(nxt)

    def largest_component(self, graph) -> int:
        max_ = 0
        st = set()
        q = []
        for start in graph:
            if start in st:
                continue
            q.append(start)
            st.add(start)
            count = 1
            while q:
                sz = len(q)
                for _ in range(sz):
                    cur = q.pop(0)
                    st.add(cur)
                    count += 1
                    for nxt in graph[cur]:
                        q.append(nxt)
            max_ = max(max_, count)
        return max_

    def island_count(self, graph: List[List[int]]) -> int:
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def buildGraph(pairs):
            graph = defaultdict(list)
            for a, b in pairs:
                graph[a].append(b)
                graph[b].append(a)
            return graph

        # graph = buildGraph(pairs)
        visited = set()
        count = 0
        q = []
        m, n = len(graph), len(graph[0])
        for i in range(m):
            for j in range(n):
                if graph[i][j] == 0 and graph[i][j] not in visited:
                    q.append((i, j))
                    visited.add((i, j))
                    count += 1
                    while q:
                        sz = len(q)
                        for _ in range(sz):
                            cur = q.pop(0)
                            visited.add(cur)
                            for x, y in dirs:
                                a, b = i + x, j + y
                                if (
                                    0 <= a < m
                                    and 0 <= b < n
                                    and graph[a][b] == 0
                                    and (a, b) not in visited
                                ):
                                    q.append((a, b))
        return count

if __name__ == "__main__":
    adj_table = {"a", ["b", "d"]}
