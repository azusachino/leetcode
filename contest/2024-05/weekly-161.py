class Solution:
    """
    1247. Minimum Swaps to Make Strings Equal
        https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/description/
    1248. Count Number of Nice Subarrays
        https://leetcode.com/problems/count-number-of-nice-subarrays/description/
    """

    def minimumSwap(self, s1: str, s2: str) -> int:
        xy = yx = 0
        for i in range(len(s1)):
            if s1[i] == "x" and s2[i] == "y":
                xy += 1
            if s1[i] == "y" and s2[i] == "x":
                yx += 1
        if (xy + yx) % 2:
            return -1  # Impossible
        # If xy and yx are both even, you can swap pairs of 'xy' and 'yx', resulting in (xy + yx) / 2 swaps.
        # If xy and yx are both odd, you need an extra swap to handle the leftover 'xy' and 'yx', resulting in (xy + yx) / 2 + 1 swaps.
        return (xy + yx) // 2 + (xy % 2)
