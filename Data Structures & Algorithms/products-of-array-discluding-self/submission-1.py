class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[1]*n
        for i in range(n):
            if i!=0:
                res[i]=res[i-1]*nums[i-1]
        print(res)
        temp=1
        for i in range(n-1,-1,-1):
            if i!=n-1:
                temp*=nums[i+1]
                res[i]=res[i]*temp
        return res



