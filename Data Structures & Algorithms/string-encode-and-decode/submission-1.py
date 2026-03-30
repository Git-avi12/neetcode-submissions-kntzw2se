class Solution:

    def encode(self, strs: List[str]) -> str:
        res=[]
        for i in strs:
            res.append(str(len(i))+"$"+i)
        s="".join(res)
        return s

    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        while i<len(s):
            n=""
            while s[i]!="$":
                n+=s[i]
                i+=1
            i+=1
            res.append(str(s[i:i+int(n)]))
            i=i+int(n)
        return res
            





