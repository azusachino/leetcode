class Solution:
    def addBinary(self, a: str, b: str) -> str:
        stack = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(a[j])
                j -= 1

            stack.append(str(carry % 2))
            carry //= 2
        return "".join(reversed(stack))

    def reverseBits(self, n: int) -> int:
        """
        1. we are shifting the bits of res by left by 1 position
        2. adding last bit of n to res. (n&1) gives us the last digit of n, since it does AND between the last bit of n and 1
        3. since we already got the last bit, we are now right shifting n by 1 unit using n >> 1 so that in the next iteration of the loop, the second-to-last bit of n can be added to res.
        """
        res = 0
        for _ in range(32):
            res = (res << 1) + (n & 1)
            n >>= 1
        return res
