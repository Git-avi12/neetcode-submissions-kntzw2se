class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hs={}
        for i,n in enumerate(nums):
            if target-n in hs:
                return [hs[target-n],i]
            else:
                hs[n]=i