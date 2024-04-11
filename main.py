from collections import deque
from typing import List


class Demo:
    def update_bit(self, bits, num, action):
        for i in range(32):
            # retrieve every binary bit of num
            if (num >> i) & 1:
                bits[i] += action

    def bits_to_int(self, bits):
        res = 0
        for i in range(32):
            if bits[i] != 0:
                res |= 1 << i
        return res

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # square!!!
        n = len(grid)

        # start, end validity check
        if not grid[0][0] == grid[-1][-1] == 0:
            return -1

        # bfs neighbor helper
        def neighbor(i, j):
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    x, y = i + di, j + dj
                    if 0 <= x < n and 0 <= y < n and grid[x][y] == 0:
                        yield (x, y)

        # track step in bfs
        q = deque([(0, 0, 1)])
        seen = set((0, 0))

        while q:
            (i, j, step) = q.popleft()
            if i == j == n - 1:
                return step
            for x, y in neighbor(i, j):
                if (x, y) not in seen:
                    seen.add((x, y))
                    q.append((x, y, step + 1))

        return -1


if __name__ == "__main__":
    d = Demo()
    bits = [0] * 32
    bits[3] = 1
    print(d.bits_to_int(bits))
    print("hello python")
    grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
    d.shortestPathBinaryMatrix(grid)
