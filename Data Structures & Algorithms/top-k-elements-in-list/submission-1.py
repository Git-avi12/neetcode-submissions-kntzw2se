class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        l=[]
        l_sort=[]
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i]+=1
        l_sort = sorted(list(d.values()),reverse=True)
        for i in range(0,k):
            for j in d:
                if d[j] == l_sort[i]and j not in l:
                    l.append(j)
                    if len(l) == k:
                        return l
        
            

