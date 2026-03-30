class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        has = {}
        for i in s:
            has[i]=has.get(i,0)+1
        for i in t:
            if has.get(i,0)>0:
                has[i]-=1
            else:
                return False
        return True


        
