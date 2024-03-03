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
