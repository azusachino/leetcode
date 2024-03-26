import random


class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.hash = {}

    def insert(self, val: int) -> bool:
        if val in self.hash:
            return False
        # save value to index `hash`
        self.hash[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hash:
            return False
        idx = self.hash[val]
        # exchange idx with last number
        self.hash[self.nums[-1]] = idx
        self.nums[idx], self.nums[-1] = self.nums[-1], self.nums[idx]
        self.nums.pop()
        del self.hash[val]
        return True

    def getRandom(self) -> int:
        # randint with inclusive boundary
        return self.nums[random.randint(0, len(self.nums) - 1)]
