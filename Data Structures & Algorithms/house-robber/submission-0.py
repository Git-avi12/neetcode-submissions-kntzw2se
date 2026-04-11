class Solution:
    def rob(self, nums: List[int]) -> int:
        fst,snd = 0,0
        for i in nums:
            temp = max(i+fst,snd)
            fst = snd
            snd = temp
        return snd