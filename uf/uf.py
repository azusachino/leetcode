class UF:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.cnt = n

    def find(self, x: int) -> int:
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, p: int, q: int) -> bool:
        x, y = self.find(p), self.find(q)
        if x == y:
            return False
        if self.rank[x] > self.rank[y]:
            x, y = y, x
        self.parent[x] = y
        self.rank[y] += self.rank[x]
        self.cnt -= 1
        return True

    def count(self):
        return self.cnt
