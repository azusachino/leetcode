from typing import List
import heapq
from collections import Counter


class PQItem:
    def __init__(self, priority: int, data: str):
        self.priority = priority
        self.data = data

    def __lt__(self, other) -> bool:
        return self.priority < other.priority

    def __repr__(self) -> str:
        return "%d @ %s" % (self.priority, self.data)


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = list(Counter(tasks).values())
        most_repeats = max(counts)
        num_longest = counts.count(most_repeats)
        return max(len(tasks), (most_repeats - 1) * (n + 1) + num_longest)


if __name__ == "__main__":
    solution = Solution()
    tasks = ["A", "A", "A", "B", "B", "B"]
    print("leastInterval", solution.leastInterval(tasks, 2))
