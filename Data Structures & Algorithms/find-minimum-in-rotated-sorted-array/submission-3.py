class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l,r=0,len(nums)-1
        while l<=r:
            print(l,r)
            print(nums[l],nums[r])
            if nums[l]<nums[r]:
                print(res,nums[0])
                res = min(res,nums[l])
                break
            m=(l+r)//2
            res=min(res,nums[m])
            if nums[m]>=nums[l]:
                l=m+1
            else:
                r=m-1
        return res
            
