class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="": return ""
        hs={}
        ht={}
        for i in t:
            ht[i]=ht.get(i,0)+1
        l=0
        have=0
        need=len(ht)
        res=[-1,-1]
        reslen=float("INF")
        for r in range(len(s)):
            c=s[r]
            hs[c]=hs.get(c,0)+1
            if c in ht and hs[c]==ht[c]:
                have+=1
            while have==need:
                if reslen>r-l+1:
                    res=[l,r]
                    reslen=min(reslen,r-l+1)
                hs[s[l]]-=1
                if s[l] in ht and hs[s[l]]<ht[s[l]]:
                    have-=1
                l+=1
        l,r=res
        return s[l:r+1] if reslen!=float("INF") else ""
            
            
            


        