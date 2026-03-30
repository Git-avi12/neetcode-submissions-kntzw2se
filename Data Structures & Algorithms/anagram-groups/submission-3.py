class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        hs = defaultdict(list)
        for i in strs:
            c=[0]*26
            for x in i:
                c[ord(x)-ord('a')]+=1
            x=tuple(c)
            hs[x].append(i)
        return list(hs.values())