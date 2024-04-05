from typing import List


class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        l = len(s)
        cnt = 0
        for c in s:
            if c == "1":
                cnt += 1
        ret = "1"
        for _ in range(l - cnt):
            ret += "0"
        for _ in range(cnt - 1):
            ret += "1"

        return ret[::-1]

    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        def updateBits(bits: List[int], x: int, change: int):
            for i in range(32):
                if (x >> i) & 1:
                    bits[i] += change

        def bitsToNum(bits: List[int]) -> int:
            result = 0
            for i in range(32):
                if bits[i]:
                    result |= 1 << i
            return result

        n = len(nums)
        result = n + 1
        bits = [0] * 32
        l = 0
        for r in range(n):
            updateBits(bits, nums[r], 1)
            while l <= r and bitsToNum(bits) >= k:
                result = min(result, r - l + 1)
                updateBits(bits, nums[l], -1)
                l += 1
        return result if result != n + 1 else -1


if __name__ == "__main__":
    s = Solution()
    print("maximumOddBinaryNumber ", s.maximumOddBinaryNumber("0101"))


class AnotherSolution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        i, sz = 0, len(s)
        ss = list(s)
        for j in range(sz - 1):
            if ss[j] == "1":
                ss[i], ss[j] = ss[j], ss[i]
                i += 1
        if ss[-1] != "1":
            ss[sz - 1], ss[i - 1] = ss[i - 1], ss[sz - 1]
        return "".join(ss)
