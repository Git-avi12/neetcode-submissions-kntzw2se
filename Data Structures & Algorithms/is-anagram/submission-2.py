class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        flag = True
        if len(s) == len(t):
            d = {}
            for i in s:
                if i not in d:
                    d[i] = 1
                else:
                    d[i]+=1
            for i in d:
                occ = d[i]
                count = 0
                for j in t:
                    if j == i:
                        count += 1
                if count != occ:
                    flag = False
        else:
            flag = False
        return flag
        
