# Greedy

## Code Snippets

### Switch Bulbs

```python
class Solution:
    # how many rounds do we need to switch all bulbs to off (0, 1)
    # at each step, we can select an index, toggle all bulbs after it (inclusive)
    def bulbs(self, nums: List[int]) -> int:
        cost = 0
        for b in nums:
            # toggle odd times, simply treat current index was toggled
            if cost % 2 != 0:
                b = not b
            # and the toggled bulb was off, cost up
            if b % 2 != 1:
                cost += 1
        return cost
```

## Problems

- switch bulbs
