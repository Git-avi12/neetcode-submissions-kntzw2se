class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cha={}
        for i in s:
            cha[i]=cha.get(i,0)+1
        for i in t:
            if i in cha and cha[i]>1:
                cha[i]=cha.get(i)-1
            elif i in cha and cha[i]==1:
                del cha[i]
            else:
                return False
        if not cha:
            return True
        return False