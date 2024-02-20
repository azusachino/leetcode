class UF:
    def __init__(self, n):
        self.nums = list(range(n))
        self.rank = [1] * n
        self.count = n
