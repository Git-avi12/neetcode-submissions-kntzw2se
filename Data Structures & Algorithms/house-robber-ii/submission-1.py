class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob1(nums):
            fst,snd = 0,0
            for i in nums:
                temp  = max(i+fst,snd)
                fst = snd
                snd = temp
            return snd
        return max(nums[0],rob1(nums[0:-1]),rob1(nums[1:]))