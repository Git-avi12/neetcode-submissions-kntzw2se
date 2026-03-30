class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        S = set(nums)
        return len(S)!=len(nums)