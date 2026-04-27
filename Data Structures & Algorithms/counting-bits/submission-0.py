class Solution:
    def countBits(self, n: int) -> List[int]:
        count = [0]*(n+1)
        for i in range(n+1):
            n = i
            while i:
                count[n]+=1
                i = i&(i-1)
        return count
                
