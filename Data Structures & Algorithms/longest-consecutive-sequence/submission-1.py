class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        max_len=0
        for i in s:
            if i-1 not in s:
                temp=1
                while i+1 in s:
                    temp+=1
                    i+=1
                max_len=max(max_len,temp)
        return max_len
