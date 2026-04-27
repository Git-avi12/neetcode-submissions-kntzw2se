class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count+=1
            n = n&(n-1)
        return count



            # 10001
            # 10000

            # 10000
            # 01111

            # 00000