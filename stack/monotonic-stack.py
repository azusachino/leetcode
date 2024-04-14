from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        枚举每根柱子的高度 h 作为矩形的高度，向左右两边找第一个高度 小于(<) h 的下标 left_i, right_i
        那么此时矩形面积为 h * (right_i - left_i - 1)，求最大值即可。
        h: [2, 1, 5, 6, 2, 3]
        l: [-1, -1, 1, 2, 1, 4]
        r: [1, 6, 4, 4, 6, 6]
        """
        n = len(heights)
        stk = []
        left = [-1] * n
        right = [n] * n
        for i, h in enumerate(heights):
            # we cannot extend the rectangle to current h anymore, because it's smaller, pop it out
            while stk and h <= heights[stk[-1]]:
                right[stk[-1]] = i
                stk.pop()
            if stk:
                left[i] = stk[-1]
            stk.append(i)
        return max(h * (right[i] - left[i] - 1) for i, h in enumerate(heights))

    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        n = len(heights)
        stk = []  # pair: (index, height)

        for i, h in enumerate(heights):
            # preserve the current index
            start = i
            # if the top of stack is greater than current `h`, we calculate what we have now
            # then pop it out, also update the older index, as we could form a rectangle from that index with current `h`
            while stk and stk[-1][1] >= h:
                index, height = stk.pop()
                res = max(res, height * (i - index))
                start = index
            stk.append((start, h))

        # the remaining was sorted array, try to find the maximum area
        for i, h in stk:
            res = max(res, h * (n - i))
        return res
