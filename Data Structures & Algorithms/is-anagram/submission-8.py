class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sh = {}
        for i in s:
            sh[i] = sh.get(i,0) + 1
        th = {}
        for i in t:
            th[i] = th.get(i,0) + 1
        for i in sh:
            if i not in th or th[i] != sh[i]:
                return False
            del th[i]
        if not th:
            return True
