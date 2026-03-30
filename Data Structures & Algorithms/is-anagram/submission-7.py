class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt={}
        for i in s:
            cnt[i]=cnt.get(i,0)+1
        for i in t:
            if not i in cnt:
                return False
            else:
                if cnt.get(i)>1:
                    cnt[i]-=1
                else:
                    del cnt[i]
        if cnt:
            return False
        else:
            return True
