class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_n = 0
        print(bin(n))
        for i in range(32):
            reversed_n = reversed_n<<1
            val = n&1
            reversed_n = reversed_n | val
            n=n>>1
        print(bin(reversed_n))
        return reversed_n