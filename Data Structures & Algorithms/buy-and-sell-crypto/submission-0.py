class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit=0
        for i in range(len(prices)):
            day=i
            
            for j in range(i,len(prices)):
                maxprofit=max(maxprofit,prices[j]-prices[i])
        return maxprofit
