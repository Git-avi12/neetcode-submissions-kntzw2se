class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        l,r=0,1
        while r<len(prices)and l<len(prices):
            if prices[l]>prices[r]:
                l+=1
                r+=1
            else:
                profit = max(profit,prices[r]-prices[l])
                r+=1
        while l<len(prices):
            profit=max(profit,prices[r-1]-prices[l])
            l+=1
        return profit
