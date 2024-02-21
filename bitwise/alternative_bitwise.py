class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while right > left:
            right &= right - 1
        return right & left


class AlternativeSolution:
    def rangeBitwiseAnd(self, l: int, r: int) -> int:
        i = 0
        # if the left bits are not equal
        while l != r:
            l >>= 1
            r >>= 1
            i += 1
            print(l, r, i)
        # restore number scale
        return r << i


if __name__ == "__main__":
    AS = AlternativeSolution()
    print(AS.rangeBitwiseAnd(5, 7))
