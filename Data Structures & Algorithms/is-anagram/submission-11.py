class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sh = {}
        for i in s:
            sh[i] = sh.get(i,0) + 1
        for i in t:
            if i not in sh:
                return False
            sh[i]-=1
            if sh[i]<0:
                return False
        return True