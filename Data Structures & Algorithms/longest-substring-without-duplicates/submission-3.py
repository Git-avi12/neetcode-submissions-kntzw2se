class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len=0
        l=0
        look=set()
        for r in range(len(s)):
            while s[r] in look: 
                look.remove(s[l])
                l+=1
            look.add(s[r])
            max_len = max(r-l+1,max_len)          
        return max_len