from typing import List
from collections import defaultdict
import heapq


class PQ:
    def __init__(self, price, current_city, steps):
        self.price = price
        self.current_city = current_city
        self.steps = steps

    def __lt__(self, other):
        return self.price < other.price

    def __eq__(self, other):
        return self.price == other.price

    def __str__(self) -> str:
        return "%s, %s, %s" % (self.current_city, self.price, self.steps)

    def __repr__(self) -> str:
        return self.__str__()


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        prices = defaultdict(lambda: defaultdict(int))
        for i, j, x in flights:
            prices[i][j] = x
        # print(prices)
        pq = [PQ(0, src, k + 1)]

        while pq:
            # print(pq)
            top = heapq.heappop(pq)
            price, city, steps = top.price, top.current_city, top.steps
            if city == dst:
                return price
            if steps > 0:
                adj = prices[city]
                # print(adj)
                for adj_city in adj.keys():
                    heapq.heappush(pq, PQ(price + adj[adj_city], adj_city, steps - 1))
        return -1


if __name__ == "__main__":
    s = Solution()
    n = 4
    flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]

    src = 0
    dst = 3
    k = 1
    r = s.findCheapestPrice(n, flights, src, dst, k)
    print("findCheapestPrice", r)
