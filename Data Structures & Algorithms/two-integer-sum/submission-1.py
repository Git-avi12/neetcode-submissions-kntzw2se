class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        has = {}  
        for i,val in enumerate(nums):
            if target-val in has:
                return [has[target-val],i]
            else:
                has[val]=i
        