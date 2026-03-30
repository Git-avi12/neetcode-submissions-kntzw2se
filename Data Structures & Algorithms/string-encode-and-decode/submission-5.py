class Solution:

    def encode(self, strs: List[str]) -> str:
        s=[]
        for i in strs:
            c=str(len(i))
            s.append(c+"#"+i)
        s="".join(s)
        return s

    def decode(self, s: str) -> List[str]:
        print("hi")
        res=[]
        i=0
        c=""
        while i<len(s):
            while s[i]!="#":
                c+=s[i]
                i+=1
            else:
                i+=1
                res.append(s[i:i+int(c)])
                i=i+int(c)
                c=""
        return res
