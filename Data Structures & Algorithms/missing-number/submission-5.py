class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = 0
        for i in range(len(nums)+1):
            if n not in nums:
                return n
            n+=1
            