from typing import List


class CustomFunction:
    # Returns f(x, y) for any given positive integers x and y.
    # Note that f(x, y) is increasing with respect to both x and y.
    # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
    def f(self, x, y):
        pass


class Solution:
    """
    1237. Find Positive Integer Solution for a Given Equation
        https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/description/
    1238. Circular Permutation in Binary Representation
        https://leetcode.com/problems/circular-permutation-in-binary-representation/description/
        math, bitwise
    1239. Maximum Length of a Concatenated String with Unique Characters
        https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/description/
    1240. Tiling a Rectangle with the Fewest Squares
        https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/description/
    """

    def findSolution(self, customfunction: CustomFunction, z: int) -> List[List[int]]:
        result = []
        x, y = 1, 1000

        while x <= 1000 and y > 0:
            val = customfunction.f(x, y)
            if val == z:
                result.append([x, y])
                y -= 1
            elif val < z:
                x += 1
            else:
                y -= 1

        return result

    def circularPermutation(self, n: int, start: int) -> List[int]:
        size = 1 << n  # Calculate 2^n
        gray_code = []  # List to store Gray Code sequence
        result = []  # List for the final circular permutation

        # Generate Gray Code
        for i in range(size):
            gray_code.append(i ^ (i >> 1))  # Calculate Gray Code value

        # Find Starting Index
        j = gray_code.index(start)

        # Build Circular Permutation
        for i in range(j, j + size):
            result.append(gray_code[i % size])  # Wrap around using modulo

        return result

    def maxLength(self, arr: List[str]) -> int:
        # remove string with duplicates
        cs = [set(s) for s in arr if len(s) == len(set(s))]
        self.res = 0

        def backtrack(i, cur):
            self.res = max(self.res, len(cur))
            for j in range(i, len(cs)):
                # combine with next non intersection string
                if not (set(cur) & cs[j]):
                    backtrack(j + 1, cur + "".join(cs[j]))

        backtrack(0, "")
        return self.res

    def tilingRectangle(self, n: int, m: int) -> int:
        pass
