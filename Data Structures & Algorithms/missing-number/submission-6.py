class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = set(nums)
        for i in range(len(nums)+1):
            print(i)
            if i not in n:
                return i