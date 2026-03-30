class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_val = float("INF")
        for i in nums:
            if i<min_val:
                min_val=i
        return min_val
        