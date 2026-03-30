class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_val = nums[0]
        low=0
        high=len(nums)-1
        while high>low:
            mid = (high-low//2)
            print(mid)
            if nums[mid]<min_val:
                min_val = nums[mid]
                high = mid-1
            else:
                low = mid+1
        return min_val
