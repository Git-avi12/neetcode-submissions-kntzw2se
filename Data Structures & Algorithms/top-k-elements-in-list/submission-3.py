class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        has={}
        pri=[[] for i in range(len(nums))]
        for i in nums:
            has[i]=has.get(i,0)+1
        for i in has:
            pri[has[i]-1].append(i)
        res=[]
        for i in pri:
            res.extend(i)
        return res[:0-k-1:-1]
