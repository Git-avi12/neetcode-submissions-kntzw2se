class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len=0
        max_freq=0
        l=0
        freq={}
        for r in range(len(s)): #0123
            freq[s[r]]=freq.get(s[r],0)+1
            print(freq)
            max_freq = max(max_freq,freq[s[r]])
            print(max_freq)
            if (r-l+1)-max_freq <= k:
                max_len=max(max_len,r-l+1)
                print(max_len,"l:",l,"r:",r)
            else:
                while (r-l+1)-max_freq > k:
                    l+=1
                freq[s[l-1]] = freq.get(s[l-1])-1
        return max_len



        

            
