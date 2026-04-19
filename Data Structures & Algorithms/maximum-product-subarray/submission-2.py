class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod=nums[0]
        if nums[0] != 0:
            max_cur_prod = min_cur_prod = nums[0]
        else:
            max_cur_prod=min_cur_prod = 1
        for i in nums[1:]:
            if i!=0:
                t1 = max_cur_prod*i
                t2 = min_cur_prod*i
                max_cur_prod = max(t1,t2,i)
                min_cur_prod = min(t1,t2,i)
                max_prod = max(max_prod,max_cur_prod)
            else:
                max_cur_prod = min_cur_prod = 1
                max_prod = max(max_prod,0)
        return max_prod           

