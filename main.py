class Demo:
    def update_bit(self, bits, num, action):
        for i in range(32):
            # retrieve every binary bit of num
            if (num >> i) & 1:
                bits[i] += action

    def bits_to_int(self, bits):
        res = 0
        for i in range(32):
            if bits[i] != 0:
                res |= 1 << i
        return res


if __name__ == "__main__":
    d = Demo()
    bits = [0] * 32
    bits[3] = 1
    print(d.bits_to_int(bits))
    print("hello python")
