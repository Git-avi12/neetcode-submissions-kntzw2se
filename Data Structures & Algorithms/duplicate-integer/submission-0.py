class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        flag = False
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j:
                    if nums[i] == nums[j]:
                        flag = True
        return flag


